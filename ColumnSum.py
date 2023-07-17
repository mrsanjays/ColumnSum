class Solution:
    def ColumnSum(self,array,row):
        col=len(array[0])
        res=[]
        for i in range(col):
            Sum=0
            for j in range(row):
                Sum+=array[j][i]
            res.append(Sum)
        return res

if __name__ == '__main__':

    array=[]
    row=int(input())
    for i in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    print(*Solution().ColumnSum(array,row))
