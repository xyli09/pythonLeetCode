

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

def getCount(nlist,start,end,score):
    count = 0
    for k in nlist[start:end+1]:
        if k == score:
            count += 1
    return count