#https://projecteuler.net/problem=1
sum=0
for i in range(1000):
    if i%5==0:
        sum=sum+i
    elif i%3==0:
        sum=sum+i
print(sum)