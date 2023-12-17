d = {1: 3, 2: 6}


# 新增字典資料
d["key2"] = "123"
# 刪資料
d.pop("1")
print(d)
d.pop("c", None)
print(d)
