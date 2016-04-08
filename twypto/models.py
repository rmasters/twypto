class Person:
    def __init__(self, username, publicKey):
        self.username = username
        self.publicKey = publicKey

        self.relationships = []


    def relationship(self, person):
        for follower in self.relationships:
            if follower.follower == person:
                return follower

        return None


    def followers(self):
        return [f for f in self.relationships if f.followed == self]


    def following(self):
        return [f for f in self.relationships if f.follower == self]

class Follower:
    def __init__(self, follower, followed):
        self.follower = follower
        self.followed = followed

        self.posts = []


    def authored(self, person):
        return [p for p in self.posts if p.author == person]


    def sent_to(self, person):
        return [p for p in self.posts if p.recipient == person]


class Post:
    def __init__(self, author, recipient, cipherText):
        self.author = author
        self.recipient = recipient
        self.cipherText = cipherText
