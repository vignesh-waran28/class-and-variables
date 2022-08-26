class cricketer:
    jersey_no = 1
    def __init__(self,city,name,jersey_no,country):
        self.city = city
        self.name = name
        self.jersey_no = jersey_no
        self.country = country

    def jersey_no(self,no):
        self.jersey_no = self.jersey_no - no

    @classmethod
    def change_jersey_no(cls,no):
        cls.jersey_no = no

    @staticmethod
    def playstatus(count):
        available_battingposition = [1,2,3,4]
        if count in available_battingposition:
            return "batting position will be decided by the captain"
        else:
            return "batting position will be decided by the player"

        
p1 = cricketer("bangalore","kl_rahul",28,"india")
p2 = cricketer("delhi","virat",30,"india")
cricketer.change_jersey_no = 2
print(p1.jersey_no)
print(p2.change_jersey_no)

print(p1.playstatus(8))
print(p2.playstatus(7))
