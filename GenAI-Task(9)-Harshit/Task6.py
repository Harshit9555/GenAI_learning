# 6.Percentiles & Sorting
import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])
sort_val = np.sort(marks)
print(f"Sorted marks: {sort_val}")

twentyfive = np.percentile(marks,25)
print(twentyfive)

fifty = np.percentile(marks,50)
print(fifty)

seventyfive = np.percentile(marks,75)
print(seventyfive)

avg_marks = np.average(marks)
cnt = 0
for i in marks:
    if i>  avg_marks:
        cnt +=1
print(f"{cnt} student  scored above average marks")
    