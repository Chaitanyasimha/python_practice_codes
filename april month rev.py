#using f strings and casing of letters
person="eric"
print(f'"Hello {person.title()},would you like learn some python today?".')
print(person.upper())
print(person.lower())
print(person.title())

fam_p = "albert einstein"
print(f'{fam_p.title()} once said,"a person who never made a mistake never tried anything new."')
#the white space theory both romving and using them 
var="\tdheeraj\t"
var1="\n\tsimha\n\tdheeraj\n\tkarthik"
print(var,var1)
print()
print(var.strip())
print(var.lstrip())
print(var.rstrip())
#prefix and suffix removal
web1="www.jinka_bomma.com"
print(web1.removeprefix("www."))
web2="bule_bomma.html"
print(web2.removesuffix(".html"))
#number theory
print(3+5)
print(10-2)
print(16/2)
print(4*2)
fav_n = 8
print(f'my fav number is"{fav_n}".')
#the zen of python
import this
#lists accesing and using f strings with them
names = ["harish","bharath","deva","hemanth","aki","garf","sudheer"]
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])
mes = f"wanna do some gaming buddy."
print(f'yo "{names[0].title()}" {mes}')
print(f'yo "{names[2].title()}" {mes}')
print(f'yo "{names[5].title()}" {mes}')
#editting a list
guests = ["sudheer","garf","harish"]
msg="you are welcome to the dinner"
print(f'yo "{guests[0].title()}" {msg}')
print(f'yo "{guests[1].title()}" {msg}')
print(f'yo "{guests[2].title()}" {msg}')
buz_g = guests.pop(2)
print(len(guests))
print(f'yo "{guests[0].title()}" {msg}')
print(f'yo "{guests[1].title()}" {msg}')
guests.insert(3,"hachu")
print(f'yo "{guests[2].title()}" {msg}')
print(f"the one who cannot come to the party is {buz_g.title()}")
guests.insert(0,"sreenu")
guests.insert(3,"otto")
guests.append("vikranth")
print(f'yo "{guests[0].title()}" {msg}')
print(f'yo "{guests[1].title()}" {msg}')
print(f'yo "{guests[2].title()}" {msg}')
print(f'yo "{guests[3].title()}" {msg}')
print(f'yo "{guests[4].title()}" {msg}')
print(f'yo "{guests[5].title()}" {msg}')
print(f"{guests[0].title()},{guests[1].title()},{guests[2].title()},{guests[3].title()},{guests[4].title()},{guests[5].title()} we found a big dining table")
print("guys we can only invite two people for dinner")
l=6
for l in range(0,4):
    gp=guests.pop()
    print(f"'{gp.title()}' ,sorry we can't invite you to the dinner")
print(f"{guests[0].title()} you are still welcome")
print(f"{guests[1].title()} you are still welcome")
del guests[1]
del guests[0]
print(guests)
