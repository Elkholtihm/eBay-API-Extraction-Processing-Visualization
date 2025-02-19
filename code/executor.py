from dotenv import load_dotenv
import os
from utils import get_access_token, search_computers, process_data
import csv

load_dotenv()
# Replace with your eBay application credentials
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    country_codes = input("Enter the country code (you can enter more than one country separated by ','): ")
    try:
        access_token = get_access_token(client_id, client_secret)
        first_write = True  # Initialize first_write flag
        for country_code in country_codes.split(','):
            country_code = country_code.strip()  # Remove any leading/trailing whitespace
            json_data = search_computers(product_name, access_token, country_code)
            print(f"Data form '{country_code}' extracted successfully.")
            filtered_data = process_data(json_data)

            # Write data to CSV
            if filtered_data:
                mode = "w" if first_write else "a"  # "w" for the first write, "a" for append
                with open('data.csv', mode, newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=filtered_data[0].keys())
                    if first_write:
                        writer.writeheader()  # write header only once
                        first_write = False  # disable after the first write
                    writer.writerows(filtered_data)
        print("Data extraction completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")