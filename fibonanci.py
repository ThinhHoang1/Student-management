def fibonaci(n):
    if n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
num = int(input("Enter num: "))
print("The first", num,"Fibonanci is: ")
for i in range(1,num+1):
    a = fibonaci(i)
    print(a,end=" ")
