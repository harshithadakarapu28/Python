"""Write a program that sums all odd numbers between i and j (inclusive)."""
n = list(map(int, input().split()))
i = int(input())
j = int(input())
capture = False
total = 0
for num in n:
    if num == i:
        capture = True
    if capture:
        if num%2 != 0:
            total += num
    if num == j:
        break
print(total)
