#Write a program to calculate the sum of all elements in the list starting from the first occurrence of i to the first occurrence of j (inclusive).
n = list(map(int, input().split()))
i = int(input())
j = int(input())
capture = False
total = 0
for num in n:
    if num == i:
        capture  = True
    if capture:
        total += num
    if num == j:
        break
print(total)