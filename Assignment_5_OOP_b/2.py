class User(object):
    usercount = 0

    def __init__(self, user):
        self.user = user
        User.usercount += 1


u1 = User("johnsmith10")
print(User.usercount)
u2 = User("marysue1989")
print(User.usercount)