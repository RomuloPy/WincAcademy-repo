# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1

leek_price = 2
cost_kilo_leek = f'Leek is {leek_price} euro per kilo.'
print(cost_kilo_leek)


# Part 2

order_leeks = 'leek 4'
quantity_leek_ordered = int(order_leeks[order_leeks.find(' ')+1:])

total_sum = leek_price * quantity_leek_ordered
print(total_sum)


# Part 3

broccoli_price = 2.34
order_broccoli = 'broccoli 1.6'

quantity_broccoli_ordered = float(order_broccoli[order_broccoli.find(' ')+1:])

total_price = broccoli_price * quantity_broccoli_ordered
print(f'{quantity_broccoli_ordered}kg broccoli costs {round(total_price, 2)}e')
