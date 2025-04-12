def divide(divisor,dividend):
    sign=(-1 if(dividend<0)^(divisor<0)else 1)
    dividend,divisor=abs(dividend),abs(divisor)
    quotient=0
    temp=0

    for i in range(31, -1, -1):
        temp=divisor<<i
        quotient|=1<<i

    if sign==-1:
        quotient=-quotient
    return quotient

a=int(input("enter a for a/b: "))
b=int(input("enter b for a/b: "))
print("results of ",a,"/",b,"is", divide(a,b))