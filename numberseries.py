n = int(input("Enter the nth value: "))
a = 0
b = 1
sum = 0
print("Fibonacci Series : ")
while(sum <= n):
     print(sum)
     a = b
     b = sum
     sum = a + b         
            
