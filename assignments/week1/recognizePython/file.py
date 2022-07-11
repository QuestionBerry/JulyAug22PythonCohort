num1 = 42 #variable declaration, initialize integer
num2 = 2.3 #variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuple declaration, initialization
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #log statement, dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #log statement, tuple access value

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #conditional if, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if, length check
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5):
    print(x) #log statement
for x in range(2,10,3): 
    print(x) #log statement
x = 0
while(x < 5):
    print(x) #log statement
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)