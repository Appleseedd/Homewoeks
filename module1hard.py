students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = [float(sum(grades[0])/len(grades[0]))]
b = [float(sum(grades[1])/len(grades[1]))]
c = [float(sum(grades[2])/len(grades[2]))]
d = [float(sum(grades[3])/len(grades[3]))]
e = [float(sum(grades[4])/len(grades[4]))]
grades = a,b,c,d,e
pare = dict(zip(sorted(students), grades))
print(pare)

