class Facebook:
    def __init__(self, username, friends_count):
        self.username = username
        self.friends_count = friends_count

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Friends Count: {self.friends_count}")

    def add_friend(self, new_friend):
        print(f"Adding friend: {new_friend}")
        self.friends_count += 1

    # Overloading the add_friend method to handle multiple cases
    def add_friend(self, *new_friends):
        for friend in new_friends:
            print(f"Adding friend: {friend}")
            self.friends_count += 1

    # Overloading the __delattr__ method to prevent attribute deletion
    def __delattr__(self, name):
        print("Deleting attributes is not allowed")


class WhatsApp(Facebook):
    def __init__(self, username, friends_count, phone_number):
        super().__init__(username, friends_count)
        self.phone_number = phone_number

    def display_info(self):
        super().display_info()
        print(f"Phone Number: {self.phone_number}")

    # Overloading the add_friend method in the child class
    def add_friend(self, new_friend, privacy_level):
        print(f"Adding friend: {new_friend} with privacy level: {privacy_level}")
        self.friends_count += 1

    # Overriding the __delattr__ method to allow deleting only specific attributes
    def __delattr__(self, name):
        if name != "phone_number":
            print("Deleting attributes is not allowed")
        else:
            super().__delattr__(name)


class Instagram(Facebook):
    def __init__(self, username, followers_count):
        super().__init__(username, friends_count=0)
        self.followers_count = followers_count

    def display_info(self):
        super().display_info()
        print(f"Followers Count: {self.followers_count}")

    # Overloading the add_friend method in the child class
    def add_follower(self, new_follower):
        print(f"Adding follower: {new_follower}")
        self.followers_count += 1


# Example usage:
facebook_user = Facebook(username="Bilal Hussain", friends_count=100)
facebook_user.display_info()
facebook_user.add_friend("Nouman")
facebook_user.add_friend("Munzir", "Abrar")
# Attempt to delete attribute in Facebook
# This should print "Deleting attributes is not allowed"
del facebook_user.username

print("\n")

whatsapp_user = WhatsApp(username="Nouman", friends_count=50, phone_number="1234567890")
whatsapp_user.display_info()
whatsapp_user.add_friend("Eve", privacy_level="High")
# Attempt to delete phone_number attribute in WhatsApp
# This should print "Deleting attributes is not allowed"
del whatsapp_user.phone_number

print("\n")

instagram_user = Instagram(username="Munzir", followers_count=200)
instagram_user.display_info()
instagram_user.add_follower("Grace")
# Attempt to delete username attribute in Instagram
# This should print "Deleting attributes is not allowed"
del instagram_user.username
