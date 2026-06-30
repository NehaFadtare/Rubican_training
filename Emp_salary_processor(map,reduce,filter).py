employees = [
    {"name": "Rahul", "salary": 25000},
    {"name": "Priya", "salary": 55000},
    {"name": "Amit", "salary": 40000},
    {"name": "Neha", "salary": 70000}
]

print("\nName of emps:")
names = list(map(lambda x: x["name"],employees))
print(names)

print("\nemp that are having salary more than 50000")
res = list(filter(lambda x : x["salary"]>50000 ,employees))
print(res)


#doubt  1.why
from functools import reduce
def myfun(acc,curr):
    # print(f"Acc:{acc}  curr:{curr}")
    return acc + curr["salary"]     # why we not use ["salary"] on both sides

print("\nTotal amount: ")
res1 = reduce(myfun,employees,0) # why we not use employee["salary"] 
print(res1)