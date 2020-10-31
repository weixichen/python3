n = int(input("请输入一个数："))
if n < 2 :
    print(n,"no")
else:
    for i in range(2, n):
        if n % i == 0 :
            print(n, "no")
            break
    else:
            print(n, "yes")


