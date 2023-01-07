#!/usr/bin/python3
def uppercase(str):
    smp1 = ''
    for i in str:
        if(i >= 'a' and i <= 'z'):
            smp1 = smp1 + chr((ord(i) - 32))
        else:
            smp1 = smp1 + i
    return smp1
