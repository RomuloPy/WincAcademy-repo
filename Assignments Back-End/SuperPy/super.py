import argparse


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


def main():
    from helpers import today, yesterday, advance_today, products, stock, revenue, profit, buy, sell, valid_month, valid_date, lowercase

    parser = argparse.ArgumentParser(
        usage="python %(prog)s", epilog="For subcommand help, enter 'python super.py <subcommand> -h'.")
    subparsers = parser.add_subparsers(
        title="subcommands", prog="python super.py", dest="subcommand")

    parser_today = subparsers.add_parser(
        "today", description="shows today's date and exit", help="shows today's date and exit")
    parser_today.set_defaults(func=today)

    parser_yesterday = subparsers.add_parser(
        "yesterday", description="shows yesterday's date and exit", help="shows yesterday's date and exit")
    parser_yesterday.set_defaults(func=yesterday)

    parser_advance_today = subparsers.add_parser(
        "advance_today", description="advance 'today' with n days and exit", help="advance 'today' with n days and exit")
    parser_advance_today.add_argument("days", type=int, help="number of days")
    parser_advance_today.set_defaults(func=advance_today)

    parser_products = subparsers.add_parser(
        "products", description="shows the offered products and exit", help="shows the offered products and exit")
    parser_products.add_argument(
        "-csv", action="store_const", const="products.csv", help="export the offered products to products.csv")
    parser_products.add_argument(
        "-excel", action="store_const", const="products.xlsx", help="export the offered products to products.xlsx")
    parser_products.set_defaults(func=products)

    parser_stock = subparsers.add_parser(
        "stock", description="shows the current stock and exit", help="shows the current stock and exit")
    parser_stock.add_argument(
        "-csv", action="store_const", const="stock.csv", help="export the current stock to stock.csv")
    parser_stock.add_argument(
        "-excel", action="store_const", const="stock.xlsx", help="export the current stock to stock.xlsx")
    parser_stock.set_defaults(func=stock)

    parser_revenue = subparsers.add_parser(
        "revenue", description="shows the revenue for period x and exit", help="shows the revenue for period x and exit")
    parser_revenue.add_argument(
        "-today", action="store_const", const="today", help="shows today's revenue")
    parser_revenue.add_argument(
        "-yesterday", action="store_const", const="yesterday", help="shows yesterday's revenue")
    parser_revenue.add_argument(
        "-month", type=valid_month,
        help="shows revenue of a month - e.g. JAN-2023")
    parser_revenue.set_defaults(func=revenue)

    parser_profit = subparsers.add_parser(
        "profit", description="shows the profit for period x and exit", help="shows the profit for period x and exit")
    parser_profit.add_argument(
        "-today", action="store_const", const="today", help="shows today's profit")
    parser_profit.add_argument(
        "-yesterday", action="store_const", const="yesterday", help="shows yesterday's profit")
    parser_profit.add_argument(
        "-month", type=valid_month,
        help="shows profit of a month - e.g. JAN-2023")
    parser_profit.set_defaults(func=profit)

    parser_buy = subparsers.add_parser(
        "buy", description="record a purchase in bought.csv and exit", help="record a purchase in bought.csv and exit")
    parser_buy.add_argument("product", type=lowercase,
                            help="product name - singular noun")
    parser_buy.add_argument("date", type=valid_date,
                            help="purchase date - YYYY-MM-DD")
    parser_buy.add_argument("price", type=float,
                            help="purchase price - floating point number")
    parser_buy.add_argument("expiration", type=valid_date,
                            help="expiration date - YYYY-MM-DD")
    parser_buy.add_argument("count", type=int, help="product count - integer")
    parser_buy.set_defaults(func=buy)

    parser_sell = subparsers.add_parser(
        "sell", description="record a sale in sold.csv and exit", help="record a sale in sold.csv and exit")
    parser_sell.add_argument("product", type=lowercase,
                             help="product name - singular noun")
    parser_sell.add_argument("date", type=valid_date,
                             help="sale date - YYYY-MM-DD")
    parser_sell.add_argument("price", type=float,
                             help="sale price - floating point number")
    parser_sell.add_argument("count", type=int, help="product count - integer")
    parser_sell.set_defaults(func=sell)


    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()