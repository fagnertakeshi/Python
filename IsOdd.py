
import math
import os
import random
import re
import sys

def isodd(num):
    if num%2 != 0:
        return True
    else:
        return False

n = 10

if isodd(n):
    print('Weird')
else:
    if n>=2 and n<=5:
        print('Not Weird')
    if n>=6 and n<=20:
        print('Weird')
    if n>20:
        print('Not Weird')