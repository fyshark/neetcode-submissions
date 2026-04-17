class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]

        for uid in self.following[userId]:
            feed.extend(self.tweets[uid])

        feed.sort(key = lambda x: -x[0])
        return [tid for _, tid in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
