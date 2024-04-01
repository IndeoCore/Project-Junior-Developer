# Testando os conhecimentos obtidos na quinta aula do curso Introdução à Ciência da Computação com Python
# Testing the knowledge acquired during the fifth lesson of the course Introdução à Ciência da Computação com Python

# Definindo e utilizando funções para deixar o código mais limpo e evitar repetições excessivas de qualquer parte do código
# Defining and using functions to make to code cleaner e avoid unnecessary repetitions from any part of the code

import math
# without functions
"""
nx = int(input("How many numbers do you want to sum up to the first variable?: "))
i = 0
sum_x = 0
while(i < nx):
    sum_x += int(input("Type an integer to sum up:"))
    i += 1

ny = int(input("How many numbers do you want to sum up to the second variable?: "))
j = 0
sum_y = 0
while(i < ny):
    sum_y += int(input("Type an integer to sum up:"))
    i += 1

nz = int(input("How many numbers do you want to sum up to the third variable?: "))
i = 0
sum_z = 0
while(i < nz):
    sum_z += int(input("Type an integer to sum up:"))
    i += 1

sum_average = (sum_x + sum_y + sum_z) / 3
"""

# With functions
"""
def sum_n_numbers(n):
    i = 0
    sum = 0
    while(i < n):
        sum += int(input("Type an integer to sum up:"))
        i += 1
    return sum

nx = int(input("How many numbers do you want to sum up to the first variable?: "))
sum_x = sum_n_numbers(nx)
ny = int(input("How many numbers do you want to sum up to the second variable?: "))
sum_y = sum_n_numbers(ny)
nz = int(input("How many numbers do you want to sum up to the third variable?: "))
sum_z = sum_n_numbers(nz)
sum_average = (sum_x + sum_y + sum_z) / 3
"""


