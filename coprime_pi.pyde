from random import *
import math

cop=0
cof=0

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def setup():
    size(400,400)
    background(0)
    
def draw():
    global cop, cof
    K=0
    a=randint(1,width)
    b=randint(1,height)
    
    strokeWeight(3)
    noFill()
    if gcd(a,b)==1:
        cop+=1.
        stroke(255,0,0)
        point(a,b)
    else:
        cof+=1.
        stroke(255)
        point(a,b)
    
    pr=cop/(cop+cof)
    pi=math.sqrt(6/pr)
    print(pi)


        
    
