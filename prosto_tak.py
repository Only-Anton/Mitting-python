
def Summ(a):
    sum = 0
    for n in range(1, a//2 +1):
        if a % n == 0:
            sum += n
    return sum
"""
for i in range(1, 100000):
    sum = Summ(i)
    if i == sum:
        print(i, sum)
"""
arr = [1,5,3,6,7,4,9,6]
"""
n = int(input('Enter the number: '))
arr_m = [i for i in arr[:] if i <= n]
arr_b = [i for i in arr[:] if i > n]
print("Littler: ", arr_m)
print('More: ', arr_b)

i = 1
#print(arr[i], len(arr))
while i < len(arr):
    if arr[i] < arr[i-1]:
        arr[i] = arr[i] + arr[i-1]
        arr[i-1] = arr[i] - arr[i-1]
        arr[i] = arr[i] - arr[i-1]
        print(arr)
        if i > 1: 
            i -= 1
    else: i += 1
"""
#print(arr)
def simpl(n):
    numb = 2**n - 1
    for i in range(2, numb//2+2):
        if numb % i == 0:
            return False
    return True
n = int(input("Enter numb: "))
# print(simpl(n))
k = 0
for i in range(2, n):
    if simpl(i):
        numb = 2**(i - 1) * (2**i - 1)
        k += 1
        print(k, i, numb, Summ(numb))
