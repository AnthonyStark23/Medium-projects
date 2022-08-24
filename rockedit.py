import random
from colorama import Fore, Back, Style
from PIL import Image
im = Image.open(r"C:\Users\Shubham\Downloads\rock-paper-scissors2.jpg")
im.show()
print(Fore.RED+"                          "+" *********             ****           ****    **      ***            *********              **         *********      ***********   *********        ")
print(Fore.RED+"                          "+" **     ****        ***   ***        ***      **   **                **      ****         **  **       **      ****   ***********   **      ****     ")
print(Fore.RED+"                          "+" **      ***       ***      ***    ***        ** **                  **       ****       **    **      **       ****  **            **       ****    ")
print(Fore.RED+"                          "+" **     ****      ***        ***  ***         ** **          ------  **      ****       **      **     **      ****   ***********   **      ****     ")
print(Fore.RED+"                          "+" ********         ***        ***  ***         **   **                *********         ************    **********     ***********   ********         ")
print(Fore.RED+"                          "+" ** **             ***      ***    ***        **     **              **               **          **   **             **            ** ***           ")
print(Fore.RED+"                          "+" **   **            ***    ***      ****      **       **            **              **            **  **             ***********   **   ***         ")
print(Fore.RED+"                          "+" **     ****            ****          ****    **         **          **             **              ** **             ***********   **     ******    ")
print()
print()
print("                                      "+"            ******        *****       *********      ******        ******        ****         *********           ")
print("                                      "+"           ****          ****             **        ****         ****          **     **      **     ****         ")
print("                                      "+"           ****         ****              **        ****         ****         **       **     **      ****        ")
print("                                      "+"               ****     ****              **           ****        ****      **         **    **     ****         ")
print("                                      "+"                *****   *****             **             *****       *****    **        **    ********            ")
print("                                      "+"                 *****   *****            **              *****       *****    **      **     ****                ")
print("                                      "+"                *****      ****           **             *****       *****      **    **      **  ***             ")
print("                                      "+"            ******           ****     *********      ******       *****           ** **       **     ****         ")
print(Fore.GREEN+"                                                             \U0001F3C6  Winning Rules of the Rock paper scissor game as follows: \U0001F3C6 \n"
      +"                                                                                Rock vs paper->paper wins  \n"
      +"                                                                                Rock vs scissor->Rock wins \n"
      +"                                                                                Paper vs scissor->scissor wins \n"
      +"                               *** There will be Three Rounds at the end of three round winner will be declared the player having maximum wins will WIN ***")
input1='y'
i=0
while(input1 =='y' or input1 == 'Y'):
    countuser=0
    countcom=0
    while (i<3):
        print("                                                           Enter choice:- \n") 
        print("                                                           1 for Rock \U0001FAA8\n")
        print("                                                           2 for paper \U0001F4DD \n") 
        print("                                                           3 for scissor \U00002702 \n")
        
        # take the input from Player
        choice = int(input("                                                           User turn: "))     
        # looping until user enter invalid input
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))
        # initialize value of Player_move variable
        # corresponding to the choice value
        if choice == 1:
            Player_move = 'Rock'
        elif choice == 2:
            Player_move = 'paper'
        else:
            Player_move = 'scissor'
            
        # print user's move
        print("                                                           user choice is: " + Player_move)
        print("\n                                                           Now its computer turn.......")
        print("\n") 
        # Computer chooses randomly any number
        # among 1 , 2 and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)
        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'
            
        print("                                                           Computer choice is: " + comp_choice_name+"\n")
    
        print("                                                           "+Player_move + " V/s " + comp_choice_name)
        if(choice == 1 and comp_choice==2 or choice == 1 and comp_choice==2):
            print("                                                           \U0001FAA8  V/S \U0001F4DD")
        elif(choice == 2 and comp_choice==3 or choice == 3 and comp_choice==2):
            print("                                                            \U00002702  V/S \U0001F4DD")
        elif(choice == 3 and comp_choice==1 or choice == 1 and comp_choice==3):
            print("                                                           \U0001FAA8  V/S \U00002702")
        else:
            if(choice==1):
                print("                                                           \U0001FAA8  V/S \U0001FAA8")
            elif(choice==2):
                print("                                                           \U0001F4DD  V/S \U0001F4DD")
            else:
                print("                                                           \U00002702  V/S \U0001F4DD")
        #we need to check of a draw
        print("\n")
        if choice == comp_choice:
            print(Fore.RED+"                                                      **********          **********                    **                **                         **       ")
            print(Fore.RED+"                                                      **         **       **        **                **   **              **                       **        ")
            print(Fore.RED+"                                                      **          **      **       **               **       **             **                     **         ")
            print(Fore.RED+"                                                      **            **    *********               ***************            **        **         **          ")
            print(Fore.RED+"                                                      **           **     *****                 **               **            **    **   **     **           ")
            print(Fore.RED+"                                                      **          **      **   ***            **                   **           ** **       **  **            ")
            print(Fore.RED+"                                                      ***********         **      ****      **                       **          **           **              ")
        elif(choice == 1 and comp_choice == 2):
            countcom=countcom+1
            im = Image.open(r"C:\Users\Shubham\Downloads\paper.jpg")
            im.show()
        elif(choice == 2 and comp_choice ==1 ):
            countuser=countuser+1
            im = Image.open(r"C:\Users\Shubham\Downloads\paper.jpg")
            im.show()
        elif(choice == 1 and comp_choice == 3):
            countuser=countuser+1
            im = Image.open(r"C:\Users\Shubham\Downloads\rock.jpg")
            im.show()
        elif(choice == 3 and comp_choice == 1):
            countcom=countcom+1
            im = Image.open(r"C:\Users\Shubham\Downloads\rock.jpg")
            im.show()
        elif(choice == 2 and comp_choice == 3):
            countcom=countcom+1
            im = Image.open(r"C:\Users\Shubham\Downloads\scissor.jpg")
            im.show()
        elif(choice == 3 and comp_choice == 2):
            countuser=countuser+1
            im = Image.open(r"C:\Users\Shubham\Downloads\scissor.jpg")
            im.show()
        i=i+1
    # Printing either user or computer wins 
    if(countuser > countcom) :
        print(Fore.BLUE+"                               **      **      *******   *********   *********            **                     **    ********   ****       **     *****    ")
        print(Fore.BLUE+"                               **      **    ****        *********   **     ****           **                   **        **      ** **      **   ****       ")
        print(Fore.BLUE+"                               **      **   ****         **          **      ****           **                 **         **      **  **     **   ****       ")
        print(Fore.BLUE+"                               **      **     ****       *********   **     ****             **               **          **      **   **    **    ****      ")
        print(Fore.BLUE+"                               **      **        ****    *********   ********                 **     ***     **           **      **    **   **       *****  ")
        print(Fore.BLUE+"                               **      **          ****  **          *****                     **   ** **   **            **      **     **  **         **** ")
        print(Fore.BLUE+"                                **    **         *****   *********   **  ****                   ** **   ** **             **      **      ** **        ***** ")
        print(Fore.BLUE+"                                  ****       ******      *********   **    *****                 **      **            ********   **       ****     ******   ")
        print("\n")
        if(countuser == 3):
            print("                                                                              ******                 ****        ")
            print("                                                                                    ***     **      **    **      ")
            print("                                                                                    ***     **     **      **     ")
            print("                                                                                 ***              **        **    ")
            print("                                                                                 ***              **        **    ")
            print("                                                                                    ***     **     **      **     ")
            print("                                                                                    ***     **      **    **      ")     
            print("                                                                              ******                 ****        ")  
        elif(countuser == 2):
            print("                                                                               *********                            ****     ")
            print("                                                                                     *****            **           ** **     ")
            print("                                                                                      ******          **          **  **     ")
            print("                                                                                      *****                           **     ")
            print("                                                                                    ******                            **     ")
            print("                                                                              *******                 **              **     ")
            print("                                                                              *******                 **          ********** ")
            print("                                                                              **************                      ********** ")
        else:
            print("                                                                                ****              ****       ")
            print("                                                                               ** **    **     **      **    ")
            print("                                                                              **  **    **    **        **   ")
            print("                                                                                  **         **          **  ")
            print("                                                                                  **         **          **  ")
            print("                                                                                  **    **    **        **   ")
            print("                                                                               *******  **     **      **    ")
            print("                                                                               *******            ****       ")
    elif(countcom > countuser):
        print(Fore.GREEN+"                   *******      ***     ****        ****  *********    **    **  ********* **********  *********      **                          **  **********  ****         **      ******     ")
        print(Fore.GREEN+"                 ****         **   **   ** **      ** **  **     ****  **    **     **     **********  **     ****     **                        **      **       ** **        **     ****        ") 
        print(Fore.GREEN+"                ****         **     **  ** **      ** **  **     ****  **    **     **     **********  **      ****     **                      **       **       **  **       **    ****         ") 
        print(Fore.GREEN+"               ****         **       ** ** **      ** **  **     ****  **    **     **     **********  **      ****      **                    **        **       **   **      **   ****          ") 
        print(Fore.GREEN+"              ****         **        ** **  **    **  **  **      **** **    **     **     **          **    *****        **                  **         **       **    **     **    ****         ")
        print(Fore.GREEN+"               ****         **       ** **   ** **    **  **     ****  **    **     **     **********  **   *****          **                **          **       **     **    **     *****       ")
        print(Fore.GREEN+"                ****        **      **  **            **  ********     **    **     **     **********  ********             **     ****     **           **       **      **   **        ****     ")
        print(Fore.GREEN+"                 ****        **     **  **            **  **           **    **     **     **          *****                 **   **  **   **            **       **       **  **         ******  ")
        print(Fore.GREEN+"                  ****        **   **   **            **  **            **  **      **     **********  **  ****               ** **    ** **             **       **        ** **        ******   ")
        print(Fore.GREEN+"                    ******      ***     **            **  **             ****       **     **********  **     ****             **        **          **********   **         ****     ******      ")
        print("\n")
        if(countcom == 3):
            print("                                                                              ******                 ****        ")
            print("                                                                                    ***     **      **    **      ")
            print("                                                                                    ***     **     **      **     ")
            print("                                                                                 ***              **        **    ")
            print("                                                                                 ***              **        **    ")
            print("                                                                                    ***     **     **      **     ")
            print("                                                                                    ***     **      **    **      ")     
            print("                                                                              ******                 ****        ")      
        elif(countcom == 2):
            print("                                                                               *********                            ****     ")
            print("                                                                                     *****            **           ** **     ")
            print("                                                                                      ******          **          **  **     ")
            print("                                                                                      *****                           **     ")
            print("                                                                                    ******                            **     ")
            print("                                                                              *******                 **              **     ")
            print("                                                                              *******                 **          ********** ")
            print("                                                                              **************                      ********** ")
        else:
            print("                                                                                ****              ****       ")
            print("                                                                               ** **    **     **      **    ")
            print("                                                                              **  **    **    **        **   ")
            print("                                                                                  **         **          **  ")
            print("                                                                                  **         **          **  ")
            print("                                                                                  **    **    **        **   ")
            print("                                                                               *******  **     **      **    ")
            print("                                                                               *******            ****       ")   
    else:
        print(Fore.RED+"                                                      **********          **********                    **                **                         **       ")
        print(Fore.RED+"                                                      **         **       **        **                **   **              **                       **        ")
        print(Fore.RED+"                                                      **          **      **       **               **       **             **                     **         ")
        print(Fore.RED+"                                                      **            **    *********               ***************            **        **         **          ")
        print(Fore.RED+"                                                      **           **     *****                 **               **            **    **   **     **           ")
        print(Fore.RED+"                                                      **          **      **   ***            **                   **           ** **       **  **            ")
        print(Fore.RED+"                                                      ***********         **      ****      **                       **          **           **              ") 
        print("\n")
        print("                                                                               ****               ****     ")
        print("                                                                              ** **     **       ** **     ")
        print("                                                                             **  **     **      **  **     ")
        print("                                                                                 **                 **     ")
        print("                                                                                 **                 **     ")
        print("                                                                                 **     **          **     ")
        print("                                                                              ********  **       ********  ")
        print("                                                                              ********           ********  ")
    print("\n")
    print("                                                           Do you want to play again? (Y/N)")
    input1 = input()
# if user input n or N then condition is True
     
# after coming out of the while loop
# we print thanks for playing
print("\n                                                           Thanks for playing")