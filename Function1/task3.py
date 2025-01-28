def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "Решение не найдено"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if isinstance(result, tuple):
    chickens, rabbits = result
    print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")
else:
    print(result)
