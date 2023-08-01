def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f'{i}. {dwarf}')

def summon_captain_planet(planeteer_calls):
    return [call.title() + '!' for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(words):
    cheeses = {"cheddar": True, "gouda": True, "camembert": True}
    for word in words:
        if cheeses.get(word):
            return word
