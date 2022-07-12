class user:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        return
    
    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points, "\n")
        return self
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name} {self.last_name} is already enrolled. \n")
        return self
    
    def spend_points(self, amount=int):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"Not enough gold points in {self.first_name}'s account.")
        return self


user1 = user("Dalton", "Quesenberry", "dq2505@gmail.com", 28)
user2 = user("Lizzi", "Browitt", "elisabethbrowitt@gmail.com", 28)
user3 = user("Davis", "Kimball", "dkimball@hotmail.com", 27)

user1.display_info().enroll().spend_points(50).display_info().enroll()
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)
