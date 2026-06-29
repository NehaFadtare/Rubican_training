def generate_report(name, *marks):
    print(f"Student Name:{name}")
    print(Total(marks))
    print(Average(marks))
    print(High(marks))
    print(Low(marks))

def Total(marks):
    return sum(marks)

def Average(marks):
    return sum(marks)/len(marks)

def High(marks):
    return max(marks)

def Low(marks):
    return min(marks)

marks = [90,95,93]

print(generate_report("neha",*marks))

avg = Average(marks)
if avg >=90:
    print("Grade:A")
elif avg >=75:
    print("Grade:B")
elif avg >=50:
    print("Grade:C")
else:
    print("failed!!")
# 90+  -> A
# 75+  -> B
# 50+  -> C
# Below 50 -> Fail