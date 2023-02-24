n, k = map(int, input().split(' '))
divs = []

for i in range(1, n+1):
	if n%i == 0:
		divs.append(i)

if len(divs) < k:
	print(0)

else:
	print(divs[k-1])
	