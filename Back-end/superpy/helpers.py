# Imports
import argparse
import csv
from time import strptime
from datetime import datetime, date, timedelta
from calendar import monthrange
from beautifultable import BeautifulTable
import xlsxwriter

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

def product_list():
    product_list = []
    with open('bought.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            product = row['product']
            if product not in product_list:
                product_list.append(product)
    product_list.sort()
    return product_list


def products(args):
    offered_products = product_list()
    no_products = len(offered_products) == 0

    if no_products:
        print("no products offered!")
    else:
        if args.csv:
            filename = "products.csv"
            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product"])
                for product in offered_products:
                    writer.writerow([product])
            print("offered products exported to products.csv!")
        elif args.excel:
            workbook = xlsxwriter.Workbook('products.xlsx')
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})
            products = ()
            for product in offered_products:
                products = products + (product,)
            row = 0
            col = 0
            worksheet.write(row, 0, 'product', bold)
            row = 1
            col = 0
            for product in (products):
                worksheet.write(row, col,     product)
                row += 1
            workbook.close()
            print("offered products exported to products.xlsx")
        else:
            table = BeautifulTable()
            for product in offered_products:
                table.rows.append([product])
            table.columns.header = ["product"]
            table.columns.alignment["product"] = BeautifulTable.ALIGN_LEFT
            table.set_style(BeautifulTable.STYLE_DOTTED)
            print(table)


def product_stock(product, date):
    def amount_sellable():
        amount_sellable = 0
        with open('bought.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d") and row['expiration'] > date.strftime("%Y-%m-%d"):
                    amount_sellable += int(row['count'])
            return amount_sellable

    def amount_sold():
        amount_sold = 0
        with open('sold.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d"):
                    amount_sold += int(row['count'])
            return amount_sold

    amount_sellable = amount_sellable()
    amount_sold = amount_sold()
    product_stock = amount_sellable - amount_sold
    return product_stock


def stock(args):
    offered_products = product_list()
    no_products = len(offered_products) == 0
    today = get_today_obj()
    if no_products:
        print("No stock available")
    else:
        if args.csv:
            filename = "stock.csv"
            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product", "stock"])
                for product in offered_products:
                    stock = product_stock(product, today)
                    writer.writerow([product, stock])
            print("Stock exported to stock.csv")
        elif args.excel:
            workbook = xlsxwriter.Workbook('stock.xlsx')
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})

            total_stock = ()
            for product in offered_products:
                stock = product_stock(product, today)
                total_stock = total_stock + ([product, stock],)

            row = 0
            col = 0
            worksheet.write(row, col, 'product', bold)
            worksheet.write(row, col + 1, 'stock', bold)
            row = 1
            col = 0
            for product, amount in (total_stock):
                worksheet.write(row, col,     product)
                worksheet.write(row, col + 1, amount)
                row += 1
            workbook.close()
            print("Stock exported to stock.xlsx")

        else:
            print(f"Stock today ({today}):")
            table = BeautifulTable()
            for product in offered_products:
                stock = product_stock(product, today)
                table.rows.append([product, stock])
            table.columns.header = ["product", "stock"]
            table.columns.alignment["product"] = BeautifulTable.ALIGN_LEFT
            table.columns.alignment["stock"] = BeautifulTable.ALIGN_RIGHT
            table.columns.padding_left["stock"] = 5
            table.set_style(BeautifulTable.STYLE_DOTTED)
            print(table)


def period_result(filename, period):
    with open(filename) as csvfile:
        month = strptime(period, '%B %Y').tm_mon
        year = strptime(period, '%B %Y').tm_year
        _, days_in_month = monthrange(year, month)
        start_date = date(year, month, 1).strftime('%Y-%m-%d')
        end_date = date(
            year, month, days_in_month).strftime('%Y-%m-%d')
        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] >= start_date and row['date'] <= end_date:
                result += float(row['price'])*float(row['count'])
        return result


def day_result(filename, day):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] == str(day):
                result += float(row['price'])*float(row['count'])
        return result


def result(args):
    subcommand = args.subcommand
    if args.today is None and args.yesterday is None and args.month is None:
        print(
            f"Choose an option - see 'python super.py {subcommand} -h'")
    else:
        if args.today:
            today = read_today_str()
            revenue = day_result("sold.csv", today)
            cost = day_result("bought.csv", today)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue today ({today}):")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit today ({today}):")
                print(profit)
        if args.yesterday:
            today = get_today_obj()
            yesterday = today - timedelta(1)
            revenue = day_result("sold.csv", yesterday)
            cost = day_result("bought.csv", yesterday)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue yesterday ({yesterday}):")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit yesterday ({yesterday}):")
                print(profit)
        if args.month:
            period = args.month
            revenue = period_result("sold.csv", period)
            cost = period_result("bought.csv", period)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue {period}:")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit {period}:")
                print(profit)


def revenue(args):
    result(args)


def profit(args):
    result(args)


def buy(args):
    if args.date > date.today():
        purchase_date = args.date.strftime("%Y-%m-%d")
        print(f"Purchase not recorded - {purchase_date} is a future date. Enter past or current date...")
    if args.expiration <= date.today():
        expiration_date = args.date.strftime("%Y-%m-%d")
        print(f"Purchase not recorded - {expiration_date} is a past or current date. Enter a future date...")
    else:
        filename = "bought.csv"
        data = [args.product, args.date, args.price,
                args.expiration, args.count]

        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
        print(f"Purchase recorded in bought.csv")


def sell(args):
    
    product = args.product
    date = args.date
    count = args.count
    stock = product_stock(product, date)
    
    if args.date > date.today():
        sale_date = args.date.strftime("%Y-%m-%d")
        print(
            f"Sale not recorded - {sale_date} is a future date. Enter past or current date...")
    else:
        if stock < count:
            print(f"{product.capitalize()} in stock on {date}: {stock}.")
            print(f"Sale not recorded - {count} is more then actual stock({stock}).")
        else:
            filename = "sold.csv"
            data = [args.product, args.date, args.price, args.count]

            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
            print(f"Sale recorded in sold.csv")


def read_today_str():
    with open('today.txt', 'r') as textfile:
        today = textfile.read()
    return today


def get_today_obj():
    today = read_today_str()
    today_obj = datetime.strptime(today, "%Y-%m-%d").date()
    return today_obj


def today(args):
    today = read_today_str()
    if today == "":
        with open('today.txt', 'w') as textfile:
            current_date = date.today().strftime("%Y-%m-%d")
            textfile.write(current_date)
        print(f"Today: {current_date}")
    else:
        print(f"Today: {today}")


def yesterday(args):
    today = get_today_obj()
    yesterday = today - timedelta(1)
    print(f"Yesterday: {yesterday}")


def advance_today(args):
    today = get_today_obj()
    days = args.days
    new_today = today - timedelta(days)


    with open('today.txt', 'w') as textfile:
        new_today_str = new_today.strftime("%Y-%m-%d")
        textfile.write(new_today_str)

    print(
        f"Today is advanced with {days} days from {today} to {new_today_str}.")


def valid_month(date_string):
    try:
        return datetime.strptime(date_string, "%b-%Y").strftime("%B %Y")
    except ValueError:
        msg = f"'{date_string}' - Format should be month-year, e.g. jan-2023".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)


def valid_date(date_string):

    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        msg = f"{date_string} - Should be an existing date in the format YYYY-MM-DD".format(date_string)
        raise argparse.ArgumentTypeError(msg)


def lowercase(string):
    return string.lower()
