n,k=[int(i) for i in input().split()]
s=[int(i) for i in input().split()]

cnt = [0] * k
for i in range(n):
    cnt[s[i] % k] += 1

ans = min(cnt[0], 1)
if k % 2 == 0:
    ans += min(cnt[k // 2], 1)
for i in range(1,(k+1)//2):
    ans += max(cnt[i],cnt[k-i])
print(ans)
