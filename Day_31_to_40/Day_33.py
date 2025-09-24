info ={"name":"aman","marks":10,"class":1}

# print(info)
# print(info.keys())
# print(info["name"])
# print(type(info))

# for key in info.keys():
#     print(info[key])

print(info.items())

for k ,value in info.items():
    print(k, "-",value)