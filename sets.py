# set is collection of unordered items (when we print any element can appear anywhere in the set)
# each element in sets is unique and unmutable (eg int ,float , boolean string tuple ) (list and dictionary cant be stored in sets as they are mutable)

nums = {1,2,3,4,5,6}
marks = {1,2,2,2}           # this will be seen as set = {1,2}

#repeated elements are stored only once

collection = {1,2,2,3,3,4,5,"hello wrold","world", "world"}

print(collection)
print(type(collection))

empty_dict = {}            # empty dictionary
empty_set = set()          # empty set

# set are mutable but its elements are immutable
sets = set()
sets.add(0)
sets.add(1)
sets.add(2)
sets.add(2)   # duplicate value is considered once
sets.add(4)
print(sets)

sets.remove(2)
print(sets)
sets.remove(1)   # error if the element doesnt exist
print(sets)

sets.add("vipin")       # can add strings 
sets.add((1,2,3,4))     # can add tuple
print(sets)
marks.clear()           # delete all values , make the sets empty
print(len(marks))       # output will be zero

cars = {"bmw","bugatti","mercedes","alto"}
print(cars.pop())          # randomly pop out any random element
print(cars)

# union and intersection in sets
set1 = {0,1,2,3}
set2 = {1,2,3,4}
print(set1.union(set2))             # find the union of the sets
print(set1.intersection(set2))      # find the intersection of the sets 



