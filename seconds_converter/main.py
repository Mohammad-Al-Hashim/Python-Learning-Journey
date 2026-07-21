total_seconds=int(input("Please enter the total number of seconds \n"))
hours=total_seconds//3600
minutes=total_seconds%3600//60
remaining_seconds=total_seconds%60 
print(f"It is: {hours} hours, and: {minutes} minutes, and: {remaining_seconds} remaining seconds.")
