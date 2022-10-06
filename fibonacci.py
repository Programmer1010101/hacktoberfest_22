'''Find Fibonnaci series'''

term=int(input("Enter the no. of terms : "))
n1,n2=0,1
count=0
if term<=0:
    print("Invalid no.Enter a positive value")
elif term==1:
    print("The Fibonacci series upto",term,":")
    print(n1)
else:
    print("The Fibonacci series upto",term,":")
    while count<term:
        print(n1,end='  ')
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1