"""Question: Triple Machine Sync – Real-Time Alert System
In an industrial automation setup, three different machines are programmed to emit alert beeps at regular intervals:
Machine A beeps every a seconds.
Machine B beeps every b seconds.
Machine C beeps every c seconds.
All machines start beeping simultaneously at time t = 0.
As a system engineer, your task is to:
Determine the first time after 0 when all three machines will beep together again.
Given a total observation period of n seconds, determine how many times all three machines will beep together within that time frame."""
def HCF(a,b):
    hcf = 1
    for i in range(2, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            hcf = i
    return hcf
def LCM(a,b):
    return(int(a*b)//HCF(a, b))
def HcfThree(a,b,c):
    return HCF(HCF(a,b),c)
def LcmThree(a,b,c):
    return LCM(LCM(a,b),c)
def beep(a,b,c,n):
    return(int(n//LcmThree(a,b,c)))
a,b,c,n= map(int, input().split())
print(beep(a,b,c,n))
