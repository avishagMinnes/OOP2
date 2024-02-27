class SocialNetwork:
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super().__new__(cls)
            cls._instances[name].name = name
            cls._instances[name].initialize_network()
        return cls._instances[name]

    def initialize_network(self):
        print("The social network " + self.name + " was created!")
        self.users = {}

    def __str__(self):
        return (f"{self.name} social network:\n{self.users.values().__str__()}")

    # class SocialNetwork:
   # def __init__(self, name):
    #    self.name = name
     #   self.users = {}
      #  print("The social network " + self.name + " was created!")

    def sign_up(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return False
        elif len(password) < 4 | len(password) > 8:
            print("Password not valid.")
            return False
        self.users[username] = User(username, password)
        return self.users[username]

    def log_in(self, username, password):
        if username in self.users:
            if (password == self.users[username].password()):
                print(username + " connected")
                self.users[username].login()
                return True
        return False

    def log_out(self, username):
        print(username + " disconnected")
        self.users[username].logout()
        return True



