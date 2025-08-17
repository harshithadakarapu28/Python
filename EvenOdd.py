
#COUNT EVEN AND ODD DIGITS IN A GIVEN STRING
def even_odd(n):
     even_num = 0
     odd_num = 0
     while (n>= 1):
         last = n% 10
         if last  % 2 == 0:
             even_num += 1
        else:
             odd_num += 1
         n = n // 10
     return even_num,odd_num
 n = int(input())
 print(even_odd(n)) 
