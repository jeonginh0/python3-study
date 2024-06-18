# Counter module

from collections import Counter

text = list("gallahad")
print(text)

c = Counter(text)
print(c)

text = """A press release is the quickest and easiest way to get free publicity.
if well written, a press release can result in multiple publish articles about your
firm and its products. And that can mean new prospects contacting you asking you to sell to
them.""".lower().split()

print(Counter(text))

c = Counter({'red':4, 'blue':2})
print(c)
print(list(c.elements()),"\n")

c = Counter(cats = 4, dogs = 8)
print(c)
print(list(c.elements()))
print()

#sdsd

inventory = Counter(apple = 39, orange = 30, banana = 15)
wastage = Counter(apple = 6, orange = 5, banana = 8)
inventory.subtract(wastage)
print(inventory)
print()

#adad

sales_day1 = Counter(apple=4, orange=9, banana=4)
sales_day2 = Counter(apple=10, orange=8, banana=6)

print(sales_day1 + sales_day2)
print(sales_day2 - sales_day1)
print()

#fdfd

l1 = [0, 1, [2, 3]]
l2 = l1

print(l1 is l2)

l1[1] = 100
l1[2][0] = 200

print(l1)
print(l2)
print(l1 is l2)