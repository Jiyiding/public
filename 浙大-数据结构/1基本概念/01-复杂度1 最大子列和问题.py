#01-复杂度1 最大子列和问题
num = int(input())
ls = [int(x) for x in input().split()] #列表推导式
ThisSum = MaxSum = 0
for i in range(num):
    ThisSum += ls[i]
    if(ThisSum > MaxSum):
        MaxSum = ThisSum
    elif(ThisSum < 0):
        ThisSum = 0
print(MaxSum)


#思路一：遍历法
class resolution:
    def maxSubArray(self,num):
        onesum = 0,maxsum = num[0]
        for i in range(len(num)):
            onesum += num[i]
            maxsum = max(onesum,maxsum)
            if(onesum < 0):
                onesum = 0
        return maxsum














