name_list = ['zhangsan','lisi','wangwu']

# 1.取值和取索引   list index out of range  列表索引超出范围
print(name_list[1])

# 知道内容，想知道在什么位置
# is not in list  如果传递的数据不在列表中
print(name_list.index('wangwu'))


# 2.修改
name_list[1]='李四'


# 3.增加

name_list.append('yq')  #在末尾加
name_list.insert(2,'杨狗倩')  #在指定索引位置插入
temp_list=['孙悟空','zhubajie']
name_list.extend(temp_list)   #在列表末尾加另一个列表

#删除
name_list.remove('wangwu')   #删除指定数据
name_list.pop()              #默认删除最后一条也可以指定索引
name_list.pop(0)
name_list.clear()            #清空整个列表



print(name_list)