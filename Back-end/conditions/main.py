# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cow_milking_status, location_cows, season, slurry_tank, grass_status):

    if location_cows == 'pasture' and time_of_day == 'night':
        return ('take cows to cowshed')
    elif location_cows == 'pasture' and weather == 'rainy':
        return ('take cows to cowshed')

    if cow_milking_status is True and location_cows == 'pasture':
        return ('take cows to cowshed\nmilk cows\ntake cows back to pasture')

    if slurry_tank is True and location_cows == 'pasture':
        return ('take cows to cowshed\nFertilize pasture\ntake cows back to pasture')

    if grass_status is True and season == 'spring' and weather == 'sunny':
        return ('take cows to cowshed\nyou can mow the lawn now\ntake cows back to pasture')

    if location_cows == 'cowshed' and cow_milking_status == True:
        return ('milk cows')

    if slurry_tank is True and location_cows == 'cowshed' and (weather != 'sunny' or weather != 'windy'):
        return ('fertilize pasture')

    if grass_status is True and season == 'spring' and weather == 'sunny' and location_cows != 'pasture':
        return ('you can mow the lawn now')
    else:
        return ('wait')


print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
