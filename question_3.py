# store the following word meaning in the python dictionary

things = {
    "tables" : ["a peice of furniture ","list of facts and figures"],
    "cat" : "a small animal"
}

print(things)

# WAP to find out how many classroom is required if each subject require one classroom

subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(subjects)
print("no. of classroom required : ",len(subjects))

# WAP to take input from user , marks of three subjects and store in dictionary

marks = {}

chem = int(input("enter chem marks :"))
marks.update({"chem" : chem})

phy = int(input("enter phy marks : "))
marks.update({"phy" : phy})

maths = int(input("enter maths marks : "))
marks.update({"maths" : maths})

print(marks)


