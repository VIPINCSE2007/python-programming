#creating a nested dictionary

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