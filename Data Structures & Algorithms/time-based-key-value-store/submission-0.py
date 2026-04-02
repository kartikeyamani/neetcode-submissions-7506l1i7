class TimeMap:

    def __init__(self):
        self.new_dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.new_dict:
            self.new_dict[key]=[]
        self.new_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.new_dict:
            return ""
        new_arr=self.new_dict[key]
        l=0
        r=len(new_arr)-1
        result=""
        while l<=r:
            mid=(l+r)//2
            if(new_arr[mid][1]<=timestamp):
                result=new_arr[mid][0]
                l=mid+1
            else:
                r=mid-1
        return result

        
        
