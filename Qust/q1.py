mnhd = ['135','123','324','546','768','123','135']
try:
    phone = int(input("请输入手机号码："))
    if len(str(phone)) != 11:
        print("手机号码长度错误")
        exit(0)
    for i in mnhd:
        if i == str(phone)[0:3]:
            break
    else:
        print("不包含有效字段")
        exit(0)
except ValueError:
    print("手机号码错误")
else :
    print("手机格式正确")

