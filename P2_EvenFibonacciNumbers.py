#https://projecteuler.net/problem=2
fib=[]
fib.append(int(1))
fib.append(int(2))
sum=0
while fib[len(fib)-1]<4000000:
    fib.append(int(fib[len(fib)-1])+int(fib[len(fib)-2]))
fib.pop(len(fib)-1)
for i in range(len(fib)):
    if fib[i]%2==0:
        sum=sum+fib[i]
print(sum)