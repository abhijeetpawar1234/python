import csv

csv_file = 'data/store_Data.csv'

def read_csv():
    '''
    Reads the CSV file and returns a list of dictionaries, each representing a row in the CSV.
    '''
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_csv(data):
    '''
    Writes the given data (list of dictionaries) to the CSV file.
    '''
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['product_id', 'product_name', 'quantity_in_stock', 'supplier_name', 'supplier_contact', 'total_cost']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_mobile(product_id, product_name, quantity_in_stock, supplier_name, supplier_contact, total_cost):
    '''
    Adds a new mobile record to the CSV file.
    '''
    data = read_csv()
    new_mobile = {'product_id': product_id, 'product_name': product_name, 'quantity_in_stock': quantity_in_stock,
                  'supplier_name': supplier_name, 'supplier_contact': supplier_contact, 'total_cost': total_cost}
    data.append(new_mobile)
    write_csv(data)

def view_mobile():
    '''
    Displays all mobile records in a formatted table.
    '''
    mobiles = read_csv()

    if not mobiles:
        print("No mobile data found")
        return

    headers = ['product_id', 'product_name', 'quantity_in_stock', 'supplier_name', 'supplier_contact', 'total_cost']
    col_width = {header: len(header) for header in headers}

    for mobile in mobiles:
        for header in headers:
            col_width[header] = max(col_width[header], len(str(mobile[header])))

    separator = '+-' + '-+-'.join(['-' * col_width[header] for header in headers]) + '-+'
    header_row = '| ' + ' | '.join([header.ljust(col_width[header]) for header in headers]) + ' |'

    print(separator)
    print(header_row)
    print(separator)

    for mobile in mobiles:
        row = '| ' + ' | '.join([str(mobile[header]).ljust(col_width[header]) for header in headers]) + ' |'
        print(row)

    # print(separator)

    

def update_mob(product_id, product_name=None, quantity_in_stock=None, supplier_name=None, supplier_contact=None, total_cost=None):
    '''
    Updates an existing mobile record in the CSV file based on product_id.
    '''
    data = read_csv()
    for mobile in data:
        if mobile['product_id'] == product_id:
            if product_name:
                mobile['product_name'] = product_name
            if quantity_in_stock:
                mobile['quantity_in_stock'] = quantity_in_stock
            if supplier_name:
                mobile['supplier_name'] = supplier_name
            if supplier_contact:
                mobile['supplier_contact'] = supplier_contact
            if total_cost:
                mobile['total_cost'] = total_cost
            break
    write_csv(data)



def delete_mob(product_id):
    '''
    Deletes a mobile record from the CSV file based on product_id.
    '''
    data = read_csv()
    data = [mobile for mobile in data if mobile['product_id'] != product_id]
    write_csv(data)








    
              
    
