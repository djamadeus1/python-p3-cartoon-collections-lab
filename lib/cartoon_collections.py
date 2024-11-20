def roll_call_dwarves(lst):
    num = 0
    for every_dwarf in lst:
        num += 1
        print(str(num) + ". " + every_dwarf)

def summon_captain_planet(lst):
    result = []
    for every_word in lst:
        new_word = every_word.capitalize() + "!"
        result.append(new_word)
    return result    


def long_planeteer_calls(lst):
    for every_word in lst:
        if len(every_word) > 4:
            return True
    return False

def find_the_cheese(lst):
    cheese = ["cheddar", "gouda", "camembert"]
    result = [word for word in cheese if word in lst]
    if len(result) > 0:
        return result[0]
    else:
        return None
