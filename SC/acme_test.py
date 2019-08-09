#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Test default product weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight,20)

    def test_default_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability,0.5)

    def test_explode(self):
        """Test explode ... should return boom"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(),'...boom!')

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Test if there are 30 products"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """ Test if all names are valid """
        products = generate_products()
        noun_list = []
        adj_list = []
        for i in products:
            product_name = i.name.split()
            adj_list.append(product_name[0])
            noun_list.append(product_name[1])
        for adj in adj_list:
            self.assertIn(adj,ADJECTIVES)
        for noun in noun_list:
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()