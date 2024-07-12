import pandas as pd
import numpy as np

csv_file = 'data/store_Data.csv'

def show_mobile():
    '''
    Reads the CSV file and prints all mobiles.
    '''
    try:
        data = pd.read_csv(csv_file)
        print('|------------------------avilable mobiles---------------------------|')
        for index, row in data.iterrows():
            print(row['product_name'])
        print('|-------------------------------------------------------------|')
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")

   



def calculate_average_mobile_cost():
    '''
    Calculates the average cost of mobiles from the CSV file.
    '''
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
        return None

    if df.empty:
        print("No mobile data found in the CSV file.")
        return None

    average_cost = df['total_cost'].mean()
    return average_cost


def generate_report():
    '''
    Generates a report based on the mobile data in the CSV file using pandas and numpy.
    '''
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
        return None

    if df.empty:
        print("No mobile data found")
        return

    total_mobiles = len(df)
    
    # Check if 'quantity_in_stock' and 'total_cost' are in df.columns
    if 'quantity_in_stock' in df.columns and 'total_cost' in df.columns:
        total_stock = df['quantity_in_stock'].sum()
        average_cost = df['total_cost'].mean()
    else:
        total_stock = 0
        average_cost = 0

    print("----- Mobile Data Report -----")
    print(f"Total number of mobiles: {total_mobiles}")
    print(f"Total quantity in stock: {total_stock}")
    print(f"Average total cost: {average_cost:.2f}")


def search_mob(name):
    data = pd.read_csv(csv_file)
    '''
    search mobile by name
    '''
    for index, row in data.iterrows():
        if name == row['product_name']:
            print(f"Product Name: {row['product_name']}")
            print(f"Quantity in Stock: {row['quantity_in_stock']}")
            found = True
            break


        if not found:
            print(f"No mobile found with name '{name}'.") 
    




if __name__ == "__main__":
    calculate_average_mobile_cost()
    generate_report()
    show_mobile()
    search_mob()

