import random

# products class


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000,10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        self.p_div_w = self.price / float(self.weight)
        if self.p_div_w <0.5:
            return 'Not so stealable...'
        if self.p_div_w >1:
            return 'Very stealable!'
        else:
            return 'Kinda stealable!'

    def explode(self):
        self.f_x_w = self.flammability * self.weight
        if self.f_x_w <10:
            return '...fizzle'
        if self.f_x_w >=10 and self.f_x_w <50:
            return '...boom!'
        else:
            return '...BABOOM!!'

# Boxing Glove Class
class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000,10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight<5:
            return 'That tickles.'
        if self.weight>=5 and self.weight<15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'




