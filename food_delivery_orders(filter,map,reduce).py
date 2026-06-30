orders = [
    {"customer": "Rahul", "amount": 450},
    {"customer": "Priya", "amount": 1200},
    {"customer": "Amit", "amount": 750},
    {"customer": "Neha", "amount": 1800}
]

print("orders having bill above 1000:")
res = list(filter(lambda x : x["amount"]>=1000 ,orders))
for i in res:
    print(i)

print("\ncustomer names:")
name = list(map(lambda x:x["customer"],orders))
for i in name:
    print(i)

# for i in orders:
#     print(i["customer"])

from functools import reduce
def myfun(acc,curr):
    # print(f"Acc:{acc}  curr:{curr}")
    return acc + curr["amount"]     # why we not use ["salary"] on both sides

print("\nAverage rating of all movies: ")
res1 = reduce(myfun,orders,0) # why we not use employee["salary"] 
print(res1)