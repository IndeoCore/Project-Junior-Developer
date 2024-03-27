# Testando os conhecimentos obtidos na terceira aula do curso Introdução à Ciência da Computação com Python
# Testing the knowledge acquired during the third lesson of the course Introdução à Ciência da Computação com Python

# Uso de condicionais para utilizar o valor de uma varíavel booleana, escrita de código baseada em ramificações por condicionais
# Using conditionals to use the value of a boolean variable, writing code with a branching structure by conditionals

x = int(input("Enter with an even number: "))

if(x % 2 == 0):
    print("Congratulations, your number is an even number!!")
else:
    print("I'm sorry, I think you did it wrong! Your number is an odd number!?")
    print("I'll give you one more chance!")
    x = int(input("Enter with an even number this time: "))
    if(x % 2 == 0):
        print("Now you got it. Congratulations!!")
    else:
        print("I'm sorry, it is an odd number again. You ran out of chances...")
print ("Bye bye!!")
