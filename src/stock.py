# -*- coding: utf-8 -*-


class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DB, cls).__new__(cls)
            cls._instance.db = {}
        return cls._instance

    def __init__(self, product):
        self.product = product

    def save_db(self):
        self.db.update({
            self.product.sku: {
                "name": self.product.name,
                "price": self.product.price,
                "quantity": self.product.quantity,
                "sku": self.product.sku,
            }  
        })
        
    def _get_product(self, sku):
        return self.db.get(sku)

    def _delete_product(self, sku):
        self.db.pop(sku)
        return True
    
    def _update_product(self, sku):
        return self._get_product(sku)

    def _get_all_records(self):
        return self.db

# class ReadProduct:
#     def __init__(self, sku=None):
#         self.sku = sku

#     def _exist_inventory_file(self):
#         if os.path.exists("inventory.txt"):
#             return True
        
#     def _read_inventory_products(self, sku):
#         # import ipdb; ipdb.set_trace()
#         if self._exist_inventory_file():
#             with open('inventory.txt', "r") as f:
#                 return f.read()
#         else:
#             raise FileNotFoundError("File not found")


class SaveProduct:
    def __init__(self, product=None):
        self.products = product

    # def _exist_inventory_file(self):
    #     if os.path.exists("inventory.txt"):
    #         return True
        
    def _save_stock_in_file_txt(self, db):
        records = db._get_all_records()
        for k, v in records.items():
            with open("inventory.txt", "a") as f:
                f.write(f"{k}: {v}\n")


class Product:
    def __init__(self, name, price, quantity, sku):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sku = sku

class Menu:
    def print_title(self):
        print("============================================================")
        print("\n****** Welcome to the Inventory Management System ******\n")
        print("============================================================")

    def print_options(self):
        print("Please select an option:")
        print("1. Add a new product")
        print("2. Update a product")
        print("3. Delete a product")
        print("4. Search a product")
        print("5. Exit")

    def print_main_menu(self):
        self.print_title()
        self.print_options()
    
    def print_update_options(self):
        print("Please select an option:")
        print("1. Update a name")
        print("2. Update a price")
        print("3. Update a quantity")
        

