'''
Quiz) Using given code, make the program for real estate.

(Example)
Here are 3 real estates.
Gangnam apartment purchase 1 billion in 2010.
Mapo officetels charter 500 million in 2007.
Songpa villa monthly rent 500/50 in 2000.

[code] '''
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
                
    def show_detail(self):
        print("{0} {1} {2} {3} in {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house1 = House("Gangnam", "apartment", "purchase", "1 billion", 2010)
house2 = House("Mapo", "officetels", "charter", "500 million", 2007)
house3 = House("Songpa", "villa", "monthly rent", "500/50", 2000)

List = []
List.append(house1)
List.append(house2)
List.append(house3)

for house in List:
    house.show_detail()