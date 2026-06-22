# check whether a list is a palindrome or not
# palindrome which looks exactly same when reverse it

list = []
list.append(input("enter number:"))
list.append(input("enter number :"))
list.append(input("enter number :"))
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("it is a palindrome")
else:
    print("not a palindrome")