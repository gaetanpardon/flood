# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:43:16 2016

@author: pardon
"""

from numpy import exp
import matplotlib.pyplot as plt 
def fontcarr (x):
    return(x**2 -2)
def dcar (x):
    return( 2*x )

def dichotomie (a,b,f,e):
    assert e>0 and f(a)*f(b)<0
    d=a
    g=b
    while ((f(d) - f(g)) < -e )or( ((f(d) - f(g) ) > e) ):
        m=(d+g)/2
        print(m)
        if f(d)*f(m)< 0 :
            g=m
        else :
            d=m
    return(d+g/2)

dichotomie(1,2,fontcarr, 0.001)
            
def newton (x,f,df,e):
    r=x
    while (f(r) < -e )or( f(r) > e) :
        d = f(r)/ (df(r)) 
        r = r
        #print(r)
    return(r)
    
newton(10,fontcarr,dcar,0.000001)

def sho(x) :
    return(x-0.01*(10**-12/0.0468))
def dsho (x) :
    return(1+1.2*(10**-12)**exp((5-(x*120))/0.0468))
    
X=[]
Y=[]    
for i in range(1000):
    X=X+[i/1]
    Y=Y+[sho(X[i])]
plt.figure()
plt.plot(X,Y)
plt.ylabel('0')
plt.xlabel("I")
plt.show()
print("\r \r \r")
s=newton(0.1,sho,dsho,0.00000001)
print("\r \r \r f(i)=",sho(s),"\r \r \r i=",s,"A")