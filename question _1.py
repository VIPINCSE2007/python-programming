#wap to input 3 movies into a list

# meathod 1   (enter every movie one by one in different variable)

movies = []          #empty list
mov1 = input("enter 1st movie :")
mov2 = input("enter 2nd movie :")
mov3 = input("enter 3rd movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# meathod 2   (enter movies in same variable)
mov = input("enter 1st movie :")
movies.append(mov)
mov = input("enter 2nd movie :")
movies.append(mov)
mov = input("enter 3rd movie :")
movies.append(mov)

print(movies)

# meathod 3   (append and input in same line)

movies.append(input("enter first movie :"))
movies.append(input("enter second movie :"))
movies.append(input("enter third movie :"))

print(movies)

