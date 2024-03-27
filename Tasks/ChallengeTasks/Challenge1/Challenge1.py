import random
s = range(1, 101)
rand = random.choice(s)
attempts = 10
win = False

def tentativa(num, rand):
    if num == rand:
        return True
    else:
        return False

print("Hello! Welcome to the Number Guesser Game!")
print("\nThe rules of the game are very simple:")
print("\n- You'll have 10 attempts to guess a number in " +
       "the range of 1 to 100")
print("- After each attempt, I'll tell you if the number is "+
      "higer or lower than your guess, to help you a little.")
print("- If you guess it right, before your attempts are over, "+
      "you win. Otherwise, you lose.")
print("- Fun fact: Mathematically you would have a 10% "+ "chance of " +
      "winning the game if I didn't give you any tips.")
print("- It means that without the tips you should win 1 out "+
      "of 10 times you play the game.")
print("- With the tips I'll give you and if you use certain logic, "+
      "you could always win the game with 7 tries or less!")
print("- Good thing that I'm a kind host, no?")
print("\nLet's get started. Good Luck!\n")

while(attempts > 0 and not win):
    print("Attempts left:", attempts)
    x = int(input("\nType your guess: "))
    win = tentativa(x, rand)
    if(x > rand and attempts > 1):
        print("\nA little above... Try a lower number in the next try!")
    if(x < rand and attempts > 1):
        print("\nYou're under... Try a higher number in the next try!")
    attempts -= 1

attempts_need = 10 - attempts

if(win):
    print("\nCongratulations! You won the game!")
    if(attempts == 9):
        print("Impressive! You got it in the first try! Lucky one!")
    if(attempts == 0):
        print("Phew!! You almost lost! You had no more attempts")
    if(attempts >= 5 and attempts < 9):
        print("And it only took you", attempts_need, "attempts!")
    if(attempts > 0 and attempts < 5):
        print("It took you", attempts_need, "attempts.")
else:
    print("\nUnfortunately, you lost! I'm sorry for that, but you can always try again!")
