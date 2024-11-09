#cars=["chevrolet","supra","dodge"]
#print(cars)
#cars_in_gar= cars
#cars.pop(cars_in_gar)
#print(cars)
#print(f"the cars in my garage are {cars_in_gar}")
#for this code the error is 'list' object cannot be interpreted as an integer

cars=['chevrolet','supra','dodge']
print(cars)
print(cars[0])
print(cars[1].title())
print(cars[-1].title())
msg=f"the car i fell in love with the first look is '{cars[-1]}'."
print(msg)

#to modify
print(cars)
cars[0]="lotus"
print(cars)

#to add
cars.append('cooper')
print(cars)

#inserting
cars.insert(2,'jaguar')
print(cars)

#deleting
del cars[-1]
print(cars)

#poping makes it better to use the values thats going to be removed
poped_car=cars.pop(3)
print(cars)
print(poped_car)
print(f"the first car i wish to buy is '{poped_car.title()}'.")

#removing by value and the val that is removed my "remove" can be used.
jag = 'supra'
cars.remove(jag)
print(cars)
print(f"the second car i wish to buy is '{jag.title()}'.")
#we can use the fstring in lists
#cars_in_gar= cars
#cars.pop(cars_in_gar)
#print(cars)
#print(f"the cars in my garage are {cars_in_gar}")