# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity=capacity
#         self.newdict={}
#         self.newlist=[]
        

#     def get(self, key: int) -> int:
#         if(self.newdict.get(key)==None):
#             return -1
#         else:
#             i=0
#             while self.newlist[i]!=key:
#                 i=i+1
#             self.newlist.pop(i);
#             self.newlist.append(key)
#             return self.newdict[key]
        

#     def put(self, key: int, value: int) -> None:
#         if len(self.newdict)<self.capacity:
#             if self.newdict.get(key)==None:
#                 self.newdict[key]=value
#                 self.newlist.append(key)
#             else:
#                 self.newdict[key]=value
#                 i=0
#                 while self.newlist[i]!=key:
#                     i=i+1
#                 self.newlist.pop(i);
#                 self.newlist.append(key)
#         else:
#             newkey=self.newlist[0]
#             self.newlist.pop(0)
#             del self.newdict[newkey]
#             self.newlist.append(key)
#             self.newdict[key]=value
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.newdict = {}   # stores key -> value
        self.newlist = []   # stores keys in usage order

    def get(self, key: int) -> int:
        if key not in self.newdict:
            return -1
        # Move key to end (most recently used)
        self.newlist.remove(key)
        self.newlist.append(key)
        return self.newdict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.newdict:
            # Update value
            self.newdict[key] = value
            # Move to end
            self.newlist.remove(key)
            self.newlist.append(key)
        else:
            if len(self.newdict) >= self.capacity:
                # Remove least recently used key
                old_key = self.newlist.pop(0)
                del self.newdict[old_key]
            # Insert new key
            self.newdict[key] = value
            self.newlist.append(key)





        
                

                


        
