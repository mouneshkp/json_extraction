import json
import csv

# Load JSON data from input file
with open('C:/Users/user/Downloads/input.json', 'r') as json_file:
    data = json.load(json_file)

# Extract required data and store in a list of dictionaries
required_data = []
for item in data['data']['docdata']['b2b']:
    for invoice in item['inv']:
        irn = invoice.get('irn', '')
        for item_details in invoice['items']:
            sgst = item_details.get('sgst', '')
            txval = item_details.get('txval', '')
            cgst = item_details.get('cgst', '')
            required_data.append({'IRN': irn, 'SGST': sgst, 'TXVAL': txval, 'CGST': cgst})

# Define CSV header and keys for data extraction
csv_header = ['IRN', 'SGST', 'TXVAL', 'CGST']
csv_keys = ['IRN', 'SGST', 'TXVAL', 'CGST']

# Write extracted data to CSV file
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    writer.writerows({key: item[key] for key in csv_keys} for item in required_data)

print("Data extracted and stored in 'output.csv'.")
