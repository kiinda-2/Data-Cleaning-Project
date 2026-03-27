## For this project I created a mock example to use to keep the data I used safe. So this just shows the working similar to what I had used for my personal work.

import pandas as pd

# 1. Define input and output file paths
input_file = r'raw_store_data.xlsx'
cleaned_file = r'cleaned_data.csv'
exceptions_file = r'exceptions_list.csv'

print("Loading dataset...")
df = pd.read_excel(input_file)

# Clean column headers -> strip hidden spaces
df.columns = df.columns.str.strip() 

# 2. Create standardized columns for matching (lowercase & trimmed)
account = df['Store Account'].astype(str).str.lower().str.strip()
store_name = df['StoreName'].astype(str).str.lower().str.strip()
brand = df['Product Brand'].astype(str).str.lower().str.strip()

# Initialize a boolean mask where everything is False (Do not exclude yet)
exclude = pd.Series(False, index=df.index)

print("Applying exclusion rules...")

# --- 1. NEBULA MART RULES ---
cond1 = account.str.contains("nebula mart", na=False)
brand1 = brand.isin(["quantum chips", "hyper-cola", "stardust soap"])
exclude |= (cond1 & brand1)

# --- 2. GALAXY GROCERS RULES ---
cond2 = account.str.contains("galaxy grocers", na=False)
brand2_exc1 = (brand == "plasma energy drink") & (~store_name.str.contains("galaxy central", na=False))
exclude |= (cond2 & brand2_exc1)

# 3. Filter the dataframe 
df_cleaned = df[~exclude] # Keep rows NOT in the exclude mask
df_exceptions = df[exclude] # Keep rows that ARE in the exclude mask

print(f"Original row count: {len(df)}")
print(f"Cleaned row count: {len(df_cleaned)}")
print(f"Rows excluded: {len(df_exceptions)}")

# 4. Save outputs to CSV 
print("Saving files...")
df_cleaned.to_csv(cleaned_file, index=False)
df_exceptions.to_csv(exceptions_file, index=False)
print("Success! Data cleaning complete.")

#My output returned the clean excel file in my folder that was a light weight to use and also share
