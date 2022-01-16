
# exc 1 update values in dictionaries and lists
"""Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
"""

from multiprocessing import Value


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1a
def updater(the_list):
    the_list[1][0] = 15
    return the_list

print(updater(x))

# 1b
def Jason(student_list):
    student_list[0]['last_name'] = 'Bryant'
    return student_list

print(Jason(students))

# 1c
def change_directory(sports_list):
    sports_list['soccer'][0] = 'Andres'
    return sports_list

print(change_directory(sports_directory))

# 1d
def change_list_value(the_list):
    the_list[0]['y'] = 30
    return the_list

print(change_list_value(z))

# --------------------------------------------------------------------------
# exc 2 iterate through a list of dictionaries
"""Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:"""

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students):
    
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterate_dictionary(some_list):
    for x in some_list:
        print(f"first_name - {x['first_name']}, last_name - {x['last_name']}")

# print(iterate_dictionary(students))
iterate_dictionary(students)

# --------------------------------------------------------------------------
# exc 3 get values from list of dictionaries
"""Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

Michael
John
Mark
KB

And iterateDictionary2('last_name', students) should output:

Jordan
Rosales
Guillen
Tonel
"""
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for x in some_list:
        for key,val in x.items():
            if key == key_name:
                print(val)

iterateDictionary2('last_name',students)

# exc 4 iterate througha doctionary with list values
"""Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
"""
"""dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for k,v in some_dict.items():
        print(f"-------------\n{k}: {len(v)}\n-------------")
        for x in v:
            print(f" {x}")
        
#get list length
#get each key and print all values
print_info(dojo)