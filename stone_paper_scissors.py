import random
user_choice=int(input("Enter the choices: 0 for rock, 1 for paper, 2 for scissors"))
if user_choice>=3 or user_choice<0:
    print ("invalid number, you lose")

else:
   computer_choice=random.randint(0,2)
   print("computer_choice")

   if user_choice==0 and computer_choice==2:
     print("you win")

   elif user_choice==2 and computer_choice==0:
     print("you lose")

   elif computer_choice>user_choice:
     print("You lose")

   elif user_choice>computer_choice:
     print("you win")

   elif user_choice==computer_choice:
     print("Draw")

