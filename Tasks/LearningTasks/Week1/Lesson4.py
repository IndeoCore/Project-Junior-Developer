# Testando os conhecimentos obtidos na quarta aula do curso Introdução à Ciência da Computação com Python
# Testing the knowledge acquired during the fourth lesson of the course Introdução à Ciência da Computação com Python

# Usando o laço de repetição "while" para iterar alguma condição englobando todos os conhecimentos obtidos até então
# Using loop structure "while" to iterating a condition encompassing all the knowledge obtained until now

print("When you have more odd digits than even digits you have an odd plus number.")
print("This is analogous for even numbers. If even and odd digits are in the same amount, you will have a neutral number.")
n = int(input("Enter with a number to verificate which one it is: "))

oddCount = 0
evenCount = 0

while(n != 0):
    if ((n % 10) % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1
    n = n // 10

if(evenCount > oddCount):
    print("Your number is an even+ number!!")
else: 
    if(oddCount > evenCount):
        print("Your number is an odd+ number!!")
    else:
        print("What a coincidence! Your number is neutral.")

