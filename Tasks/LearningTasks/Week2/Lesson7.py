# Testando os conhecimentos obtidos na sétima aula do curso Introdução à Ciência da Computação com Python
# Testing the knowledge acquired during the seventh lesson of the course Introdução à Ciência da Computação com Python

# Repetições encaixadas, o jeito mais eficiente de usar repetições dentro de repetições
# Nested loops, the more efficient way to use repetitions loop inside another loop

# Retornando a soma de todos os elementos de uma matriz
# Returning the sum of all elements of a matrix

row = int(input("Number of rows: "))
col = int(input("Number of columns: "))
elements_sum = 0
i = 0
while(i < row):
    j = 0
    while(j < col):
        print("Type the", i+1, j+1, "element of the matrix: ", end="")
        elements_sum += int(input())
        j += 1
    i+=1
print("sum =", elements_sum)