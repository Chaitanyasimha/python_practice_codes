###module 4 book###

cars = ['mesarati','benz','bently','porshe','chevrolet']
sli_cars = cars[0:4]
print(sli_cars)
#if i want to use a tuple with one element i have to use the trailing ,
car = ('porshe',)
print(car[0])
#you cant change but can re define the tuples
buffet_items = ('cheese burger','sandwiches','pizza','natchos','french fries')
print("the items at this buffet are :")
for items in buffet_items:
    print(items)
#buffet_items[0] = 'noodles' to make an error to show that tuples dojnt allow the modification of the tuples
#rewriting the tuple
buffet_items = ('macroni','pancakes','pizza','natchos','french fries')
print("the items at this buffet are :")
for items in buffet_items:
    print(items)
#conditional tests
#(predictions of tests)
friends = ["dheeraj","karthik","dheeraj","rathi","devi","eswar","raju","simha","rujith","garfiel"]
if friends[0] == "dheeraj":
    print("true")
else :
    print("false") 


#using the "is" and "?" and "i predict true" fucction and keywords
print("Is friends[0] == 'sudheer'? i predict True.")