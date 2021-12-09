first_name = 'Carlotta'
print(first_name)

last_name = 'Chen'
print(last_name)

age = 29
bank_account = 12345
loves_code = True
print(loves_code)

if age >= 18:
  print("I'm an adult")
elif age >= 13:
  print("I'm a teenager")
else:
  print("I'm a child")

#### Array ####
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
  print(num)
  
print(numbers[5])

#### Open file and loop through it ####
final_grades = open("FinalGrades.csv")
for line in final_grades:
  print(line)
final_grades.close()

final_grades = open("FinalGrades.csv")
a = 0
b = 0
c = 0
for line in final_grades:
  line = line.rstrip('\n').split(',')
  for value in line:
    if value == 'A':
      a += 1
    if value == 'B':
      b += 1
    if value == 'C':
      c += 1
print(a, b, c) 

## .seek() to go back to beginning of file if you
## want to loop again:

final_grades.seek(0, 0)
for line in final_grades:
  print(line)

final_grades.close()

#### Assigning variable to appropriate datatype ####
float_1 = 0.25
float_2 = 40.0
product = float(float_1) * float(float_2)
big_string = "The product was " + str(product)
print(big_string)

#### Date and time plus formatting ####
from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d' % (now.month, now.day, now.year)

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

