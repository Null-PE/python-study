#列出当前对象所包含的方法 返回值是一个字符串列表
# dir(obj)
# 
#查询文档
# help(obj.func)


#类型比较

L = [1,2,3,4]

if type(L) == type([]):
    print('L is list')
if type(L) == list:
    print('L is list')
if isinstance(L, list): # best one
    print('L is list')

