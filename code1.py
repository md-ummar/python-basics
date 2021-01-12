uip = int(input("enter a number \n"))
# case1 
# if the number is 0 or  1 then it is neither prime nor composite
if uip == 0 or uip == 1:
     print("it is not prime")
#case 2: if the number is 2 then it is prime

elif uip  == 2 :
     print("it is prime")
 
#case 3:if the number is greater than 2

elif uip >=2 :
   for i in range(2,uip):
        if (uip%i) == 0:
            print("it is not a prime number")
            break 
   else:
        print("it is prime number")
else:
    print("it is not a prime number")
