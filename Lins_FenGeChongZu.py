

def Words(input_srt):

    #使用[split]方法,将数组以指定关键字进行分割，当数组内存在此关键字时，将关键字转化为逗号【,】将数组分割为不同字符串
    print("分割前："+input_srt)
    work_list = input_srt.split(" ")
    print("分割后：",work_list)
    #翻转
    fanzhuan_list = work_list[-1::-1]
    #重组
    chongzu_list = " ".join(fanzhuan_list)
    print('重组后:',chongzu_list)
    return chongzu_list
if __name__=="__main__":
    input_srt = '超级 星期 五'
    rw = Words(input_srt)
    print('最后结果输出：',rw)