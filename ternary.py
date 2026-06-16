#ternary operator using variable
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

#ternary operator without using variable
foods = input("foods : ")
print("sweet") if foods == "cake" or foods == "jalebi" else print("not sweet")