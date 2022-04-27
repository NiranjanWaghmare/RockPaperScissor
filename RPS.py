import random

print("="*100)   
print("Lets play Rock Paper Scissor!!!")

game = ['rock', 'paper', 'scissor']
p = 0 #player score
c = 0 #computer score
entry = input("Yesss (yes) | Not interested (no) :  ").lower()

if entry == "yes":
    while True:
        print("-"*100)   
        print("lets do this")
        choicep=input("Rock, Paper or Scissor: ").lower()
        if choicep == 'rock' or choicep == 'paper' or choicep == 'scissor':
            
            print("Player : "+choicep.upper())
            comp = random.choice(game)
            print("Computer: "+ comp.upper())
            if (choicep == 'rock' and comp == 'rock') or (choicep == 'scissor' and comp == 'scissor') or (choicep == 'paper' and comp == 'paper'):
                print("Its a Tie. Try Again, Nobody Won")
            if choicep == 'rock' and comp == 'paper':
                print("Computer win, You lose")
                c +=1
            if choicep == 'rock' and comp == 'scissor':
                print("You win, Hurray!!") 
                p +=1
            if choicep == 'scissor' and comp == 'rock':
                print("Computer win, You lose")
                c +=1      
            if choicep == 'scissor' and comp == 'paper':
                print("You win, Hurray!!")
                p +=1
            if choicep == 'paper' and comp == 'rock':
                print("You win, Hurray!!")
                p +=1
            if choicep == 'paper' and comp == 'scissor':
                print("Computer win, You lose")
                c +=1
        else:
            print("Wrong choice")
        print("Wanna play another round")   
        #print("  %d %d " %(p, c))
        entry = input("yes or no : ").lower()
        if entry != "yes":
            print("Final Scores are  ")
            print("-"*25) 
            print("Your Score :  %d" %p)
            print("-"*25) 
            print("Computer Score :  %d" %c)
            print("-"*25) 
            if c>p:
                print("You LOSE the Series, Better luck next time")
            elif p>c:
                print("You WON the Series, Hurray!!!!!!")  
            else:
                print("Its a Tie. Try Again, Nobody Won the Series")
            break


else:
    print("OK, next time ")

print("Bye....")   
print("="*100)   