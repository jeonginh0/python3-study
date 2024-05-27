# practice1 - 연습문제 1

a = [1]
b = ["a", "b", "c"]
b[1] = a[0]
print(b)
print("---------------------------------------------------------")

f1 = ["orange", "melon", "pineapple"]
f2 = ["watermelon", "grape"]
f2.remove("grape")
f1.append(f2)
print(f1)
print("---------------------------------------------------------")

f = ["apple", "orange", "pear", "strawberry", "melon", "cherry"]
print(f[-3:], f[1::3])
print("---------------------------------------------------------")

f = ["orange", "melon", "pineapple", "cherry"]
n = ['1', '2', '3']
first, second, third = n
print(second * f.index("pineapple"))
print("---------------------------------------------------------")

c = ["red", "green", "blue", "yellow"]
c.insert(1, "blue")
print(c)
print("----------------------------------------------------------")


