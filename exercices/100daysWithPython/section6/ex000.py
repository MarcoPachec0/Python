student_heights = [180, 124, 165, 173, 189, 169, 146]
totalHeight = 0
totalStudents = 0

for height in student_heights:
    totalHeight += height
    totalStudents += 1

averageHeight = totalHeight/totalStudents

print(f'The total of students is {totalStudents} and the total of height is {totalHeight}')
print(f'The average height is {averageHeight:.2f}')


