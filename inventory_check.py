import csv

with open('inventory_data.csv', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            stock = int(row['stock_level'])
            threshold = int(row['reorder_threshold'])

            if stock < threshold:
                print(f"Product ID: {row['product_id']}, Category: {row['category']}")
        except:
            print("Skipping bad data")
            