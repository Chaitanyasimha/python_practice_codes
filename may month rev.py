#1 module book



#hello_world
hello_world= "python world"
print(f"hi and welcome to {hello_world}")

#2 module book



#casing tests andsteips
name = " chaitanya simha "
print(f"the nametitle = {name.title()}, uppercase = {name.upper()}, lowercase = {name.lower()}, strip = k{name.strip()}d, lstrip  = k{name.lstrip()}, rstrip = {name.rstrip()}d")
#famous quote
msg1 = "itam chet tvam imam dramyam sangramam na karishyasi"
msg2 = "tataha sva darmam kirtim cha hitva papam avapsyasi"
krishnas_msg = f'\n\nKrishna said to Arjuna,"{msg1}\n\t\t\t{msg2}."\n\n'
print(krishnas_msg)
#removal of prefix and suffix
web1="www.dheergadu.com"
file1="extention.net"
print(file1.removesuffix(".net"),web1.removeprefix("www."))
#numbers operations to print num 8
print(1+7)
print(9-1)
print(2*4)
print(16/2)
print(2**3)
#fav number
fav_num = 9
print(f"\nmy fav num is {fav_num}\n")
import this
#printing friends names one by one from a list
frds_names = ["ravie","bhairava","silver","hatie","chaitu"]
#way 1
print("\n\t\tWAY 1\n")
print(frds_names[0].title())
print(frds_names[1].title())
print(frds_names[2].title())
print(frds_names[3].title())
print(frds_names[4].title())
print("\t\tWAY 2")
print(f"\n{frds_names[0].title()}\n{frds_names[1].title()}\n{frds_names[2].title()}\n{frds_names[3].title()}\n{frds_names[4].title()}")

#3 module book



#guest list
dinner_inv = ["ravie","bhairava","silver","hatie","chaitu"]
for guests in dinner_inv:
    print(f"\ndear guest {guests} you have been invited to the banquet")
print(f"\nit is our heartfelt sorrow that mr'{dinner_inv[1].title()} cannot attend to the baquet")
dinner_inv[1] = "tom riddle"
for guests in dinner_inv:
    print(f"\ndear guest {guests} you are  invited to the banquet")
print("\nguys we found a bigger table")
dinner_inv.insert(0,"potter")
dinner_inv.insert(-3,"weasley")
dinner_inv.append("granger")
print(dinner_inv)
for guests in dinner_inv:
    print(f"\n{guests} you are invited to the banquet ")
print("\nsorry guys we are sorry that we can only invite two members to the banquet")

"""

dinner_inv.pop(0)
print(f"\nsorry {dinner_inv.pop(1)} we cannot invite you")
dinner_inv.pop(1)
print(f"\nsorry {dinner_inv.pop(2)} we cannot invite you")
dinner_inv.pop(2)
print(f"\nsorry {dinner_inv.pop(-1)} we cannot invite you")
print(dinner_inv)
for guests in dinner_inv:
    print(f"\n{guests} you are invited to the banquet ")
    
    
if this removal is done like this the removal of items in the list is done 6 times
first at the dinner_inv.pop then again in the print statement"""

print(f"\nsorry {dinner_inv.pop(0)} we cannot invite you")
print(f"\nsorry {dinner_inv.pop(1)} we cannot invite you")
print(f"\nsorry {dinner_inv.pop(-2)} we cannot invite you")
print(f"\nsorry {dinner_inv.pop(-1)} we cannot invite you")
print(dinner_inv)
for guests in dinner_inv:
    print(f"\n{guests} you are invited to the banquet ")
print(dinner_inv)
del dinner_inv[0]
del dinner_inv[0]
del dinner_inv[0]
del dinner_inv[0]
print(dinner_inv)
print("\nthe dinner list is empty now\n")

#organising a list

visit_places = ["japan","swiss","canada","singapore","london"]
print("the orginal list is this :")
print(visit_places)
print("\nthe sortedd list is this :")
print(sorted(visit_places))
print("\nthe orginal list has not been updated :")
print(visit_places)
print("\nthe reveresed list is this :")
print(sorted(visit_places,reverse = True))
print("\nthe orginal list has not been updated :")
print(visit_places)
print("\nthe orginal list has perminantly reversed :")
visit_places.reverse()
print(visit_places)
print("\nthe orginal list is reveresed and back to normal :")
visit_places.reverse()
print(visit_places)
print("\nthe alphabetical sorted list :")
visit_places.sort()
print(visit_places)
print("\nthe orginal list has been reversed using the sort function :")
visit_places.sort(reverse=True)
print(visit_places)

#using len function in the guests list
print(f"{len(dinner_inv)} members has been invited to the party")


"""   

we have now know that for functions like len,sorted wants the variable to be inserted in them not limke .len() or .sorted()

"""

#trying to make an index error
#print(visit_places[5]) this makes a list out of range error

#working with lists or using for loops efficiently in lists

pizzas = ["african perperi","cheese burst","bell peppers","olives"]
print("\nthe provided pizzas are :")
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"{pizza} is one of my favortie pizzas")
print(f"\nthe kind of pizzas i like are {pizzas[0].title()}, {pizzas[1].title()}, {pizzas[2].title()}, and {pizzas[3].title()}" )
print("'i really love pizzas so much'")

animals = ["lynx","panther","lion","tiger"]
print("\nthe bigcats in the wild are :")
for bigcats in animals:
    print(bigcats)
    print(f'"{bigcats}" would make a great hunter in the wild')
print("\nAll these animals are bigcats of the jungle\n")

#making a list of numbersusing for loop
##this is short cut for that of cource "way1"
print("\t\t\tway1\n")
numbers_1 = list(range(1,21))
print(numbers_1)

print("\n\t\t\tway2\n")
numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers)

#printing million numbers and inserting them in list
million = list(range(1,1001))
for nums in million:
    print(nums)
print(min(million),max(million),sum(million))

#printing odd numbers using 3rd argument of a for loop
odd_nums = list(range(1,21,2))
print(odd_nums)

#multiples of three
mul_of_3 = []
for nums in range(1,11):
    mul_of_3.append(nums*3)
print("\nthe multiples of 3 are :")
print(mul_of_3)

""" if you want another code for the same implementation you can write 

mul_of_3 = []
for nums in range(1,11):
    num_3 = nums*3
    mul_of_3.append(num_3)
print("\nthe multiples of 3 are :")
print(mul_of_3) 
"""
    
#making cube lists
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print("\nthe cubes of 1 to 10 :")
print(cubes)

##using list comprehensions to form a list of numbers

cube_comp = [values**3 for values in range(1,11)]
print("\nthe list comrehension used for cubes :")
print(cubes)

#playing with list comprehensions
print("\nthe list comrehension used for pizzas :")
l_comp1 = [pizza.title() for pizza in pizzas]
print(l_comp1)


## 4 MODULE BOOK ##

