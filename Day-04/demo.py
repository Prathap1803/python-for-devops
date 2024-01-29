import demo2
opt = int(input("Choose the below \n 1.Add \n 2.sub \n"))
num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))

def add(a,b):
    sum = a+b
    print (sum)
def sub(a,b):
    sub = a-b
    print(sub)
if (opt==1):
    add(num1,num2)
elif(opt==2):
    sub(num1,num2)
elif(opt==3):
    demo2.mul(num1,num2)

