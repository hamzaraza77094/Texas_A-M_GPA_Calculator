# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Hamza Raza
# Section:     415
# Assignment:  Lab 7b
# Date:        5 Oct 2020

# Asks how many classes you are taking to determine how many times to run the for loop
class_num = int(input("How many classes are you taking: "))

# Blank lists to have class info entered 
class_lst = []
credit_lst = []
grades_lst = []

# GPA total to get the total number of GPA Points from the classes
gpa_total = 0

#Run the code as many times as many classes the user has
for x in range(class_num):
    # Asking for information
    class_n = input("Enter class name: ")
    credit_hours = float(input("Enter the credit hours for that class: "))
    grade = input("Enter final grade for class: ")
    # This determines the GPA point the user gets depending on the class and credit hours
    if grade == 'A':
        gpa_total += (credit_hours * 4)
    elif grade == 'B':
        gpa_total += (credit_hours * 3)  
    elif grade == 'C':
        gpa_total += (credit_hours * 2)
    elif grade == 'D':
        gpa_total += (credit_hours * 1)
    elif grade == 'F' or grade == 'U':
        gpa_total += (credit_hours * 0)
    # Add all of the info to the lists
    class_lst.append(class_n)
    credit_lst.append(credit_hours)
    grades_lst.append(grade)
    print()
# Adding up all of the credit hours in the list gives the total credit hours
total_credit_hours = sum(credit_lst)
gpa = gpa_total / total_credit_hours

#Print all of the outputs, the extra join and strip is to make the display look cleaner
print("Classes you have: ", ', '.join(class_lst))
print("Credits for each class: ", str(credit_lst).strip('[]'))
print("Grades for each class: ", ','.join(grades_lst))
#Round gpa to 4 decimal places
print("GPA: ", round(gpa, 4))
