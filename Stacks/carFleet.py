def carFleet(target, position, speed):
    stack = []
    pair = [[p,s] for p,s in zip(position, speed)] #with list comprehension we accomplish tuple creation inside a list without the need of ".append", we simplify things.
    pair.sort(reverse=True) # we modify the list and invert the natural order (ascending) to a descending order (in-place). Un "pair.sort()" lo haria de forma ascendente, pero nosotros queremos lo contrario, por eso usamos el "reverse=True".
    for p, s in pair: # we iterate through each element (tuple) in the list of tuples.
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

print(carFleet(20, [0, 2, 15], [6, 3, 1]))
