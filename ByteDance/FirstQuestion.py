
#
# 输入描述:
# 输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 第3行为一个正整数q代表查询的组数
# 第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。 数据范围n <= 300000,q<=300000 k是整型
#
# 输出描述:
# 输出：一共q行，每行一个整数代表喜好值为k的用户的个数

def question1():
    str = input("请输入user:")
    num = int(str,10)

    klist = []
    strlist = input("请输入score:").split()

    for i in range(num):
        score = int(strlist[i],10)
        klist.append(score)

    str = input()
    cmdNum = int(str,10)

    for i in range(cmdNum):
        strlist = input().split()
        start = int(strlist[0],10)
        end = int(strlist[1],10)
        k = int(strlist[2],10)
        print(getCount(klist,start-1,end-1,k))

# def getCount(nlist,start,end,score):
#     count = 0
#     for k in nlist[start:end+1]:
#         if k == score:
#             count += 1
#     return count

def getCount(nlist,start,end,score):
    if start == end:
        print(start)
        if nlist[start] == score:
            return 1
        else:
            return 0
    d = end - start

    mid = int(d/2)


    count1 = getCount(nlist,start,start+mid,score)
    count2 = getCount(nlist,start+mid+1,end,score)
    return count1+count2




question1()

t = [i for i in range(5)]
print(t)
print(t[2:3])


def testMap():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print(dict.get('Alice'))

    for key, values in dict.items():
        print(key, values)

    a, b = map(lambda x: int(x), input("请输入两个数：").split())
    print(type(a), a)
