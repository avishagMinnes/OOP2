import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post:
    def __init__(self, user, content):
        self.content = content
        self.user = user

    def like(self, user1):
        if user1.logged and user1.username != self.user.username:
            self.user.notifications.append(user1.username + " liked your post")
            print("notification to " + self.user.username + ": " + user1.username + " liked your post")

    def comment(self, user1, content):
        if(user1.logged):
            self.user.notifications.append(user1.username + " commented on your post")
            print("notification to " + self.user.username + ": " + user1.username + " commented on your post: " + content)


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)
        print(self.user.username + ' published a post:\n"' + self.content + '"\n')

    def __str__(self):
        return self.user.username + ' published a post:\n"' + self.content + '"\n'


class ImagePost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)
        print(user.username + " posted a picture\n")

    def display(self):
            try:
                image = mpimg.imread(self.content)
                plt.imshow(image)
                plt.show()
            except FileNotFoundError:
                print("\nShows picture")

    def __str__(self):
        return self.user.username + " posted a picture\n"



class SalePost(Post):
    def __init__(self, user, product, price, location):
        super().__init__(user, product)
        self.price = price
        self.location = location
        self.isSold = False
        print(f"{self.user.username} posted a product for sale:\nFor sale! {self.content}, price: {self.price}, pickup from: {self.location}\n")

    def discount(self, precent, password):
        if self.user.logged and password == self.user.password:
            self.price *= (1 - precent / 100)
            print(f"Discount on {self.user.username} product! the new price is: {self.price}")

    def sold(self, password):
        if self.user.logged and password == self.user.password:
            print(self.user.username + "'s product is sold")
            self.isSold = True


    def __str__(self):
        if self.isSold:
            return f"{self.user.username} posted a product for sale:\nSold! {self.content}, price: {self.price}, pickup from: {self.location}"
        return f"{self.user.username} posted a product for sale:\nFor sale! {self.content}, price: {self.price}, pickup from: {self.location}"


class PostFactory:

    def create_post(user, post_type, *args, **kwargs):
        if post_type == "Text":
            return TextPost(user, *args, **kwargs)
        elif post_type == "Image":
            return ImagePost(user, *args, **kwargs)
        elif post_type == "Sale":
            return SalePost(user, *args, **kwargs)
        else:
            return False

    @staticmethod
    def create_text_post(user, content):
        return TextPost(user, content)

    @staticmethod
    def create_image_post(user, content):
        return ImagePost(user, content)

    @staticmethod
    def create_sale_post(user, product, price, location):
        return SalePost(user, product, price, location)

