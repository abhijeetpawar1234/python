from Crud import read_csv, write_csv
import pandas as pd
import numpy as np

csv_file = 'data/store_Data.csv'


def generate_report():
    '''
    Generates a report based on the mobile data in the CSV file using pandas and numpy.
    '''
    df = read_csv()

    if df.empty:
        print("No mobile data found")
        return

    total_mobiles = len(df)
    total_stock = df['quantity_in_stock'].sum()
    average_cost = df['total_cost'].mean()

    print("----- Mobile Data Report -----")
    print(f"Total number of mobiles: {total_mobiles}")
    print(f"Total quantity in stock: {total_stock}")
    print(f"Average total cost: {average_cost:.2f}")
