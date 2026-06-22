# in a dictionary we store data in akey value pair  "key": value

dict = {
    "name" : "vipin",
    "age" : 19,
    "marks" : [90,92,94,85],
    21 : 19,               #key can be integer
     (21,25) : "marks"     #key can be tuple
}

dict["name"] = "apnacollege"   #we can change the value of any key
dict["surname"] = "bisht"      # add another key value pair in dictionary
print(dict)

null_dict = {}                      # empty dictionary
null_dict["name"] = "vipin"         #add value in empty dictionary
print(null_dict)