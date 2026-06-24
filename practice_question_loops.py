# print numbers from 1 to 100
i = 1
while i<=100:
    print(i)
    i+=1
print("!------loop ended-------!")

# print numbers from 100 to 1

j = 100
while j>=1:
    print(j)
    j-=1

# print multiplication of table of n

n = int(input("table of "))
i = 1
while i<=10:
    print(n*i)
    i+=1

# print numbers in list using loop
#[1,4,9,16,25,36,49,64,81,100]

list = []
i = 1
while i<=10:
    list.append(i*i)
    i+=1
print(list)


# print the numbers from list
list1 = []
number = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < 10 :
    print(number[index])
    

    list1.append(number[index])
    print(list1)
    index += 1


# search for a given number from a list
list2 = [1,4,9,16,25,36,49,64,25,81,100]
x = 25
m = 0
while m < len(list2):
    if(list2[m] ==x):
        print("number found at index",m)
    else:
        print("searching ......")
    m+=1