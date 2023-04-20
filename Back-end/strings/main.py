# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


# Part one

player1_scored = "Ruud Gullit"
player2_scored = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player1_scored + ' ' + str(goal_0) + ', ' + player2_scored + ' ' + str(goal_1)
print(scorers)

report = f'{player1_scored} scored in the {goal_0}nd minute\n{player2_scored} scored in the {goal_1}th minute'

print(report)



# Part two

player = 'Oleksiy Mykhaylychenko'

first_name = player[0:player.find(' ')]
print(first_name)

last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = f'{first_name[0]}. {last_name}'
print(name_short)

chant = f'{first_name}! ' * (len(first_name)-1) + (first_name + '!')
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)