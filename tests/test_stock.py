# -*- coding: utf-8 -*-
import os
import sys
import unittest
from src.stock import Product, DB, ReadDB, SaveProduct


class DBTests(unittest.TestCase):

    def setUp(self):
        self.save_db = SaveProduct()
        self.read_db = ReadDB()
        self.product = Product(name="Papa", price="100", quantity=1, sku="1")
        self.db = DB(self.product)
        self.db.save_db()
    
    def tearDown(self) -> None:
        if os.path.exists("inventory.txt"):
            os.remove("inventory.txt")

    def make_inventory_file(self):
        self.save_db.save_stock_in_file_txt(self.db)
        
    def test_make_inventory_file(self):
        self.save_db.save_stock_in_file_txt(self.db)
        if os.path.exists("inventory.txt"):
            self.assertTrue(True)
        else:
            self.assertRaises(FileNotFoundError("File not found"))

    def test_exist_inventory_file(self):
        self.make_inventory_file()
        self.save_db.save_stock_in_file_txt(self.db)
        if os.path.exists("inventory.txt"):
            self.assertTrue(True)
        else:
            with self.assertRaises(FileNotFoundError("File not found")):
                pass

    def test_search_existing_product(self):
        self.assertEqual(self.db.get_product("1"), {'name': 'Papa', 'price': '100', 'quantity': 1, 'sku': '1'})

    def test_search_non_existing_product(self):
        self.assertEqual(self.db.get_product("2"), None)

    def test_load_stock_from_file(self):
        self.make_inventory_file()
        if os.path.exists("inventory.txt"):
            self.assertTrue(True)
            data = self.read_db._load_stock_from_file()
            db = self.db._preload_data(data)
            db.save_product_from_file()
            self.assertEqual(self.db.get_product("1"), {'name': 'Papa', 'price': '100', 'quantity': 1, 'sku': '1'})

        
    def test_load_stock_from_file_without_file(self):
        with self.assertRaises(FileNotFoundError):
            data = self.read_db._load_stock_from_file()
            # db = self.db._preload_data(data)
            # db.save_product_from_file()
            # self.assertEqual(self.db.get_product("1"), {'name': 'Papa', 'price': '100', 'quantity': 1, 'sku': '1'})


    def test_save_db(self):
        self.assertEqual(self.product.name, "Papa") 
        self.assertEqual(self.product.price, '100')
        self.assertEqual(self.product.quantity, 1)
        self.assertEqual(self.product.sku, "1")

    def test_add_product(self):
        sku = "1"
        self.assertIn("1", self.db.get_all_records())
        self.assertEqual(self.db.get_product(sku)["name"], "Papa")

    def test_delete_product(self):
        sku = "1"
        self.db._delete_product(sku)
        self.assertNotIn(sku, self.db.get_all_records())

    def testupdate_product(self):
        sku = "1"
        product = self.db.update_product(sku)
        product.update({
            "name": "Tomate",
            "price": 100,
            "quantity": 200,
        })
        self.assertEqual(self.db.get_product(sku)["name"], "Tomate")
        self.assertEqual(self.db.get_product(sku)["price"], 100)
        self.assertEqual(self.db.get_product(sku)["quantity"], 200)


    def test_option_5(self):
        self.save_db.save_stock_in_file_txt(self.db)