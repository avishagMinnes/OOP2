from Lib.Post import Post


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged = true
        self.following = []
        self.posts = []
        self.followers = []
        self.notifications = []

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    def login(self, username, password):
        logged = true;

    def logout(self, username):
        logged = false;

    def follow(self, user):
        while(self.logged):
            if user.username not in self.following:
                self.following.append(user.username)
                print(self.username + " started following " + user.username)
                user.followers.append(self)

    def unfollow(self, user):
        while(self.logged):
            self.following.remove(user.username)
            print(self.username + " unfollowed " + user.username)
            user.followers.remove(self)

    def publish_post(self, type, *args, **kwargs):
        while(self.logged):
            self.posts.append(PostFactory.create_post(type, *args, **kwargs))
            for follower in self.followers:
                follower.notifications.append(self.username + " has a new post")
            return PostFactory.create_post(type, *args, **kwargs)

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}\n"







