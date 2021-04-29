
def comp(dataslice):
    '''dataslice数据切片
输出比大小状态'''
    if dataslice[0]-dataslice[1]>0:
        return False
    else:
        return True
    #没考虑数据相等的情况
    
def extmark(datalist):
    '''datalist数据列表
输出相应位置的极值标记列表'''
    extm = ['' for i in range(len(datalist))]
    for i in range(len(datalist)-2):
        if comp(datalist[i:i+2]) != comp(datalist[i+1:i+3]):
            extm[i+1] = 'max' if comp(datalist[i:i+2]) else 'min'
    return extm
                


from tkinter.filedialog import askopenfilename
file = askopenfilename() 

with open(file,'r') as f:
    raw_l = f.readlines()

data = []
for each in raw_l:
    data.append(int(each.split()[1][-5:])) #看数据都是最后不超过五位数就直接切片了，也可以lstrip把左边的字母和0去掉

extm = extmark(data) #产生极值点标记列表
for i in range(len(data)): 
    if extm[i]:
        t = '\t'.join([raw_l[i].strip(),extm[i]])
        raw_l[i] = ''.join([t,'\n']) 

with open(file,'w') as f:
    f.writelines(raw_l) #最后的效果是在原文件的最后加上min或max
