grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
d=[sum(grades[0])/ len(grades[0]),sum(grades[1])/ len(grades[1]),
sum(grades[2])/ len(grades[2]),sum(grades[3])/ len(grades[3]),
sum(grades[4])/ len(grades[4])]
#print(d)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
f=sorted(students)
#print(f)
fin={f[0]:d[0],f[1]:d[1],f[2]:d[2],f[3]:d[3],f[4]:d[4]}
print(fin)


