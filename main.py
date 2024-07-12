from Crud import add_mobile, view_mobile, update_mob, delete_mob
from data_Science import generate_report
 

def main():
    while True:
        print("\n Mobile Store Inventory")
        print("1. Add Mobile")
        print("2. View Mobiles")
        print("3. Update Data")
        print("4. Delete Existing")
        print("5. Show Report")
        print("6. Exit")

        ch = input("Enter the Choice :: ")

        if ch == '1':
            try:
                id = input("Enter the product id: ")
                name = input("Enter the product Name: ")
                quantity_in_stock = int(input("Enter quantity in stock: "))
                supplier_name = input("Enter the supplier name: ")
                supplier_contact = input("Enter the supplier contact: ")
                total_cost = int(input("Enter the total cost: "))
                add_mobile(id, name, quantity_in_stock, supplier_name, supplier_contact, total_cost)
            except ValueError:
                print("Invalid input. Please enter numeric values for  quantity in stock, and total cost.")
        
        elif ch == '2':
            view_mobile()

        elif ch == '3':
            try:
                product_id = input("Enter the id to update: ")
                product_name = input("Enter the New product Name (leave blank to skip): ")
                quantity_in_stock = int(input("Enter New quantity in stock : "))
                supplier_name = input("Enter New supplier name (leave blank to skip): ")
                supplier_contact = input("Enter New supplier contact (leave blank to skip): ")
                total_cost = int(input("Enter New total cost : "))
                update_mob(product_id, product_name or None, quantity_in_stock or None, supplier_name or None, supplier_contact or None, total_cost or None )
            except ValueError:
                print("Invalid input. Please enter numeric values for ID, quantity in stock, and total cost.")

        elif ch == '4':
            try:
                d_id = input("Enter id to delete: ")
                delete_mob(d_id)
            except ValueError:
                print("Invalid input. Please enter a numeric value for ID.")

        elif ch == '5':
            # Add functionality for showing reports
            
            print("Showing reports...")
            generate_report()

        elif ch == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        

             
