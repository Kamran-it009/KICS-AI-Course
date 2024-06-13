# for loop
# while loop


n = 1
# infinite loops
while n <= 5:
    print(f'{n}:Hello Batch-13')
    n = n + 1

# Example while loop
n = 2
while n <= 20:
    print(n)
    n = n + 2

# Example of for loop
# range(start, end, step)
for i in range(2, 22, 2):
    print(i)

# Example of break statement
for i in range(10):
    print(i)
    if i == 5:
        break

# Example of continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)
    
# Nested Loops
for i in range(5):
    for j in ['apple', 'banana', 'cherry']:
        print(f'{i}- {j}')
    print()
