import re
import pandas as pd
import pdfplumber
import os

folder_path = "bid"
output_file = "bid_summary.xlsx"

columns = [
    "Supplier Name", "Product Name / Item", "Quantity",
    "Unit Price (₹)", "Total Price (₹)", "Delivery Time (Days)",
    "Payment Terms", "Warranty/Guarantee", "File Name"
]

data = []

for file_name in os.listdir(folder_path):
    if file_name.lower().endswith(".pdf"):
        file_path = os.path.join(folder_path, file_name)
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        # Extract fields using regex
        supplier = re.search(r"Supplier Name\s*[:\-]?\s*(.+)", text)
        product = re.search(r"Product Name / Item\s*[:\-]?\s*(.+)", text)
        quantity = re.search(r"Quantity\s*[:\-]?\s*(\d+)", text)
        unit_price = re.search(r"Unit Price\s*[:\-]?\s*([\d,]+)", text)
        total_price = re.search(r"Total Price\s*[:\-]?\s*([\d,]+)", text)
        delivery = re.search(r"Delivery Time\s*\(Days\)\s*[:\-]?\s*([\d,]+)", text)
        payment = re.search(r"Payment Terms\s*[:\-]?\s*(.+)", text)
        warranty = re.search(r"Warranty/Guarantee\s*[:\-]?\s*(.+)", text)

        row = [
            supplier.group(1).strip() if supplier else "",
            product.group(1).strip() if product else "",
            int(quantity.group(1).replace(",", "")) if quantity else 0,
            int(unit_price.group(1).replace(",", "")) if unit_price else 0,
            int(total_price.group(1).replace(",", "")) if total_price else 0,
            int(delivery.group(1).replace(",", "")) if delivery else 0,
            payment.group(1).strip() if payment else "",
            warranty.group(1).strip() if warranty else "",
            file_name
        ]

        data.append(row)

df = pd.DataFrame(data, columns=columns)
df.to_excel(output_file, index=False)
print("Excel created:", output_file)
