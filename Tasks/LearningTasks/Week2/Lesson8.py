# Testando os conhecimentos obtidos na oitava aula do curso Introdução à Ciência da Computação com Python
# Testing the knowledge acquired during the eighth lesson of the course Introdução à Ciência da Computação com Python

# Explorando o conceito de listas em python e aprendendo mais sobre seu funcionamento
# Exploring the concept of lists in python and learning more about how it works.


list = []

n = int(input("How many numbers your list will have: "))
step = int(input("Multiples of: "))

for x in range(0, n, step):
    list.append(x)

def list_inverter(s):
    return reversed(s)

def elements_sum(s):
    sum = 0
    for x in s:
        sum += x
    return sum

def sort_list(s):
    return sorted(s)

def print_list(s):
    for x in s:
        print(x)

print("Sum:", elements_sum(list))
print("List:")
print_list(list)
print("Inverter......")
list = list_inverter(list)
print_list(list)