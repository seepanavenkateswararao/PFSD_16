import pytest
def sumOfNaturalNumbers(n):
    sum=0
    if n<0:
        return 0
    else:
        for i in range(0,n+1):
            sum=sum+i
    return sum
def factorial(n):
    sum=0
    if n<0:
        return sum
    else:
        for i in range(0,n+1):
            sum=sum*i
    return sum
def factor(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt++
    return cnt
def test():
    assert sumOfNaturalNumbers(10)==55
    # assert factorial(5)==120
    # assert factor(4)==3