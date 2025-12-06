A = 1
'''
迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。
iter:创建一个迭代器对象，迭代器对象可以用来逐个访问可迭代对象中的元素
next:调用 next 函数时，迭代器会返回其当前位置的下一个元素，并将内部指针移动到下一个位置，当迭代器耗尽（即没有更多元素可返回）时，会引发 StopIteration 异常（可结合try使用）
字符串，列表或元组对象都可用于创建迭代器
'''
list = [1,2,3,4,5,6]
it = iter(list)#创建迭代器
print('输出迭代器内容（列表的一个元素）',next(it))
print('输出迭代器内容（列表的二个元素）',next(it))
print('输出迭代器内容（列表的三个元素）',next(it))
#遍历输出迭代器内容
for x in it:
    print(x,end=" ")
    print()

list_2 = [1,2,3,4,5,6]
it  = iter(list_2)
while True:
    try:
        print("循环输出迭代器内容：",next(it))
    except StopIteration:
        print("迭代器已耗尽")
        break