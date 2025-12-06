A = 1
'''
Python推导式：

列表(list)推导式{
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

字典(dict)推导式

集合(set)推导式

元组(tuple)推导式

'''
#列表（list）推导式
#len()获取数据的长度
#.upper()将name传入的内容转化为大写英文
a_list = ["abc","def",'ghi',"jkl","mno1"]
A_lsit = [name.upper()for name in a_list if len(name)>3]
print(A_lsit)