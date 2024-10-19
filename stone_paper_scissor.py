
import random
print("Deepak Projects #2")
print("Welcome to the game of Stone Paper Scissor")
a = random.choice(['stone','paper','Scissor'])
x = print("enter 1 = stone \n      2 = paper \n      3 = scissor")
b = input("Enter 1 for stone, 2 for paper, or 3 for scissor: ")
if b == '1':
	print("You chose stone")
elif b == '2':
	print("You chose paper")
elif b == '3':
	print("You chose scissor")

    
print("Computer Choosed ",a)


if a == 'stone' and b == '1':
    print("Both chosed same , Draw")
    
elif a == 'stone' and b == '2':
    print("Computer win ")
    
elif a == 'stone' and b == '3':
    print("Computer win ")
    
elif a == 'paper' and b == '1':
    print("You won ")
    
elif a == 'paper' and b == '2':
    print("Both chosed same,Draw ")
    
elif a == 'paper' and b == '3':
    print("You won ")
    
elif a == 'Scissor' and b == '1':
    print("You won ")
    
elif a == 'Scissor' and b == '2':
    print("Computer win ")
    
elif a == 'Scissor' and b == '3':
    print("Both chosed same,Draw ")






