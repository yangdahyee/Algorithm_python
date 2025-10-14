import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]  

unique_words = list(set(words))  
unique_words.sort()              
unique_words.sort(key=len)        

for word in unique_words:
    print(word)