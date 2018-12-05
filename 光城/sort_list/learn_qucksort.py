l = [1,9,0,7,6]

def qucikSort(s,low,high):
    if low>high:
        return
    # 以第一个为枢椎
    privor = s[low]
    i = low
    j = high
    while i<j:
        # 从右向左找比枢椎小的值
        while i<j and s[j]>=privor:
            j-=1
        # 从左向右找比枢椎大的值
        while i<j and s[i]<=privor:
            i+=1
        if i<j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
    s[low] = s[i]
    s[i] = privor
    qucikSort(s,low,i-1)
    qucikSort(s,i+1,high)
    return s

print("-------未排序前-------")
print(l)
print("-------排序后-------")
print(qucikSort(l,0,len(l)-1))


def qucikSort1(s,low,high):
    if low>high:
        return
    # 以第一个为枢椎
    privor = s[low]
    i = low
    j = high
    while i<j:
        # 从右向左找比枢椎小的值，并挖坑
        while i<j and s[j]>=privor:
            j-=1
        # 开始填坑
        if i<j:
            s[i]=s[j]
            i+=1
        # 从左向右找比枢椎大的值，并挖坑
        while i<j and s[i]<privor:
            i+=1
        # 开始填坑
        if i<j:
            s[j]=s[i]
            j-=1
    # 枢椎填入ij相等位置
    s[i] = privor
    # 分治法
    qucikSort1(s,low,i-1)
    qucikSort1(s,i+1,high)
    return s
l = [1,9,0,7,6]
print("-------未排序前-------")
print(l)
print("-------排序后-------")
print(qucikSort1(l,0,len(l)-1))