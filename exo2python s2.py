print( "donner un nombre intier ")
global x
x=input() 
def my_function():
    y=0
    a = (1, 2, 3, 4, 5)
    y =int(x)+int(sum(a))
    return y
result = my_function()
print(result)