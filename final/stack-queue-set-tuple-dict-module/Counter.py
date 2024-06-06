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
