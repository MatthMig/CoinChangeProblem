# Returns maximal decimal precision of a list of coins
def get_decimal_precision(list_coins):
    precision = 0
    for c in list_coins:
        if not '.' in str(c):
            continue
        p_coin = len(str(c).split('.')[1])
        if p_coin > precision:
            precision = p_coin
    return precision

# Returns list of possibles list of coins to change nb_units
def number_changing_possibilities(nb_units, list_coins, memory=None, precision=None):
    # Intialization
    if memory is None:
        memory = {}
    if precision is None:
        precision = get_decimal_precision(list_coins)
    if nb_units == 0:
        return []
    memory[nb_units] = []

    # Exploration of each possibility
    for c in list_coins:
        if nb_units < c:
            continue
        new_nb_units = round(nb_units - c, precision)
        # Change possibilities for nb_units-c
        change_results = number_changing_possibilities(new_nb_units, list_coins=list_coins, memory=memory, precision=precision)
        # If nb_units is in list_coins we add the change as the value in list_coins
        change_list = []
        if change_results == []:
            change_list = [[c]]
        # We add every possibility to change nb_units
        for change_result in change_results:
            change_list.append(sorted([c] + change_result))
        # We add the change to memory if it is not already in it
        for change in change_list:
            if not change in memory[nb_units]:
                memory[nb_units].append(change)
    return memory[nb_units]        

list_coins = [0.1, 0.5, 1, 2, 5]
print(len(number_changing_possibilities(nb_units=5, list_coins=list_coins)))