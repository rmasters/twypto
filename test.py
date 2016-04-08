from twypto.managers import signup, follow, post, timeline, keyring
import binascii

ross = signup("ross")
bot1 = signup("bot1")
bot2 = signup("bot2")

follow(bot1, ross)
follow(bot1, bot2)
follow(ross, bot1)

post(ross, "Hello world")
post(bot2, "Bleep bloop")
post(bot1, "Foo bar")

def current_user(username):
    users = keyring.keys.keys()
    for user in users:
        if user != username:
            del keyring.keys[user]

def print_timeline(user):
    print "Timeline for @%s" % user.username
    print "=" * 20
    for post in timeline(user):
        print "Post from @%s" % post.author.username
        print "CIPHERTEXT: %s" % binascii.b2a_base64(post.cipherText[0]).rstrip()
        print "CLEARTEXT: %s" % post.clearText
        print "-" * 20
    print "\n"

current_user(ross.username)
#current_user(bot1.username)

print_timeline(ross)
print_timeline(bot1)
print_timeline(bot2)
