from .models import Person, Follower, Post
from .encryption import PostFactory, Keyring

keyring = Keyring()

def signup(username):
    key = keyring.generate(username)
    return Person(username, key.publickey())


def follow(follower, followed):
    f = Follower(follower, followed)
    followed.relationships.append(f)
    follower.relationships.append(f)


def post(author, message):
    pf = PostFactory()
    for follower in author.followers():
        ciphertext = pf.create(message, author, follower.follower)
        p = Post(author, follower.follower, ciphertext)
        follower.posts.append(p)


def timeline(user):
    pf = PostFactory()
    posts = []
    for followed in user.following():
        for post in followed.sent_to(user):
            posts.append(post)

    for post in posts:
        post.clearText = pf.read(post, keyring.get(user.username))

    return posts

