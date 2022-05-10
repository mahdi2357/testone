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

# create a function that takes a string and returns a string with the first and last characters swapped
def swap_first_last_characters(word):
    return word[-1] + word[1:-1] + word[0]
    