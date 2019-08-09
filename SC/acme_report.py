from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    product_list = []

    # create a list of product names
    for i in range(num_products):
        adj = sample(ADJECTIVES,1)[0]
        noun = sample(NOUNS,1)[0]
        prod_name = str(adj) + ' ' + str(noun)
        product_list.append(prod_name)

    # iterate over product names to create products
    for name in product_list:
        class Products(Product):
            def __init__(self, name, price=randint(5,101), weight=randint(5,101),
                         flammability=uniform(0,2.5),identifier=randint(1000000, 10000000)):
              self.name = name
              self.price = price
              self.weight = weight
              self.flammability = flammability
              self.identifier = identifier
        products.append(Products(name))

    return products


def inventory_report(products):
    unique_name_list = []
    weight_list = []
    price_list = []
    flam_list = []

    for i in products:
        if i.name not in unique_name_list:
            unique_name_list.append(i.name)

        weight_list.append(i.weight)
        price_list.append(i.price)
        flam_list.append(i.flammability)

    def mean(num_list):
        return round(sum(num_list)/float(len(num_list)),2)

    print('The number of unique product names are:', len(unique_name_list))
    print('The average price of products are:', mean(price_list))
    print('The average weight of products are:', mean(weight_list))
    print ('The average flammability of products are:', mean(flam_list))


if __name__ == '__main__':
    inventory_report(generate_products())



