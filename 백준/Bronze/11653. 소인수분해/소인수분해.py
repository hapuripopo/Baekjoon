N = int(input())

if N > 1:
	while(N >= 2):
		for i in range(2, N + 1):
			if N % i == 0:
				N = N // i
				print(i)
				break
			