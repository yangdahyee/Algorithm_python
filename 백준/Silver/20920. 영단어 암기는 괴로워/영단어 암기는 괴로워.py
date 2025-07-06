import sys 
from collections import Counter 

N,M = map(int,sys.stdin.readline().rstrip().split())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

wordbook =[]
for word in words:
    if len(word) >= M:
        wordbook.append(word)
        
counter = Counter(wordbook)
ans = list(set(wordbook))

ans.sort()
ans.sort(key=lambda x: len(x), reverse=True)
ans.sort(key=lambda x: counter[x], reverse=True)


print("\n".join(ans))