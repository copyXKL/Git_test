#海象运算符,在判断条件内将10赋值给n
if (n:=10)>11:
    print("true")
else:
    print("false")

# and运算符，and左右的两个条件，只要有一个条件为False，最终结果即为False且不在执行后续此if判断内的代码，当两边条件均为True时，输出True
if C:=((B:=10)>5) and ((A:=10)>9):
    print("and运算",C)
else:
    print('False')

# or运算符，or左右只要有一个条件为True，结果为True
if C:=((A:=5)>10) or ((B:=11)>10):
    print("or运算",C)

# not运算符，对结果进行取反，如果结果是True，则返回False
if C:=((A:=11)>10):
    D = not C
    print("not运算",D)

# in  在指定内容中找到值返回True，否则返回False
A,B = 1,99
C_list = [1,2,3,4,5]
if A in C_list:
    print(C_list,"内存在",A)
else:
    print(C_list,"内不存在",A)
# not in  在指定内容中找到值返回True，否则返回False
if B not in C_list:
    print(C_list,"内不存在",B)
else:
    print(C_list,"内存在",B)
'''
算数运算符
+   加
-   减
*   乘
/   除
%   取模
**  次幂
//  整除，向下取整

比较运算符
==  比较相等
！=  比较不等
>   大于
<   小于
>=  大于等于
<=  小于等于

赋值运算符
=   c = a + b 将 a + b 的运算结果赋值为 c
+=  c += a 等效于 c = c + a
-=  同上
*=  同上
/=  同上
%=  同上
**= 同上
//= 同上
:=  海象运算符

逻辑运算符
and 与
or  或
not 非

成员运算符
in  在指定内容中找到值返回True，否则返回False
not in 在指定内容中不存在值时返回True，否则返回False

身份运算符   用于比较两个对象的存储单元
is      x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
is not  x is not y ， 类似 id(x) != id(y)。如果引用的不是同一个对象则返回结果 True，否则返回 False
id() = 获取变量内存地址的函数
'''