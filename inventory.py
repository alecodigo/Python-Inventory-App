# -*- coding: utf-8 -*-

import os


class DB:
    def __init__(self, product=None, db={}):
        # import ipdb; ipdb.set_trace()
        self.db = db
        self.product = product

    def _save_db(self):
        self.db.update({
            self.product.sku: {
                "name": self.product.name,
                "price": self.product.price,
                "quantity": self.product.quantity,
                "sku": self.product.sku,
            }  
        })
        
    def _get_product(self, sku):
        # import ipdb; ipdb.set_trace()
        return self.db.get(sku)

    def _delete_product(self, sku):
        self.db.pop(sku)
        return True
    
    def _update_product(self, sku):
        return self._get_product(sku)


class ReadProduct:
    def __init__(self, sku=None):
        self.sku = sku

    def _exist_inventory_file(self):
        if os.path.exists("inventory.txt"):
            return True
        
    def _read_inventory_products(self, sku):
        # import ipdb; ipdb.set_trace()
        if self._exist_inventory_file():
            with open('inventory.txt', "r") as f:
                return f.read()
        else:
            raise FileNotFoundError("File not found")


class SaveProduct:
    def __init__(self, product=None):
        self.products = product

    def _exist_inventory_file(self):
        if os.path.exists("inventory.txt"):
            return True
        
    def _save_inventoy_products(self, product):
        if self._exist_inventory_file():
            with open('inventory.txt', "a") as f:
                f.write(f"product: {product.name}\n")
                f.write(f"price: {product.price}\n")
                f.write(f"quantity: {product.quantity}\n")
                f.write(f"sku: {product.sku}\n")
                f.write(f"------------------\n")
        else:
            with open("inventory.txt", "w") as f:
                f.write(f"product: {product.name}\n")
                f.write(f"price: {product.price}\n")
                f.write(f"quantity: {product.quantity}\n")
                f.write(f"sku: {product.sku}\n")
                f.write(f"------------------\n")

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
        

if __name__ == "__main__":
    save_db = SaveProduct()
    read_db = ReadProduct()
    menu = Menu()
    option = False
    # db = False
    while option != "5":
        menu.print_main_menu()
        option = input("Enter your option: ")
        # Add new product
        if option == "1":
            product_name = input("Enter the product name: ")
            product_price = input("Enter the product price: ")
            product_quantity = input("Enter the product quantity: ")
            product_sku = input("Enter the product sku: ")
            product = Product(product_name, product_price, product_quantity, product_sku)
            db = DB(product)
            db._save_db()

        # Update product
        if option == "2":
            product_sku = input("Enter the product sku: ")
            db = DB()
            product_db = db._update_product(product_sku)
            if product_db:
                menu.print_update_options()
                update_option = input("Enter the update option: ")
                if update_option == "1":
                    product_name = input("Enter the product name: ")
                elif update_option == "2":
                    product_price = input("Enter the product price: ")
                elif update_option == "3":
                    product_quantity = input("Enter the product quantity: ")
                # Update product and save
                product_db.update({
                    "name": product_name if product_name else product_db.get("name"),
                    "price": product_price if product_price else product_db.get("price"),
                    "quantity": product_quantity if product_quantity else product_db.get("quantity"),
                    "sku": product_db.get("sku"),
                }  
            )
            
        # Delete product
        if option == "3":
            product_sku = input("Enter the product sku: ")
            db = DB()
            if db._delete_product(product_sku):
                print(f"Product {product_sku} deleted")
            
        if option == "4":
            db = DB()
            product_sku = input("Enter the product product sku: ")
            print(f"", db._get_product(product_sku))

    # Exit
    if option == "5":
        save_db._save_inventoy_products(product)
