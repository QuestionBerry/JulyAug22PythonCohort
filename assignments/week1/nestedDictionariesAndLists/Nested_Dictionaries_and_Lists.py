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

#1 Update Values in Dictionaries and Lists
x[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

#2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    
def iterateDictionary(some_list):
    for dictionary in some_list:
        studentInfo = ""
        for key in dictionary:
            if studentInfo: #adds a comma and space after each key-value pair if string is not empty
                studentInfo += ", "
            studentInfo += key + " - " + dictionary[key]
        print(studentInfo)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterateDictionary(students)

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for i in some_dict[key]:
            print(i)
        print() #add line break after list completes

printInfo(dojo)