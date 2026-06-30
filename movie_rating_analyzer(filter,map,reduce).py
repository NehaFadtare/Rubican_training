movies = [
    {"title": "Inception", "rating": 9.0},
    {"title": "Avatar", "rating": 7.8},
    {"title": "Joker", "rating": 8.9},
    {"title": "Titanic", "rating": 7.2}
]

print("\nMovies having rating more than 8:")
res = list(filter(lambda x : x["rating"]>=8.0 ,movies))
for i in res:
    print(i)

print("\nMovie titles:")
titles = list(map(lambda x:x["title"],movies))
for i in titles:
    print(f"title: {i}")


from functools import reduce
def myfun(acc,curr):
    # print(f"Acc:{acc}  curr:{curr}")
    return acc + curr["rating"]     # why we not use ["salary"] on both sides

print("\nAverage rating of all movies: ")
res1 = reduce(myfun,movies,0) # why we not use employee["salary"] 
avg = res1 / len(movies)
print(avg)