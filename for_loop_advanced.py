num=12345
sum=0
for i in range(len(str(num))):#lengthcan not accept integer so convert in to str
    temp=num%10#taking modulus
    num=num//10#abstracting last digits
    sum+=temp#adding each values to the previous value of sum
print(sum)