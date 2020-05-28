def knapsack(p, w, v):
    n = len(p)
    lists,arr = [],[[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, v + 1):
            if w[i - 1] <= j:  # 如果当前物品的体积不超过背包的容量，p[i-1]当前物品的价值，w[i-1]当前物品的体积
                arr[i][j] = max(arr[i - 1][j], p[i - 1] + arr[i - 1][j - w[i - 1]])
            else: #如果当前物品的体积超过背包的容量
                arr[i][j] = arr[i - 1][j]
    remain = v

    for i in range(n, 0, -1):
        if arr[i][remain] > arr[i - 1][remain]:
            lists.append(i - 1)  # (i-1)为当前物品的编号
            remain -= w[i - 1]  # 容积减去已经找到的物品，再次寻找

    return arr[-1][-1], lists


if __name__ == '__main__':
    p = [700 ,500, 800 ,600 ,520]  # 物品的价值
    w = [3, 2, 9, 4, 3] # 物品占的体积
    v = 8  # 背包的容量
    print(knapsack(p, w, v))