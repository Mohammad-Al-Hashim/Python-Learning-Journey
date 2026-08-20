done_tasks = []
ongoing_tasks = []
task_list = input("Please type the names of the tasks separated by a comma: \n").split(", ")
for one_task in task_list:
    print("\n",one_task,"\n")
    finished = input(f"Did you finish {one_task} today? Type yes or no \n").lower()
    if finished in ["yes","no"]:
        if finished == "yes":
            print("Nice job!")
            done_tasks.append(one_task)
        else:
            print("Try not to put it off")
            ongoing_tasks.append(one_task)
    else:
        print("You must type either yes or no. You typed:",finished,"Try again")
        break
progress = input("Do you want to see your today's progress? Type yes or no \n")
if progress in ["yes","no"]:
    if progress == "no":
        print("OK, Have a nice day")
    else:
        print(f"------------Done tasks--------------\n{done_tasks}")
        print("\n\n")
        print(f"------------Ongoing tasks--------------\n{ongoing_tasks}")
else:
    print("You must type either yes or no. You typed:",progress,"Try again")
