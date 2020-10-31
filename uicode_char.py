begin = int(input("请输入开始值： "))
stop = int(input("请输入结束值： "))
s = " "
for  code in range(begin,stop):
    s += chr(code)
print(s)