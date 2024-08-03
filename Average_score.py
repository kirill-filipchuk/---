grades = [[5,3,3,5,4] , [2,2,2,3] , [4,5,5,2] , [4,4,3] , [5,5,5,4,5]]
students = {"Johnny" , "Bilbo" , "Steve" , "Khendrik" , "Aaron"}
result = {}
for index, student in enumerate(sorted(students)):
   result[student] = sum(grades[index]) / len(grades[index])

print(result)