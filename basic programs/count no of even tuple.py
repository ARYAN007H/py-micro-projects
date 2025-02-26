

pairs = ((2, 5), (4, 2), (9, 8), (12, 10))


even_pair_count = 0

for a, b in pairs:

    if a % 2 == 0 and b % 2 == 0:
        even_pair_count += 1


print("Number of pairs where both a and b are even:", even_pair_count)
