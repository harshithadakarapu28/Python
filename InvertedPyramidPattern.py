""" Inverted Pyramid Pattern in Python"""
 n = int(input())
 for i in range(n, 0 , -1):
     for j in range(n-i):
         print(" ", end = " ")
     for k in range(1, i*2):
         print("*", end = " ")
     print()
