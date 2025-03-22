# Description: This program solves a system of simultaneous congruences

n=int(input("Enter number of congruences:"))

#Initialize the lists

remainder=[]
modulus=[]

#Input the congruences

for i in range (0,n,1):
    remainder.append(int(input("Enter remainder:")))
    modulus.append(int(input("Enter modulus:")))

#Finding value of modulus of the result

p=1

for i in range (0,n,1):
    p=p*modulus[i]

#Define the function of the system of congruences

def func(a):
    z=0
    for j in range(0,n,1):
        if (a-remainder[j])%(modulus[j])==0:
            z+=1
        else:
            break
    if z==n:
        print("The solution is ",a,"mod(",p,")")
        return True
    return False

#Finding the solution by brute force

for i in range(0,p,1):
    if func(i):
        break