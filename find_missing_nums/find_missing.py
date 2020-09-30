"""
l = [0, 2, 3, 5, 7, 9, 13]
for i in l.copy():
	if l.index(i) != l.index(l[-1]) and (n := i + 1) != l[l.index(i) + 1]:
		print(n)
"""
l = [0, 2, 3, 5, 7, 9, 13]

def find_missing(items: list):
	for elem in items:
		if (index := items.index(elem)) != items.index(items[-1]
				) and (n := elem + 1) != items[index + 1]:
			items.insert(index + 1, n)
			yield n 

for elem in find_missing(l):
	print(elem)

