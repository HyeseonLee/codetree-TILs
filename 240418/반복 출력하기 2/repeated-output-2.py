import sys

n = int(sys.stdin.readline().strip())

def printt(n):
    if n== 0:
        return
    print("HelloWorld")

    printt(n-1)

printt(n)