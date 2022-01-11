# exc 1 basic - print all integers from 1 to 150
for x in range(0,151):
    print(x)

# exc 2 mult of five - print mutiples of 5 from 5 to 1000
for x in range(5,1001,5):
    print(x)

# exc 3 counting dojo way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
int = 1
while int < 100:
    int += 1
    if int % 10 == 0:
        print("Coding Dojo")
    elif int % 5 == 0:
        print("Coding")
    else:
        print(int)

# exc 4 huge - Add odd integers from 0 to 500,000, and print the final sum.
int = 1
total = 0
while int <=500000: # checked with smaller numbers and seemed good
    total = int + total
#    print(int,total) # checked work here
    int +=2
print(total)

# exc 5 countdown by fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    print(x)

# exc 6 flexible counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)
