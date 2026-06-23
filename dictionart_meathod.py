info = {
    "name" : "vipin",
    "age" : 19,
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 92
    }
}
print(info["subject"]["chem"])   #fetching out a specific detail info --> subject --> chem


# 1) dict.keys()
print(info.keys())
print(list(info.keys()))
print(len(list(info.keys())))    #info.keys() --> all keys
                                 #list(info.keys()) --> type cast into list
                                 #len(list(info.keys())) --> total elements in the list

# 2) dict.value()
print(info.values())
print(list(info.values()))

# 3) dict.items()
print(info.items())
print(list(info.items()))

#4) to print value of any key
print(info["name"])           #print the value , if something is wrong then it will show error
print(info.get("name"))        #if the variable doesnt exist or it show some error the it will return none , this meathod of fetching data is considered good

#5) student.update(new_dict)
new_dict = {"name" : "rahul" , "age" : 16}
info.update(new_dict)               #used to update the current dictionary
print(info)