#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# prediction: 5 is printed
# reality: confirmed

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# prediction: 5 is printed; undefined function ignored
# reality: incorrect! undefined function threw an error, stopping the success

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# prediction: 5 will be printed; 10 will be ignored because the first command succeeded
# reality: confirmed


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# prediction: answer will be 5 because the return ends the function... 10 never prints
# reality: confirmed

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# prediction: 5 prints
# reality: partially correct; 5 printed and None on next line. Why?


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# prediction: it never "sums" b,c; it only prints. yes, "numbers" are being passed in argument but they are printed as strings, me thinks. i am thinking it prints "1223" 
# reality: printed 3 and 5 on two lines while also generating an error (operand type for +)


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# prediction:  converts integers to strings, concatenates printing "25"
# reality: confirmed


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# prediction: prints 100, then evluates and returns 10 and ends ("return 7" line never executes); 10 also prints because of funtion call in print
# reality: confirmed; prints 100\n10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# prediction: 7\n14\n21; return 3 never occurs because previous return
# reality: confirmed


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# prediction: returns 8, prints 8; return 10 never occurs
# reality: confirmed


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# prediction: 500\n300\n300\n300\n300
# reality: incorrect; printed 500 500 300 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# prediction: 500\n300\n300\n300
# reality: incorrect; printed 500 500 300 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# prediction: 500\n500\n300\n500
# reality: NameError (name 'b' is not defined)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# prediction: 1\n3\n2
# reality: confirmed


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# prediction: 1\n3\n (10 and 5 returned but do nothing)
# reality: incorrect; 1 3 5 10 printed. Why?
