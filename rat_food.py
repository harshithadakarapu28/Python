def calculate (r, unit, arr,n):
    if arr is None or n == 0:
        return -1
    totalFood = r * unit
    FoodNow = 0

    for house in range(n):
        FoodNow += arr[house]
        if FoodNow >= totalFood:
            return house+1
        
    return 0
# Input handling
r = int(input("enter the nimber of rats:"))
unit  = int(input("enter the value of units:"))
n = int(input("Enter the number of elements in a array:")) 
arr = list(map(int, input("enter the list elements:").split()))


print(calculate(r, unit, arr, n))
           