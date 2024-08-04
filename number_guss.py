import random
import time

print("-"*20)

user_range = int(input("Enter your range : "))
num = random.randint(1,user_range)
time.sleep(1)

#design
print("-"*20)
print()
print("-"*20)

print("1 > 1 times")
print("2 > 3 times")
print("3 > infinity times")
user = int(input("How many times :: "))
time.sleep(1)

#design
print("-"*20)
print()
print("-"*20)

#1 times
if user == 1:
    #now guss the number
    user_guss = int(input("Guss the num : "))
    
    if user_guss == num:
        print(":) - Your Win!.... - :)")
    else:
        print(":) - Game Over")

# 3 times
elif user == 2:
    for times in range(1,3+1):
        if times == 1:
            print(f"{times} Guss the num : ",end="")
        else:
            print(f"{times} Times Left : ",end="")
        user_guss = int(input())
        
        if user_guss == num:
            print()
            print("-"*20)
            time.sleep(1)
            print(":) - Your Win!.... - :)")
            print("-"*20)
            print()
            break
        else:
            if times == 1 or times == 2:
                print()
                print(":) - Try .")
            else:
                print()
                print(":( - Game Over")

#infinat times
elif user == 3:
    times = 1
    while True:
        if times == 1:
            print(f"{times} Guss the num : ",end="")
        else:
            print(f"{times} Times Left : ",end="")
        user_guss = int(input())
        
        if user_guss == num:
            print()
            print("-"*20)
            time.sleep(1)
            print(":) - Your Win!.... - :)")
            print("-"*20)
            print()
            break
        else:
            print()
            print(":) - Try..")
            
        times += 1