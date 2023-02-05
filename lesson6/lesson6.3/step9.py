eye = ((1, 0, 0, 0, 0),
       (0, 1, 0, 0, 0),
       (0, 0, 1, 0, 0),
       (0, 0, 0, 1, 0),
       (0, 0, 0, 0, 1))
n = int(input())

new_eye= eye[:n]
ans = ()
for i in range(n):
    ans += (new_eye[i][:n],)
for row in ans:
    print(*row)