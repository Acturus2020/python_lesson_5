from collections import Counter

n = int(input())
list1 = []
for word in range(0,n):
    list1.append(input())
temp = set(list1)
count_unique = 0
for i in temp:
    count_unique += 1
print(count_unique)
a = dict(Counter(list1))
for elem in a:
    print(a[elem], end= ' ')
