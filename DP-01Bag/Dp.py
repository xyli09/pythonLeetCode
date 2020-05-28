import numpy as np

# 定义重量
weight = {}
weight["water"] = 3
weight["book"] = 1
weight["food"] = 2
weight["jacket"] = 2
weight["camera"] = 1
# 定义价值
worth = {}
worth["water"] = 10
worth["book"] = 3
worth["food"] = 9
worth["jacket"] = 5
worth["camera"] = 6

# 存放行标对应的物品名:
table_name = {}
table_name[0] = "water"
table_name[1] = "book"
table_name[2] = "food"
table_name[3] = "jacket"
table_name[4] = "camera"

# 创建矩阵,用来保存价值表
table = np.zeros((len(weight), 6))


for i in range(0, len(weight)):   # i 容许的重量
    for j in range(0, 6):     # j 候选物品
        this_name = table_name[i]
        # 获取重量
        this_weight = weight[this_name]
        # 获得价值
        this_worth = worth[this_name]

        # 获取上一个单元格 (i-1,j)的值
        if (i > 0):
            before_worth = table[i - 1, j]
            # 获取（i-1,j-重量）
            temp = 0
            if (this_weight <= j):
                temp = table[i - 1, j - this_weight]
            # (i-1,j-this_weight)+求当前商品价值
            # 判断this_worth能不能用，即重量有没有超标，如果重量超标了是不能加的
            synthesize_worth = 0
            if (this_weight - 1 <= j):
                synthesize_worth = this_worth + temp
            # 与上一个单元格比较,哪个大写入哪个
            if (synthesize_worth > before_worth):
                table[i, j] = synthesize_worth
            else:
                table[i, j] = before_worth
        else:
            # 没有（i-1,j）那更没有(i-1,j-重量),就等于当前商品价值,或者重量不够，是0
            if (this_weight - 1 <= j):
                table[i, j] = this_worth
print(table)

print("--------------------------------------")

