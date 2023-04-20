# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line


# Variables

language_most_spoken_spain = 'Castilian Spanish'
language_most_spoken_switzerland = 'German'
prevalent_religion_spain = 'Roman Catholic'
prevalent_religion_switzerland = 'Roman Catholic'
capital_name_spain = 'Madrid'
capital_name_switzerland = 'Bern'
gdp_spain = 1715000000
gdp_switzerland = 590700000000
population_growth_spain = (0.13 / 100)
population_growth_switzerland = (0.65 /100)
total_poulation_spain = 47163418 
total_poulation_switzerland = 8508698
population_at_least = 10000000


# 1. The language spoken the most in Switzerland is the same as in Spain.

language_most_spoken = language_most_spoken_spain == language_most_spoken_switzerland
print(language_most_spoken)


# 2. The most prevalent religion in Switzerland is the same as in Spain.

prevalent_religion = prevalent_religion_spain == prevalent_religion_switzerland
print(prevalent_religion)


# 3. The name length of Spain's capital does not equal that of Switzerland.

capital_name_length = len(capital_name_spain) != len(capital_name_switzerland)
print(capital_name_length)


# 4. Switzerland's GDP is greater than Spain's GDP.

greater_gdp = gdp_switzerland > gdp_spain
print(greater_gdp)


# 5. The population growth is less than 1% in Switzerland and Spain.

population_growth_less_onepercent = (1/100) > (population_growth_spain) and (1/100) > (population_growth_switzerland)
print(population_growth_less_onepercent)

# 6. At least one of the two countries has a population count of over 10 million.

population_over_tenmillion = population_at_least < total_poulation_spain or population_at_least < total_poulation_switzerland
print(population_over_tenmillion)

# 7. Exactly one of the two countries has a population count of over 10 million.

one_over_tenmillion = (total_poulation_switzerland < population_at_least and total_poulation_spain > population_at_least) or (total_poulation_switzerland > population_at_least and total_poulation_spain < population_at_least)
print(one_over_tenmillion)
