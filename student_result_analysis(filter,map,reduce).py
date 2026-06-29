students = [
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 48},
    {"name": "Amit", "marks": 76},
    {"name": "Neha", "marks": 61}
]

print("\nstudents having above 50 marks:")
res = list(filter(lambda x : x["marks"]>=50 ,students))
print(res)

print("\nGrades:")
names = list(map(lambda x:( x["name"],"A+" if x["marks"] >= 90 else
                            "B+" if x["marks"] >= 75 else
                            "c+" if x["marks"] >= 50 else
                            "Fail"),students))
print(names)

from functools import reduce
def myfun(acc,curr):
    # print(f"Acc:{acc}  curr:{curr}")
    return acc + curr["marks"]     # why we not use ["salary"] on both sides

print("\nAverage marks of class: ")
res1 = reduce(myfun,students,0) # why we not use employee["salary"] 
avg = res1 / len(students)
print(avg)