cart = [
    {"product": "Laptop", "price": 50000},
    {"product": "Mouse", "price": 1200},
    {"product": "Keyboard", "price": 2500},
    {"product": "Monitor", "price": 15000}
]

print("\nProducts that price are more than 5000")
res = list(filter(lambda x : x["price"]>5000 ,cart))
print(res)

print("\nName of prosucts:")
names = list(map(lambda x: x["product"],cart))
print(names)

from functools import reduce
def myfun(acc,curr):
    # print(f"Acc:{acc}  curr:{curr}")
    return acc + curr["price"]     # why we not use ["salary"] on both sides

print("\nTotal amount: ")
res1 = reduce(myfun,cart,0) # why we not use employee["salary"] 
print(res1)