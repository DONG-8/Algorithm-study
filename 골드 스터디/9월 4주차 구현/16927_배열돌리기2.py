import sys
sys.stdin = open('test.txt')

N, M, R = map(int, sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

