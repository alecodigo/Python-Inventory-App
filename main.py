# -*- coding: utf-8 -*-
from src.exceptions import UnknownException
from src.stock import Product, DB, SaveProduct, Menu, ReadDB

if __name__ == "__main__":
    save_db = SaveProduct()
    read_db = ReadDB()
    if read_db._exist_inventory_file():
        data = read_db._load_stock_from_file()
        db = DB._preload_data(data)
        db._save_product_from_file()
    menu = Menu()
    option = False
    while option != "5":
        menu.print_main_menu()
        option = input("Enter your option: ")
        # Add new product
        if option == "1":
            try:
                product_name = input("Enter the product name: ")
                if not product_name.isalpha():
                    print("\nWarning: Product name must be a string\n")
                    continue
            except:
                raise UnknownException("Unknown error")
            try:
                product_price = abs(int(input("Enter the product price: ")))
                product_quantity = abs(int(input("Enter the product quantity: ")))
            except ValueError as e:
                print('Error: Invalid product price or quantity')
                continue
            try:
                product_sku = input("Enter the product sku: ")
                product = Product(product_name, product_price, product_quantity, product_sku)                
                db = DB(product)
                db.save_db()
            except:
                raise UnknownException("Unknown error")

        # Update product
        if option == "2":
            product_sku = input("Enter the product sku: ")
            # db = DB()
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
            if db._delete_product(product_sku):
                print(f"Product {product_sku} deleted")
            
        if option == "4":
            product_sku = input("Enter the product product sku: ")
            print(f"", db._get_product(product_sku))

    # Exit
    if option == "5":
        save_db._save_stock_in_file_txt(db)