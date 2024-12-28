# -*- coding: utf-8 -*-
import os
import sys
# With the line below, the problem with tne module no fond is solved
# sys.path.append(os.path.abspath(os.path.join(__file__, '../')))
# import ipdb; ipdb.set_trace()
import unittest
from src.stock import Product, DB


class DBTests(unittest.TestCase):

    def setUp(self):
        self.product = Product(name="Papa", price="100", quantity=1, sku="1")
        self.db = DB(self.product)
        self.db._save_db()
    
    def test_save_db(self):
        assert self.product.name == "Papa"
        assert self.product.price == '2a'
        assert self.product.quantity == 1
        assert self.product.sku == "1"

    def test_add_product(self):
        sku = "1"
        self.assertIn("1", self.db._get_all_records())
        self.assertEqual(self.db._get_product(sku)["name"], "Papa")

    def test_delete_product(self):
        sku = "1"
        self.db._delete_product(sku)
        self.assertNotIn(sku, self.db._get_all_records())

    def test_update_product(self):
        sku = "1"
        product = self.db._update_product(sku)
        product.update({
            "name": "Tomate",
            "price": 100,
            "quantity": "a20",
        })
        self.assertEqual(self.db._get_product(sku)["name"], "Tomate")
        self.assertEqual(self.db._get_product(sku)["price"], 100)
        self.assertEqual(self.db._get_product(sku)["quantity"], 200)