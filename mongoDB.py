import pymongo

myclient = pymongo.MongoClient('mongodb://47.103.55.173:27017/')

# db = myclient.Test
# mongo_collection1 = db.Test_01    # 或者 mongo_collection1 = db['Test_01']
# mongo_collection2 = db.Test_02


db = myclient.xfbms
db.authenticate("xfbms", "xfbms")

# collection = db.xfbms

# 查看全部表名称
# db.collection_names()
# print(db.collection_names())

collist = db.collection_names()
myquery = {"txid": "8824ffc6ac7382c7f485f8c5c2af33f9c12d62d12bf5eaa41f6fe0781722cfec"}
for col in collist:
    print(col)
    mycol = db[col]
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


mycol = db["SaleDeliverClearingTB"]
SalesOrderTH_Col = db["SalesOrderTB"]

for x in mycol.find():
    data = x["data"]
    t=data["slsOrder"]
    dc = data["DocCode"]
    sor = data["slsOrderRowid"]
    # date = data["pricedate"]
    if t is not None:
        print("slsOrder:"+t)
        print("doccode:"+dc)
        print("rowid:"+sor)
        # print(date)
        myquery = {"data.DocCode": t}
        mydoc = SalesOrderTH_Col.find(myquery)
        for doc in mydoc:
            print("doc:"+doc["data"]["DocCode"])

        # if "pricedate" in data:
        #   date = data["pricedate"]
        #   print(date)
        # else:
        #     print("pricedate not in dict!")
for so in SalesOrderTH_Col.find():
    data2 = so["data"]
    t2 = data2["DocCode"]
    t3 = data2["rowid"]
    t4  = data2[""]
    if t is not None:
        print("success:"+t2)
        print(t3)

# myquery = { "data.DocCode": "DFWM190609561" }
# mydoc = mycol.find(myquery)
# # print(mydoc)
# for x in mydoc:
#     print(x)

