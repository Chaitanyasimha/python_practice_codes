#que_10. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input
#through the keyboard in hundreds, find the total number of currency notes of each denomination the
#cashier will have to give to the withdrawer.

#ANS:
cash = eval(input("please enter amount in hundreds :"))
i = 0
j = 0
k = 0
while (cash%100 == 0):
    cash = cash - 100
    i = i+1
    print(cash)
    print(i)
    if cash == 0:
        break
while (cash%50 == 0):
    cash = cash - 50
    j = j+1
    if cash == 0:
        break
while (cash%10 == 0):
    cash = cash - 10
    k = k+1
    if cash == 0:
        break
if i > 0:
    print(f"you get {i} no of 100 notes")
if j > 0:
    print(f"you get {j} no of 50 notes")
if k > 0:
    print(f"you get {k} no of 10 notes")
print(cash)
print(i)