from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

1.


def unique_koala_facts(number):

    facts = []
    while number > 0:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(fact)
        number -= 1

    return facts


print(unique_koala_facts(7))


# 2.

def all_facts():

    list_all_facts = []
    counter = 0
    limit = 1000

    while counter < limit:
        counter += 1
        fact = random_koala_fact()
        if fact not in list_all_facts:
            list_all_facts.append(fact)

    return list_all_facts


def num_joey_facts():

    all_koala_facts = all_facts()
    joey_list = [fact for fact in all_koala_facts if "joey" in fact]
    return int(len(joey_list))


# 3.

def koala_weight():

    all_facto = all_facts()
    weight = [x for x in all_facto if "kg" in x]
    y = len(weight)
    counter = 0
    item = weight[counter]
    if y > 1:
        print("more then one")
    result = item.index("kg")
    if item[result] == "k" and result - 1 != " ":
        last_number_index = result - 1
        x = last_number_index
        # last_number = item[x]
        while item[x] != " ":
            x = x - 1
            first_number_index = x
    first_number_index = first_number_index + 1
    return int(item[first_number_index: last_number_index + 1])

print(koala_weight())
# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())


