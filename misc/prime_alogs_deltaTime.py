"""
Created By : Al-Banna-Techno
"""
import math
import datetime

"""
this solution created to compare two method of
checking prime numbers

This Solution is very bad to use with mathematical applications
because decorator use large amount size of ram-cpu
and also make gui application heavy if
decorators controlled on shader(vertex or fragment)

but you can use isPrimeNum_1|2  function
without using check_time deco-func
into your application to reduce cpu-usage

"""
def check_time(func):
    """ABT-Doc: Warn : This Function must use only with decorator
    From Level 2 "deco has parameter "
    """
    def dos(pars):
        a = datetime.datetime.now()
        func(pars)
        b = datetime.datetime.now()
        tim = b - a
        print(tim)
    return dos

"The Best"
def isPrimeNum_1(num):
    loop=0
    if num==2:return False,loop
    loop+=1
    if num<2 or num %2==0:return False,loop
    loop += 1
    # print("After Start")
    var=math.sqrt(num)
    loop += 1
    var=int(var+1)
    loop += 1
    for a in range(3,var,2):
       loop += 1
       if num%a==0:
           return False,loop
    return True,loop
def isPrimeNum_2(num):
    loop=0
    if num==2:return True,loop
    loop+=1
    if num < 2 or num % 2 == 0: return False,loop
    loop += 1
    # print("After Start")
    b=3
    loop += 1
    for a in range(b,num,2):
        loop += 1
        if num%b==0:
            return False,loop
    return True,loop


@check_time
def f1(sd):
    print("IP1 : ")
    print(isPrimeNum_1(sd))
@check_time
def f2(sd):
    print("IP2 : ")
    print(isPrimeNum_2(sd))

def ff(val):
    f1(val)
    f2(val)

"wiki https://en.wikipedia.org/wiki/List_of_prime_numbers"
ff(16769023)
