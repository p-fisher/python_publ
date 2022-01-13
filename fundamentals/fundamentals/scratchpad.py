count = 0
while count <= 5:
    print("looping - ", count)
    count += 1



x = [5,34,10,1,6]
# x.append(2)
x+=[2]
print(x)


x= [3,11,6,9,10]
print(x[1])



def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")   # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)   # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)   # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

