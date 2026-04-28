a = []
i = 0
b =  1
while i < 100 :
    a.append(b)
    b += 1
    i += 1

x =     51                             # computer choose the number.
print(x)
p = 1
c = 0 
while p == 1 :
    y = int(input("Enter the number : "))
    if(y < x) :
        print("",y,"is too small")
        print("Enter big number")
        c += 1
    elif(y > x) :
        print("",y,"is too big")
        print("Enter smaller number")
        c += 1
    elif(y == x) :
        print("your guess is correct : ",x)  
        c += 1
        break  
        p += 1
    else :
        print("Invalid Input")

print("Final Answer")
print("you guess the answer : ",c,"times")
















