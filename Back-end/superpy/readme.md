## Intructions to run SuperPy

1. Install Python on your computer.
2. Save SuperPy on your computer.
3. Open command-line.
4. Use "pip install" to install the modules XlsxWriter and beautifultable.
5. Go to the directory where you previously saved SuperPy and type: python super.py

```
options:
  -h, --help            show this help message and exit

subcommands:
  {today,yesterday,advance_today,products,stock,revenue,profit,buy,sell}
    today               show today's date and exit
    yesterday           show yesterday's date and exit
    advance_today       advance 'today' with n days and exit
    products            show the offered products and exit
    stock               show the current stock and exit
    revenue             show the revenue for period x and exit
    profit              show the profit for period x and exit
    buy                 record a purchase in bought.csv and exit
    sell                record a sale in sold.csv and exit

For subcommand help, enter 'python super.py <subcommand> -h'.
```

## Access help

As you can see in the example above, help is displayed when running the program. Subcommand help can be accessed by entering 'python super.py \<subcommand\> -h'. Any positional (i.e. required) or optional arguments will be displayed in the subcommand help.

**E.g.** get help on "today" subcommand (takes no arguments):

```
...\>python super.py today [-h]

show today's date and exit

options:
  -h, --help  show this help message and exit
```

**E.g.** get help on "products" subcommand (takes two optional arguments):

```
...\>python super.py products -h
...\>python super.py products [-h] [-csv] [-excel]

show the offered products and exit

options:
  -h, --help  show this help message and exit
  -csv        export the offered products to products.csv
  -excel      export the offered products to products.xlsx
```

**E.g.** get help on "buy" subcommand (takes five positional arguments):

```
...\>python super.py buy -h
...\>python super.py buy [-h] product date price expiration count

record a purchase in bought.csv and exit

positional arguments:
  product      product name      - singular noun
  date         purchase date     - YYYY-MM-DD
  price        purchase price    - floating point number
  expiration   expiration date   - YYYY-MM-DD
  count        product count     - integer

options:
  -h, --help  show this help message and exit
```

## Execute a subcommand

To execute a subcommand, enter 'python super.py \<subcommand\> \[arguments\]'. The program will then call a function with the same name, e.g. today() after "today" has been entered.

### **- today**

Subcommand to show today's date in the terminal.
The function today() prints today's date to the standard output, stdout.
Today's date is the date recorded in the text file "today.txt".
Today() takes no positional or optional arguments.

To execute "today", enter 'python super.py today'.

If no date has been recorded in "today.txt", the current date is printed:

```
...\>python super.py today
Today: 2023-03-01
```

If today has been advanced by a number of days using the "advance_today" subcommand described below, the advanced date is printed:

```
...\>python super.py today
Today: 2023-02-28
```

### **- yesterday**

Subcommand to show yesterday's date in the terminal.
The function yesterday() prints yesterday's date to the standard output, stdout.
Yesterday's date is calculated relative to the date recorded in the text file "today.txt" as today's date.
Yesterday() takes no positional or optional arguments.

To execute "yesterday", enter 'python super.py yesterday':

```
...\>python super.py yesterday
Yesterday: 2023-02-28
```

### **- advance_today**

Subcommand to advance 'today' with n days.
The function advance_today() advances today's date - as recorded in today.txt - with n days.
Advance_today() takes one positional argument (days).

To execute "advance_today", enter: 'python super.py advance_today \<days\>':

```
python super.py advance_today 2
Today is advanced with 2 days from 2023-03-01 to 2023-02-27.
```

The 'new today' is recorded in today.txt:

```
2023-02-27
```

You can go back any number of days, e.g.:

```
python super.py advance_today 90
Today is advanced with 90 days from 2023-03-01 to 2022-12-01.
```

Going back to a year BC will throw an OverflowError:

```
2500 years = 912.500 days

super.py advance_today 912500
Traceback (most recent call last):
  File "C:\Users\Romulo\OneDrive\Documentos\Winc_Academy\Back-end\superpy\super.py", line 104, in <module>
    main()
  File "C:\Users\Romulo\OneDrive\Documentos\Winc_Academy\Back-end\superpy\super.py", line 100, in main
    args.func(args)
  File "C:\Users\Romulo\OneDrive\Documentos\Winc_Academy\Back-end\superpy\helpers.py", line 301, in advance_today
    new_today = today - timedelta(days)
                ~~~~~~^~~~~~~~~~~~~~~~~
OverflowError: date value out of range
    new_today = today - timedelta(days)
OverflowError: date value out of range
```

### **-products**

Subcommand to show the offered products in the terminal.
The function products() prints the offered products to the standard output, stdout.
Products() takes two optional arguments (-csv and -excel).
The optional arguments make the function export the offered products to either products.csv or products.xlsx.

To execute "products", enter: 'python super.py products':

```
...\>python super.py products
...........
: product :
...........
: beer :
: juice :
: water :
: wine :
...........

```

To execute "products" with the option -csv, enter: 'python super.py products -csv':

```
...\>python super.py products -csv
offered products exported to products.csv
```

The offered products are now exported to products.csv:

```
product
beer
juice
water
wine
```

To execute "products" with the option -excel, enter: 'python super.py products -excel':

```
...\>python super.py products -excel
offered products exported to products.xlsx
```

Open the file products.xlsx in Excel to see the result.

### **-stock**

Subcommand to show the current stock in the terminal.
The function stock() prints the current stock to the standard output, stdout.
The current stock is the stock on today's date as recorded in today.txt.
Stock() takes two optional arguments (-csv and -excel).
The optional arguments make the function export the current stock to either stock.csv or stock.xlsx.

To execute "stock", enter: 'python super.py stock':

```
...\>python super.py stock
Stock today (2023-03-01):
.......................
: product :     stock :
.......................
: beer    :        80 :
: juice   :       150 :
: water   :       100 :
: wine    :        35 :
.......................

```
To execute "stock" with the option -csv, enter: 'python super.py stock -csv':

```
...\>python super.py stock -csv
current stock exported to stock.csv

```

The current stock is now exported to stock.csv:

```
product,stock
beer,80
juice,150
water,100
wine,35
```

To execute "stock" with the option -excel, enter: 'python super.py stock -excel':

```
...\>python super.py stock -excel
current stock exported to stock.xlsx
```

Open the file stock.xlsx in Excel to see the result.

### **-revenue**

Subcommand to show the revenue for period x in the terminal.
The function revenue() prints the revenue for period x to the standard output, stdout.
Revenue() takes three optional arguments (-today, -yesterday and -month).

To execute "revenue", enter 'python super.py revenue \[option]'.

If you execute "revenue" without an option, the program will prompt you to add one:

```
...\>python super.py revenue
please enter an option - see 'python super.py revenue -h'
```

With the option "-today":

('Today' is today's date as recorded in today.txt.)

```
...\>python super.py revenue -today
Revenue today (2023-03-01):
0
```

With the option "-yesterday":

```
...\>python super.py revenue -yesterday
Revenue yesterday (2023-03-01):
0
```

With the option "-month":

```
...\>python super.py revenue -month mar-2023
Revenue March 2022:
62.5
```

### **-profit**

Subcommand to show the profit for period x in the terminal.
The function profit() prints the profit for period x to the standard output, stdout.
Profit() takes three optional arguments (-today, -yesterday and -month).

To execute "profit", enter 'python super.py profit \[option]'.

If you execute "profit" without an option, the program will prompt you to add one:

```
...\>python super.py profit
please enter an option - see 'python super.py profit -h'
```

With the option "-today":

('Today' is today's date as recorded in today.txt.)

**E.g.** with today == 2023-03-01:

```
...\>python super.py profit -today
Profit today (2023-03-01):
-407.5
```

With the option "-yesterday":

```
...\>python super.py profit -yesterday
Profit yesterday (2023-02-28):
0
```

With the option "-month":

```
...\>python super.py profit -month mar-2023
Profit March 2023:
-345.0
```

### **- buy**

Subcommand to record a purchase in bought.csv.
The function buy() appends the entered data to this csv file.
Buy() takes five positional arguments: product, date, price, expiration and count.

To execute "buy", enter 'python super.py buy \<product\> \<date\> \<price\> \<expiration\> \<count\>':

```
...\>python super.py buy water, 2023-03-01, 0.5, 2024-06-10, 100
purchase recorded in bought.csv
```

The purchase data is now appended to bought.csv:

```
product,date,price,expiration,count
water,2023-03-01,0.5,2024-06-10,100
```


### **- sell**

Subcommand to record a sale in sold.csv.
The function sell() appends the entered data to this csv file.
Sell() takes four positional arguments: product, date, price and count.

To execute "sell", enter 'python super.py sell \<product\> \<date\> \<price\> \<count\>':

```
...\>python super.py sell juice 2023-03-05 2.5 25
sale recorded in sold.csv
```

The sale data is now appended to sold.csv:

```
product,date,price,count
juice,2023-03-05,2.5,25
```