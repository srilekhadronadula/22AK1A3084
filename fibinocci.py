a=int(input("enter the number"))
n=2
fib=0
f1=1
f2=1
while(fib<a):
    fib=f1+f2
    f1=f2
    f2=fib
    n+=1
if(fib==a):
    print('fib')
    print('the position of the fibinoci number is:',n)
else:
    print('not a fib')