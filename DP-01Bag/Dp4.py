#coding=utf-8
"""
Created on Thu Mar 25 15:08:59 2019

@author: xyli
"""
import numpy as np

def change(i,j,cost,weight,worth,f,table,table_value):
    total_cost=0
    if (i - weight[j] >= 0):
        t1 = f[i - weight[j]]
        t = t1 + worth[j]

        table[j, i] += name[j]
        table[j, i] += 'f' + str(i - weight[j])
        table_value[j, i] = t;
        if (cost < t):
            total_cost = t
        else:
            cost = t
            total_cost = cost
    return cost


def findValueMinIndex(table_value,value):
     index = -1;
     t = float('inf')
     for i in range(len(weight)):
         if(table_value[i,value]==0):
             continue
         if(table_value[i,value]<=t):
             # print('tv:',table_value[i,n-1])
             t = table_value[i,value]
             index = i
     return index

def findRoute2(table_value,table_name,value):

    index = findValueMinIndex(table_value, value)
    route = table_name[index, value - 1]
    s = route.split('f')
    routeList= []
    routeList.append(int(s[0]))
    preV = int(s[1])
    print('os:',s)
    print('ol:',len(s))
    print('ov:', preV)
    while len(s) > 1:
        index = findValueMinIndex(table_value, preV)
        print('ii:',index)
        route = table_name[index, preV - 1]
        s = route.split('f')

        print('is:',s)
        print('il:',len(s))
        if len(s)>1 :
          preV = int(s[1])
          routeList.append(int(s[0]))
          if int(s[0])==0:
              break
        elif len(s)==1:
            if(s[0].strip()):
             routeList.append(int(s[0]))
             if int(s[0]) == 0:
                 break
    # routeList.append(int(s(0)))
    return routeList

def findRoute(table_value,table_name,value,routeList):

    index = findValueMinIndex(table_value, value)
    # print('oi:',index)
    route = table_name[index, value]
    s = route.split('f')
    # print('os:',s)
    # print('ol:',len(s))

    if len(s) <= 1:
        if(s[0].strip()):
            print('w:',s[0].strip())
            if int(s[0]) == 0:
                return routeList
        else:
            return routeList
    if int(s[1]) == 0:
        routeList.append(int(s[0]))
        return routeList
    if int(s[0]) == 0:
        return routeList

    routeList.append(int(s[0]))
    # print('or:', routeList)
    preV = int(s[1])
    # print('ov:', preV)
    findRoute(table_value,table_name,preV,routeList)


if __name__ == "__main__":

    n = 14  # 表示目标总额
    f = [0 for i in range(n + 1)]
    print(f)

    worth = [1, 1, 1, 1]  # 表示每种券的损耗值。cost函数损耗值越小越好。每个券对应的损耗值根据当前剩余的券来做计算。如果某种券用完，则该券的损耗值设为INF。
    weight = [2, 3, 6, 8]  # 表示单个的面额。实际为券的面额
    name = ['20', '35', '60', '80']  # 表示券的名字
    table = np.zeros((len(weight), n), dtype=np.dtype((np.str_, 500)))
    table_value = np.zeros((len(weight), n))
    # n, m = table_value.shape
    # print(n, m)
    # for i in range(n):
    #     for j in range(m):
    #         table_value[i, j] = float('inf')
    # print(table_value)

    for i in range(1, n):
        # i=2
      # if n%5==0:  #排除不是5的倍数的总额
        cost = float('inf')
        for j in range(4):
            # table[j,i] = '0'
            cost = change(i, j, cost,weight,worth, f, table, table_value)
        f[i] = cost
        print("f[", i, "]=", f[i])

    # print(f)
    print(table)
    print(table_value)
    # index = findValueMinIndex(table_value, 6)
    # print('ooi:', index)
    routeList = []
    findRoute(table_value,table,n-1,routeList)
    print('al:',routeList)


