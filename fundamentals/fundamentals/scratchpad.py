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