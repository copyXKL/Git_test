A = 1
'''

列表(list)推导式{
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

字典(dict)推导式
基本格式：
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }

集合(set)推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }

元组(tuple)推导式

'''
#列表（list）推导式
#len()获取数据的长度
#.upper()将name传入的内容转化为大写英文
a_list = ["abc","def",'ghi',"jkl","mno1"]
A_lsit = [name.upper()for name in a_list if len(name)>3]
print("列表",A_lsit)

#字典（dict）推导式,字典推导式使用{}包裹内容，字典：以键值对的形式存放数据
#此代码作用：遍历a_list的内容赋值给Key，通过len(Key)获取Key的长度，再通过Key:len(Key)拼接成键值对，输出【列表数据:长度】的内容
A_dict = {Key:len(Key) for Key in a_list}
print("字典",A_dict)

#集合(set)推导式
#遍历集合(1,2,3)赋值给x，通过(x**3)求集合的次幂输出
A_set = [x**3 for x in (1,2,3)]
print("集合",A_set)

#遍历字符串'abcdefg'赋值给x2，判断x2内不存在'abc'的返回给A_set2
A_set2 = [x2 for x2 in 'abcdefg' if x2 not in 'abc']
print("集合",A_set2)

#元组(tuple)推导式（生成器表达式），元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组，直接输出时，返回生成器对象，需通过其他转换数据类型函数将其进行转换
#与列表推导式不同，此推导式仅在需要时才生成数据，不直接将结果存放在内存里，适合处理大量数据场景
#通过range(1,10)生成从1-10的数字并赋值给x
A_tuple = (x for x in range(1,10))
print('输出生成器对象',A_tuple)
print("将生成器对象转化为列表",list(A_tuple))
#生成器对象为一次性，已经被输出过的生成器，再进行输出时无内容
print("将生成器对象转化为元组",tuple(A_tuple))