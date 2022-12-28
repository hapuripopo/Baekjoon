# 한수인지 아닌지 bool 값을 반환합니다.
def isHansu(orgin_num):
    split_num = [int(i) for i in list(orgin_num)]
    if len(split_num) < 3:
        return True
    else:
        for i in range(1, len(split_num) - 1):
            if (split_num[i] - split_num[i-1]) != (split_num[i+1] - split_num[i]):
                return False
        return True


N = int(input())
cnt = 0

for i in range(1, N + 1):
    if isHansu(str(i)):
        cnt += 1

print(cnt)
