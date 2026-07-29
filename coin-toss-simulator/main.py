import random
print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █░█ █ █▀█ ▀█▀ █░█ ▄▀█ █░░   █▀▀ █▀█ █ █▄░█   ▀█▀ █▀█ █▀ █▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   ▀▄▀ █ █▀▄ ░█░ █▄█ █▀█ █▄▄   █▄▄ █▄█ █ █░▀█   ░█░ █▄█ ▄█ ▄█  
       
█▀▀ ▄▀█ █▀▄▀█ █▀▀
█▄█ █▀█ █░▀░█ ██▄ 
""")
input("Press ENTER to start")
random_number = random.randint(0,1)
if random_number == 0:
    print("The result is: HEADS!")
else:
    print("The result is: TAILS!")
