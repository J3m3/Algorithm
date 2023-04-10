input = __import__("sys").stdin.readline

input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

if X := A - B:
    print(len(X))
    print(*sorted(A - B))
else:
    print(0)
