import json
import pandas as pd

# Load JSON data
with open('./Localizable.xcstrings', 'r') as file:
    data = json.load(file)

# Prepare data for Excel
rows = []
for key, value in data["strings"].items():
    row = {'Key': key}
    for lang, translation in value["localizations"].items():
        row[lang] = translation["stringUnit"]["value"]
    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows)

# Save to Excel
from datetime import datetime

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
excel_path = f'./Localizable_{current_time}.xlsx'
df.to_excel(excel_path, index=False)

print(f"Excel file saved to {excel_path}")
