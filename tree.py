n = int(input("请输入： "))
#方法1
# for i in range(1,n+1):
#     starts = '*' * (2 * i + 1)
#     blanks = ' '* (n -i)
#     print(blanks +  starts)

#方法2
for i in range(1, n + 1):
    starts = '*' * (2 * i - 1)
    print(starts.center(2 * n - 1))

for i in range(n):
    print(' ' * (n-1) + '*')
