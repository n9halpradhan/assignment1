n=int(input("Enter two digit number: "))
test=0 
while(n>0):
  rem=n%10
  test=(test*10)+rem
  n=n//10
print("The reverse number is : {}".format(test))