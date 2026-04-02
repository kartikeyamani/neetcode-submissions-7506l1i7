class Twitter:

    def __init__(self):
        self.tweets={}
        self.time=1
        self.followers={}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId,[]).append((-self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap=[]
        if userId in self.tweets:
            for t in self.tweets[userId]:
                heapq.heappush(maxheap,t)
        if userId in self.followers:
            for user in self.followers[userId]:
                if user in self.tweets:
                    for t in self.tweets[user]:
                        heapq.heappush(maxheap,t)
        newsfeed=[]
        for _ in range(10):
            if not maxheap:
                break
            timestamp,tweetId=heapq.heappop(maxheap)
            newsfeed.append(tweetId)

        return newsfeed
            
        
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followers.setdefault(followerId,set()).add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)