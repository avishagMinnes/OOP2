from Post import PostFactory


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged = True
        self.following = []
        self.posts = []
        self.followers = []
        self.notifications = []

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def login(self):
        self.logged = True;

    def logout(self):
        self.logged = False;

    def follow(self, user):
        if self.logged:
            if user.username not in self.following:
                self.following.append(user.username)
                print(self.username + " started following " + user.username)
                user.followers.append(self)

    def unfollow(self, user):
        if self.logged:
            if user.username not in self.following:
                return
            self.following.remove(user.username)
            print(self.username + " unfollowed " + user.username)
            user.followers.remove(self)

    def publish_post(self, post_type, *args, **kwargs):
        new_post = PostFactory.create_post(self, post_type, *args, **kwargs)
        self.posts.append(new_post)

        for follower in self.followers:
            follower.notifications.append(self.username + " has a new post")

        return new_post

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}"







