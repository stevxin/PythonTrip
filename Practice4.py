#列表中元素是数字，对其排序，但在排序时，要把出现在某群组内的数字放在群组外的那些数字之前
# number=[8,3,1,2,5,4,7,6]
# group=[2,3,5,7]
# sort_priority(number,group)
# print(number)
# [2,3,5,7,1,4,6,8]


def sort_method(src,group):
    length=len(src)
    for x in range(1,length):
        for y in range(x,0,-1):
            if src[y] < src[y-1]:
                src[y-1],src[y] = src[y],src[y-1]
    else:
        temp=list(set(src) ^ set(group))
        temp.insert(0,group)
        a,b=temp[0],temp[1:]
        src=[*a,*b]
    return  src

print(sort_method([7,3,1,2,5,4,7,6],[2,3,5,7]))
