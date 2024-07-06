# Day 2: 30 Days of python programming
first_name = "Kafilat"
last_name = "Adewumi"
full_name = last_name + first_name
country = "Nigeria"
city = "Ilorin"
age = 28
year = 1996
is_married = True
is_true = True
is_light_on = False
school, system, level = "University of Ilorin", "Macbook pro", "year four"


print(school, system, level)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))
print(type(age))



a = 5
b = 4
# add
print(f'{a} + {b} = {a + b}')
# subtract
print(f'{a} - {b} = {a - b}')
# multiply
print(f'{a} * {b} = {a * b}')
# division
print(f'{a} / {b} = {a/b}')
# modulus
print(f'{a} % {b} = {a % b}')
# floor division
print(f'{a} // {b} = {a // b}')  
# power / exponentiation
print(f'{a} ** {b} = {a ** b}')


radius = int(input('Enter radius: '))
area_of_circle = 3.14 * (radius ** 2)   #THr2
print(area_of_circle)
circum_of_circle = (2*3.14) * (radius ** 2)  #2THr2
print(circum_of_circle)

language = 'Python'
last_index = len(language) - 1
print(last_index)
last_letter = language[last_index]
print(last_letter) # n