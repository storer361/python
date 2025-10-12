number =int(input("enter the number :"))
n =int(input("enter how many powers you want to calculate  :"))
print(f"\npowers of {number} are:")
for i in range (1,n+1):
    power_value=number**i
    print(f"{number}^{i}={power_value}")
    