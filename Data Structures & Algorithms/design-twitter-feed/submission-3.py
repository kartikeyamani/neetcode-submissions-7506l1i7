class Twitter:

    def __init__(self):
        self.count=0
        self.tweets=defaultdict(list)
        self.followers=defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap=[]

        res=[]
        heapq.heapify(minheap)
        self.followers[userId].add(userId)
        for follower in self.followers[userId]:
            if follower in self.tweets:
                index=len(self.tweets[follower])-1
                count,tweetId=self.tweets[follower][index]
                heapq.heappush(minheap,[count,tweetId,follower,index-1])
        while minheap and len(res)<10:
            count,tweetId,followerId,index=heapq.heappop(minheap)
            res.append(tweetId)

            if index>=0:
                cnt,tweet=self.tweets[followerId][index]
                heapq.heappush(minheap,[cnt,tweet,followerId,index-1])
        return res



                
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
        
