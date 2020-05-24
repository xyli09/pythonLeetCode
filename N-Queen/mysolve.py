
import collections

result = []
n = 4

#pie :x+y
#na :x-y
def DFS(queens,pie,na):
    i = len(queens) #行数
    collections.defaultdict
    if i == n :
        print("queen:",queens)
        print("pie:",pie)
        print("na",na)
        result.append(queens)
        return None

    for j in range(n):
        if j not in queens and i+j not in pie and i - j not in na:
            DFS(queens+[j],pie+[i+j],na+[i-j])


DFS([],[],[])

for sol in result:
    for i in sol:
        print(["."*i + "Q" +"."*(n - i -1) ])
    print("----------------------")