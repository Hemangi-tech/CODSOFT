import random

print(" *******************************************************")
print(" Winning Rules of the Game STONE, PAPER, SCISSORS")
print("1.Rock vs Scissors : Rock wins\n2.Rock vs Paper: Paper wins\n3.Paper vs Scissors: Scissor wins\n")
print(" *******************************************************")



print("Lets start the game")

while True:
    options=("Rock" , "Paper" , "Scissors")
    Computer=random.choice(options)
    choice=input("Enter your choice\n")
    

    if(choice=='rock' or 'Rock' or 'ROCK'):
       Player="Rock"
        
    elif(choice=='paper' or 'Paper' or 'PAPER'):
         Player="Paper"
    elif(choice=='scissors' or 'Scissors' or 'SCISSORS'):
        Player="Scissors"
        
    
    print("Computer choice:",Computer)
    print("Player choice:",Player)


    if(Player==Computer):
        print("its a Draw")
    elif(Player=="Rock" and Computer=="Paper"):
        result="Paper"
        print("Paper wins")
    elif(Player=="Scissors" and Computer=="Paper"):
        result="Scissors"
        print("Scissors wins")    
    elif(Player=="Paper" and Computer=="Rock"):
        result="Paper"
        print("Paper wins")
    elif(Player=="Paper" and Computer=="Scissors"):
        result="Scissors"
        print("Scissors wins")
    elif(Player=="Rock" and Computer=="Scissors"):
        result="Rock"
        print("Rock wins")
    elif(Player=="Scissors" and Computer=="Rock"):
        result="Rock"
        print("Rock wins")

    if(result==Player):
       print("Congratulations you wins !!")
    elif(result==Computer):
        print("Computers wins\nBetter Luck Next Time !!")
    else:
        print("Oops its a tie")
        
    
    c=input("Do you want to play again y for yes and n for No\n")
    if(c=="n"):
        break
    
print("Thanks for Playing")














        
        
