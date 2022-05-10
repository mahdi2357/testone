# Create fibonachi function
def fibonachi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#Create hello function
def hello():
    print("Hello World")

print(fibonachi(10))
hello()
