import random
n1 = (random.randint(1, 5), random.randint(1, 10), random.randint(1, 10), random.randint(10, 30), random.randint(1, 10))
print(n1)
print(f'O maior numero é {max(n1)} e o menor numero é {min(n1)}')
print(f'O maior numero é {sorted(n1)[-1]} e o menor é {sorted(n1)[0]}')