# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1.

film_names = ['Indiana Jones',
              'Superman',
              'Close Encounters of the Third Kind',
              'Star Wars', 'Midway',
              'Jaws',
              'The Towering Inferno']


def alphabetical_order(film_names):

    film_names.sort()
    return film_names


print(alphabetical_order(film_names))


# 2.


def won_golden_globe(film):

    winners = ['jaws',
               'star wars: episode iv - a new hope',
               'e.t. the extra-terrestrial',
               'memoirs of a geisha']
    if film.lower() in winners:
        return True
    else:
        return False


print(won_golden_globe('Jaws'))



# 3.

#   toto_albums = ['Old Is New',
#                 'Toto XIV',
#                 'Falling in Between',
#                 'Toto XX ',
#                 'The Seventh One',
#                 'Fahrenheit'
#                 ]
mixed_list = ['You Are Welcome',
              'Daddy-O',
              'I Passed for White',
              "Because They're Young",
              'The Secret Ways',
              'Toto XIV',
              'Fahrenheit'
              'Old Is New'
              ]


def remove_toto_albums(mixed_list):

    for item in mixed_list:
        if item == 'Old Is New':
            mixed_list.remove(item)
        elif item == 'Toto XIV':
            mixed_list.remove(item)
        elif item == 'Falling in Between':
            mixed_list.remove(item)
        elif item == 'Toto XX':
            mixed_list.remove(item)
        elif item == 'The Seventh One':
            mixed_list.remove(item)
        elif item == 'Fahrenheit':
            mixed_list.remove(item)

    return mixed_list


print(remove_toto_albums(mixed_list))
