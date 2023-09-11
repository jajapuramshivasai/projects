import matplotlib.pyplot as plt

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

with open('test.dat', 'r') as input_file, open('fact.txt', 'w') as output_file:
    for line in input_file:
        number = int(line.strip())
        fact = factorial(number)
        output_file.write(f"{number},{fact}\n")
numbers = []
factorials = []

with open('fact.txt', 'r') as fact_file:
    for line in fact_file:
        number, fact = map(int, line.strip().split(','))
        numbers.append(number)
        factorials.append(fact)

plt.figure(figsize=(10, 6))
plt.plot(numbers, factorials, marker='o', linestyle='-', color='b')
plt.xlabel('Number')
plt.ylabel('Factorial')
plt.title('Factorials vs. Numbers')
plt.grid(True)
plt.savefig('factorial_plot.png')
plt.show()