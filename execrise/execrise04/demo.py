# 练习一 字符串
#  1. 定义一个字符串Hello Python 并使用print( )输出
# a = 'Hello Python'
# print(a)
# # 2. 定义第二个字符串Let‘s go并使用print( )输出
# b = "Let's go"
# print(b)
# # 3. 定义第三个字符串"The Zen' of Python" -- by Tim Peters 并使用print( )输出
# c = '"The Zen'
# f = "'"
# e = 'of Pytuon"--by Tim Peters'
# print(c+f+e)
# g = ' Let\'s go!\\ta'
# print(g)
# j = '"The Zen\' of Python" -- by Tim Peters'
转义字符‘\’：用于单双引号同时存在，无法匹配的情况;;;\转义字符：消除字符原有特殊含义或功能，将其转化成可输出的普通字符
# print(j)
# #练习二 字符串基本操作

# 1. 定义两个字符串分别为 xyz 、abc
# a = 'xyz'
# b = 'abc'
# # 2. 对两个字符串进行连接
# print(a+b)
# # 3. 取出xyz字符串的第二个和第三个元素
# print(a[0:1])
# print(a[1:2])
[]用于取出字符串中的元素

# # 4. 对abc输出10次
# print(b*10)
# # 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
# print('a' in (a) )
# print('a' in (b) )
判断是否存在用 in或者 not in


# # 练习三 列表的基本操作
#
# # 1. 定义一个含有5个数字的列表
# a_list = ['1','2','3','4','5']
#
# # 2. 为列表增加一个元素 100
# a_list.append('100')
# print(a_list)
# # 3. 使用remove()删除一个元素后观察列表的变化
# a_list.remove('4')
# print(a_list)
# # 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
# print(a_list[0:3])
切片的过程是从第一个想要的对象开始，到第一个不想要的对象结束。第一个想要的对象到第一个不想要的对象之间的连续对象就是你所有想要的对象。
# print(a_list[3:4])
# a=[1,2,3,4,5]
# print(a[0:5])
#
# # 练习四 元组的基本操作
#元组的总结：
1、元组是一个有序的集合，
2、元组和列表一样可以使用索引、切片来取值。
3、创建元组后不能在原地进行修改替换等操作。
4、元组支持嵌套，可以包含列表、字典和不同元组。
5、元组支持一般序列的操作，例如:＋、*
     >>>(1,2)+(3,4)
     (1,2,3,4)
     >>>(7,8)*4
     (7,8,7,8,7,8,7,8)
    注意＋、*操作时，返回的是一个新元组

元组的不可变性，在保证一个程序安全方面起到很大作用。在Python更深入的学习中你还会学到元组tuple更多特性和操作方法，对于入门级的初学才来说先了解这些元组的基础就可以了。
#
1. 定义一个任意元组，对元组使用append() 查看错误信息
 a = ((1,2),(3,4),(5,6))
# # print(a.append(5))
# # 2. 访问元组中的倒数第二个元素
# print(a[1])
# q = tuple('hello')
tuple函数的功能：它可以一个列表为参数，把它转换为元组。元组不可修改，若需修改，先转换为列表，然后修改，修改后，用tuple 转换为元组。
# print(q)
元组不可修改，若需修改，先转换为列表，然后修改，修改后，用tuple 转换为元组。对元祖修改案例如下：
# a = (2,3,3)#将此元组修改为（3，3，3）
# b = list(a)
# print(b)
# b[0]=3
# print(b)
# print(tuple(b))

# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
c = (11,12,13)
d = tuple('1.')#若不用 tuple，1.不是元组类型，输出来为字符串，无法与另一个元组连接，所以需先用 tuple 转换为元组
print(d)
print(c)
print(c+d)

# 4. 计算元组元素个数
e  = (1,2,3,4,5,6,7)
print(len(e))