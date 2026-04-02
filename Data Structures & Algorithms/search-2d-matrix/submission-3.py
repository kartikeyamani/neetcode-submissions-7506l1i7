class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1=0
        r1=len(matrix)-1
        while l1<=r1:
            mid=(l1+(r1-l1)//2)
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                l=0
                r=len(matrix[mid])-1
                while l<=r:
                    mid1=(l+(r-l)//2)
                    if target==matrix[mid][mid1]:
                        return True
                    elif target>matrix[mid][mid1]:
                        l=mid1+1
                    else:
                        r=mid1-1
                return False
            elif target>matrix[mid][-1]:
                l1=mid+1
            else:
                r1=mid-1
        return False
        


        