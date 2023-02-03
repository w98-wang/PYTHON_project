import pyinputplus
import random

#全局变量，选择项
std = ('红', '黄', '蓝', '绿', '白', '粉')

def judge(true_raw, user_raw):
    true = true_raw
    user = user_raw
    half_correct = []
    full_correct = []
    #输入长度检查
    if len(true) != 4 or len(user) != 4:
        return "输入长度错误"
    #输入值范围检查
    for item in user:
        if not std.__contains__(item):
            return "输入错误值"
    #全对统计
    for i in range(len(user)):
        if user[i] == true[i]:
            full_correct.append(user[i])

    #半对统计
    for item in user:
        if true.__contains__(item):
            if full_correct.__contains__(item):
                continue
            else:
                half_correct.append(item)

    #返回结果
    return str(len(set(full_correct)))+"全对，"+str(len(set(half_correct)))+"半对"


def get_four_color():
    user = []
    while len(user) < 4:
        x = pyinputplus.inputStr('第'+ str(len(user)+1)+'个颜色：')
        if std.__contains__(x):
            user.append(x)
        else:
            print('输入错误值！')
            continue
    return user


true = []
while len(true) < 4:
    x = std[random.randint(0, 5)]
    if true.__contains__(x):
        continue
    else:
        true.append(x)
#print(true)
print("游戏开始，你有6次机会，有以下选项")
print(std)
log = []
for i in range(6):
    print("第"+str(i+1)+"次尝试:")
    #显示历史记录
    if i > 0:
        for l in log:
            print(l)
    user = get_four_color()
    s = judge(true, user)
    if s == "4全对，0半对":
        print("恭喜过关！")
        break
    else:
        print(s)
        #记录log
        logStr = "第" + str(i+1) + "次选择" + user.__str__() + ' 结果：' + s
        log.append(logStr)

print("正确答案：")
print(true)