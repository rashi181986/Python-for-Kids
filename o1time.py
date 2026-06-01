names  = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']
scores = [90, 75, 88, 62, 95]
n      = len(scores)

# O(1) -- index access, always 1 step:
top = scores[0]
print('O(1) index access   : score =', top, '| steps = 1')

# O(n) -- linear search, worst case n steps:
steps = 0
for name in names:
    steps += 1
    if name == 'Kabir': break
print('O(n) linear search  : steps =', steps, '| n =', n)

# O(n^2) -- nested loop, ~n*n comparisons:
steps = 0
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
print('O(n^2) pair check   : steps =', steps, '| n*(n-1)/2')

# Output:
# O(1) index access   : score = 90 | steps = 1
# O(n) linear search  : steps = 5  | n = 5
# O(n^2) pair check   : steps = 10 | n*(n-1)/2