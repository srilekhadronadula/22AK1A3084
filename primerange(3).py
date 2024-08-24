def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def print_primes(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num,end=" ")
start=int(input('enter the start of the range:'))
end=int(input('enter the ending range'))
print('primes numbers in the range are:')
print_primes(start,end)
