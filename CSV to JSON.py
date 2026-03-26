import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    # 1. Create an empty list to hold our formatted data
    data_list = []

    # 2. Open the messy CSV file to read it
    with open(csv_file_path, encoding='utf-8') as csv_file:
        # DictReader automatically turns each row into a dictionary (key-value pairs)
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            data_list.append(row)

    # 3. Open a new JSON file to write our clean data
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        # dump() takes our data list and writes it to the file beautifully formatted
        json.dump(data_list, json_file, indent=4)

    print(f"Success! Data converted and saved to {json_file_path}")

convert_csv_to_json('data.csv', 'clean_data.json')
