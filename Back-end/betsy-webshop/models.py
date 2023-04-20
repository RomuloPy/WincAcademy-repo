import peewee

db = peewee.SqliteDatabase("database.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = peewee.CharField(unique=True)
    description = peewee.TextField()
    price = peewee.DecimalField(decimal_places=2, auto_round=True)
    quantity = peewee.IntegerField(null=True)


class Tag(BaseModel):
    name = peewee.CharField(unique=True)
    product = peewee.ForeignKeyField(Product, backref='tags')


class User(BaseModel):
    name = peewee.CharField(unique=True)
    address = peewee.TextField()
    billing_info = peewee.TextField()
    products_owned = peewee.ManyToManyField(Product, backref='users')


class Transaction(BaseModel):
    user_id = peewee.ForeignKeyField(User, backref='transactions')
    product_id = peewee.ForeignKeyField(Product, backref='transactions')
    quantity = peewee.IntegerField()


UserProduct = User.products_owned.get_through_model()


def populate_test_data():
    db.create_tables([Product, Tag, User, Transaction, UserProduct])

    product_data = [
        ('microphone', '''A microphone, colloquially called a mic or mike, is a transducer that converts sound into an electrical signal.''',
        150, 1, ('voice_object', 'england', 'metal')),

        ('guitar', '''The guitar is a fretted musical instrument that typically has six strings.''',
         285, 1, ('instrument', 'wood', 'us')),

        ('drums', '''The drum is a member of the percussion group of musical instruments.''', 550, 1, ('percussion_instrument', 'wood', 'china')),

        ('pick', '''A guitar pick is a plectrum used for guitars. Picks are generally made of one uniform material—such as some kind of plastic''',
         0.8, 1, ('accessory', 'plastic', 'n/a')),
    ]

    user_data = [
        ('bruno', 'eindhovenstraat 13', 'AS150883', ['microphone']),
        ('natalia', 'polenstraat 7', 'BS130290', ['pick']),
        ('jason', 'moederlaan 49', 'CS120212', ['drums'])
    ]

    for name, description, price, quantity, tags in product_data:
        product = Product.create(
            name=name, description=description, price=price, quantity=quantity)
        for tag in tags:
            Tag.create(name=tag, product=product)

    for name, address, billing_info, products_owned in user_data:
        user = User.create(
            name=name, address=address, billing_info=billing_info)
        for product in products_owned:
            user.products_owned.add(Product.get(Product.name == product))
