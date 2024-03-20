#3.lOOP
#A. create a loop that prints intergers from 5 to 10 ,including 10.
#using the for loop

for i in range(5, 11):
 print(i)

"""using the while loop

current_no = 5
while current_no <= 10:
    print(current_no)
current_no += 1"""

#B.Create a loop that generate a list of integers from 5 to 10 , including 10.

#using the for loop

a_list_of_integers = []

for i in range(5, 11):
    a_list_of_integers.append(i)

print(a_list_of_integers)

''''using the while loop

a_list_of_integers = []
current_no = 5

while current_no <= 10:
    a_list_of_integers.append(current_no)
    current_no += 1

print(a_list_of_integers)'''


#c.create a loop that multiplies all the integers from 5 to 10 inincluding 10

#using for loop

number_in_the_range= 1

for i in range(5, 11):
    number_in_the_range = number_in_the_range * i

print(number_in_the_range)

"""using while loop
result = 1
current_number = 5

while current_number <= 10:
    result *= current_number
    current_number += 1

print(result)

x=1

for i in range(5,11):
    x=x*i
    
print (x)"""