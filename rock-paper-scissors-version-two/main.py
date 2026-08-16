#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1
if False:
    import random
    print("Welcome to the rock, paper, scissors game.")
    user_typed = input("Press enter to continue or type (Help), for the rules. \n").lower()
    if user_typed == "help":
        print("""
    =====================================================
            ROCK, PAPER, SCISSORS — RULES
    =====================================================

    HOW TO PLAY:
    *Type ROCK, OR: PAPER, OR: SCISSORS, and press enter.
    *The computer will choose a random choice. 
    *The result will appear to show who is the winner, YOU OR THE COMPUTER?
    -----------------------------------------------------
                    THE THREE CHOICES
    -----------------------------------------------------

        ROCK                     PAPER                  SCISSORS
        _______                  _______                  _______
    ---'   ____)              ---'   ____)____         ---'   ____)____
        (_____)                       ______)                  ______)
        (_____)                       _______)              __________)
        (____)                       _______)              (____)
    ---.__(___)               ---.__________)          ---.__(___)

    -----------------------------------------------------
                    WHO WINS WHAT?
    -----------------------------------------------------

    [ ROCK ]     crushes   [ SCISSORS ]  -->  Rock wins!
    [ SCISSORS ] cuts      [ PAPER ]     -->  Scissors wins!
    [ PAPER ]    covers    [ ROCK ]      -->  Paper wins!

    * Same choice by both players? It's a TIE! Re-roll!

    =====================================================
    """)
    elif user_typed:
        print(f"You must type (help) to reveal the rules. OR: press enter to skip the rules. You pressed: {user_typed}")
    user_choice = input("Enter your choice. (rock, paper, scissors): \n").lower()
    right_choices = ["rock","paper","scissors"]
    if user_choice in right_choices:
        print("This is your choice:")
        if user_choice == "rock":
            print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
                
            """)
        elif user_choice == "paper":
            print("""
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

            """)
        elif user_choice =="scissors":
            print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
                
            """)
    else:
        print("You must choose: (rock) or (paper) or (scissors). You choose:",user_choice)
    computer_choice = random.choice(right_choices)
    print("This is the computer choice:")
    if computer_choice == "rock":
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
                
        """)
    elif computer_choice == "paper":
        print("""
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

        """)
    else:
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
                
        """)
    wins_computer = [computer_choice =="paper" and user_typed =="rock"], [computer_choice =="rock" and user_typed =="scissors"],[computer_choice=="scissors" and user_typed =="paper"]
    if len(computer_choice) == len(user_typed):
        print("THE RESULT IS: TIE")
    elif wins_computer:
        print("THE RESULT IS: YOU LOSE")
    else:
        print("THE RESULT IS: YOU WIN")

#V2
if False:
    import random
    print("Welcome to the rock, paper, scissors game.")
    user_typed = input("Press enter to continue or type (Help), for the rules. \n").lower()
    if user_typed == "help":
        print("""
    =====================================================
            ROCK, PAPER, SCISSORS — RULES
    =====================================================

    HOW TO PLAY:
    *Type ROCK, OR: PAPER, OR: SCISSORS, and press enter.
    *The computer will choose a random choice. 
    *The result will appear to show who is the winner, YOU OR THE COMPUTER?
    -----------------------------------------------------
                    THE THREE CHOICES
    -----------------------------------------------------

        ROCK                     PAPER                  SCISSORS
        _______                  _______                  _______
    ---'   ____)              ---'   ____)____         ---'   ____)____
        (_____)                       ______)                  ______)
        (_____)                       _______)              __________)
        (____)                       _______)              (____)
    ---.__(___)               ---.__________)          ---.__(___)

    -----------------------------------------------------
                    WHO WINS WHAT?
    -----------------------------------------------------

    [ ROCK ]     crushes   [ SCISSORS ]  -->  Rock wins!
    [ SCISSORS ] cuts      [ PAPER ]     -->  Scissors wins!
    [ PAPER ]    covers    [ ROCK ]      -->  Paper wins!

    * Same choice by both players? It's a TIE! Re-roll!

    =====================================================
    """)
    user_choice = input("Enter your choice. (rock, paper, scissors): \n").lower()
    right_choices = ["rock","paper","scissors"]
    if user_choice in right_choices:
        print("This is your choice:")
        if user_choice == "rock":
            print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
                
            """)
        elif user_choice == "paper":
            print("""
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

            """)
        elif user_choice =="scissors":
            print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
                
            """)
        computer_choice = random.choice(right_choices)
        print("This is the computer choice:")
        if computer_choice == "rock":
                print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
                
            """)
        elif computer_choice == "paper":
            print("""
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

            """)
        else:
            print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
                
            """)
        wins_computer = [computer_choice =="paper" and user_choice =="rock"], [computer_choice =="rock" and user_choice =="scissors"],[computer_choice=="scissors" and user_choice =="paper"]
        if len(computer_choice) == len(user_choice):
            print("THE RESULT IS: TIE")
        elif wins_computer:
            print("THE RESULT IS: YOU LOSE")
        else:
            print("THE RESULT IS: YOU WIN")
    else:
        print("You must choose: (rock) or (paper) or (scissors). You choose:",user_choice,"Try again")
    if user_typed:
        print(f"You must type (help) to reveal the rules. OR: press enter to skip the rules. You typed: {user_typed}")

#V3
if False:
    import random
    print("Welcome to the rock, paper, scissors game.")
    user_typed = input("Please press enter to continue or type (Help), to see the rules. \n").lower()
    if user_typed == "help":
        print("""

    =====================================================
            ROCK, PAPER, SCISSORS — RULES
    =====================================================

    HOW TO PLAY:
    *Type ROCK, OR: PAPER, OR: SCISSORS, and press enter.
    *The computer will choose a random choice. 
    *The result will appear to show who is the winner, YOU OR THE COMPUTER?
    -----------------------------------------------------
                    THE THREE CHOICES
    -----------------------------------------------------

        ROCK                     PAPER                  SCISSORS
        _______                  _______                  _______
    ---'   ____)              ---'   ____)____         ---'   ____)____
        (_____)                       ______)                  ______)
        (_____)                       _______)              __________)
        (____)                       _______)              (____)
    ---.__(___)               ---.__________)          ---.__(___)

    -----------------------------------------------------
                    WHO WINS WHAT?
    -----------------------------------------------------

    [ ROCK ]     crushes   [ SCISSORS ]  -->  Rock wins!
    [ SCISSORS ] cuts      [ PAPER ]     -->  Scissors wins!
    [ PAPER ]    covers    [ ROCK ]      -->  Paper wins!

    * Same choice by both players? It's a TIE! Re-roll!

    =====================================================
    """)

    elif user_typed:
        print(f"You must type (help) to reveal the rules. OR: press enter to skip the rules. You typed: {user_typed}", "NO problem. The game will start as if you pressed enter.")
    user_choice = input("Please enter your choice. (rock, paper, scissors): \n").lower()
    right_choices = "rock","paper","scissors"
    if user_choice in right_choices:
        if user_choice == "rock":
                print("""
            This is your choice:
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
                    
                """)

        elif user_choice == "paper":
                print("""

            This is your choice:    
            _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        
                """)
                
        else:
                print("""

            This is your choice:    
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
                    
                """)
            
    else:
        print("You must write: (rock) or (paper) or (scissors). You wrote:",user_choice, "Please restart the game")
    computer_choice = random.choice(right_choices)
    if computer_choice == "rock":
        print("""

        This is the computer choice:
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
                    
        """)

    elif computer_choice == "paper":
        print("""

        This is the computer choice:
            _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        
        """)
                
    else:
        print("""

        This is the computer choice:
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
                    
        """)
    computer_wins = [
        (computer_choice == "scissors" and user_choice == "paper") or
        (computer_choice == "paper" and user_choice == "rock") or
        (computer_choice == "rock" and user_choice == "scissors")
    ]
    tie = computer_choice == user_choice
    if any(computer_wins):
        print("THE RESULT IS: YOU LOSE")
    elif tie:
        print("THE RESULT IS: TIE")
    else:
        print("THE RESULT IS: YOU WIN!")

#V4
import random
print("Welcome to the rock, paper, scissors game.")
user_typed = input("Please press enter to continue or type (Help), to see the rules. \n").lower()
if user_typed == "help":
    print("""

=====================================================
          ROCK, PAPER, SCISSORS — RULES
=====================================================

  HOW TO PLAY:
  *Type ROCK, OR: PAPER, OR: SCISSORS, and press enter.
  *The computer will choose a random choice. 
  *The result will appear to show who is the winner, YOU OR THE COMPUTER?
-----------------------------------------------------
                 THE THREE CHOICES
-----------------------------------------------------

     ROCK                     PAPER                  SCISSORS
    _______                  _______                  _______
---'   ____)              ---'   ____)____         ---'   ____)____
      (_____)                       ______)                  ______)
      (_____)                       _______)              __________)
      (____)                       _______)              (____)
---.__(___)               ---.__________)          ---.__(___)

-----------------------------------------------------
                 WHO WINS WHAT?
-----------------------------------------------------

  [ ROCK ]     crushes   [ SCISSORS ]  -->  Rock wins!
  [ SCISSORS ] cuts      [ PAPER ]     -->  Scissors wins!
  [ PAPER ]    covers    [ ROCK ]      -->  Paper wins!

  * Same choice by both players? It's a TIE! Re-roll!

=====================================================
""")

elif user_typed:
    print(f"You must type (help) to reveal the rules. OR: press enter to skip the rules. You typed: {user_typed}", "NO problem. The game will start as if you pressed enter.")
user_choice = input("Please enter your choice. (rock, paper, scissors): \n").lower()
right_choices = "rock","paper","scissors"
if user_choice in right_choices:
    if user_choice == "rock":
            print("""
        This is your choice:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
                  
            """)

    elif user_choice == "paper":
            print("""

        This is your choice:    
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    
            """)
            
    else:
            print("""

        This is your choice:    
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
                  
            """)
          
else:
    print("You must write: (rock) or (paper) or (scissors). You wrote:",user_choice, "Please restart the game")
computer_choice = random.choice(right_choices)
if computer_choice == "rock":
    print("""

    This is the computer choice:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
                  
    """)

elif computer_choice == "paper":
    print("""

    This is the computer choice:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    
    """)
            
else:
    print("""

    This is the computer choice:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
                  
     """)
computer_wins = (
    (computer_choice == "scissors" and user_choice == "paper") or
    (computer_choice == "paper" and user_choice == "rock") or
    (computer_choice == "rock" and user_choice == "scissors")
)
tie = computer_choice == user_choice
if computer_wins:
    print("THE RESULT IS: YOU LOSE")
elif tie:
    print("THE RESULT IS: TIE")
else:
    print("THE RESULT IS: YOU WIN!")
