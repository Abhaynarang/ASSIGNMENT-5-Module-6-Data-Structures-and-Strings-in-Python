# dictionary, ---> {}, key
# dictionary = {key:value, key1:value1.....}

student_marks= {'Alice': 85, 'Sam': 65,'Mark':95,'Nick': 96}
#print(my_dict)

name1 = input("Enter the student name to know their marks : ")

name = name1.capitalize()

if name in student_marks:
    print(f"{name}'s Marks: {student_marks[name]}")
else:
    print("student not found in the records.")