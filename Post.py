from Lib.User import User
import matplotlib.pyplot as plt


class Post:
    def __init__(self, user, type, content):
        self.type = type
        self.user = user
        self.content = content

    def like(self, user1):
        while(user1.logged):
            self.user.notifications.append(user1.username + " liked your post")
            print("notifaction to " + self.user.username + ": " + user1.username + " liked your post")

    def comment(self, user1, content):
        while(user1.logged):
            self.user.notifications.append(user1.username + " commented on your post")
            print("notifaction to " + self.user.username + ": " + user1.username + ": commented on your post: " + content)


class TextPost(Post):
    def __init__(self, username, content):
        super().__init__(username, content)
        print(username + ' published a post: \n"' + self.content + '"')

    def __str__(self):
        return (username + ' published a post: \n"' + self.content + '"')


class ImagePost(Post):
    def __init__(self, username, image):
        super().__init__(username, image)
        print(username + " posted a picture")

    def display(self):
        plt.imshow(self.content)

    def __str__(self):
        return(username + " posted a picture")



class SalePost(Post):
    def __init__(self, username, product, price, location):
        super().__init__(username, product)
        self.price = price
        self.location = location
        print(self.username + " posted a product for sale: \nFor sale! " + self.content + ", price: " + self.price + ", pickup from: " + self.location)

    def discount(self, precent, password):
        while(self.user.logged):
            if (password == self.user.password):
                self.price = self.price*(1-(precent/100))
                print ("Discount on " + self.user.username + " product! the new price is: " + self.price)

    def sold(self, password):
        while(self.user.logged):
            if (password == self.user.password):
                print(self.user.username + "'s product is sold")

    def __str__(self):
        if(Post.sold(self) == True):
            return( self.username + " posted a product for sale: \nSold " + self.content + ", price: " + self.price + ", pickup from: " + self.location)
        return (self.username + " posted a product for sale: \nFor sale! " + self.content + ", price: " + self.price + ", pickup from: " + self.location)


class PostFactory:
    @staticmethod
    def create_text_post(username, content):
        return TextPost(content)

    @staticmethod
    def create_image_post(username, image):
        return ImagePost(username, image)

    @staticmethod
    def create_sale_post(username, product, price, location):
        return SalePost(username, product, price, location)

