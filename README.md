# AI Access Data-Cleaning-Project
Data Cleaning project to learn and practice cleaning data using Python, Pandas

* **Tools:** VS Code, Python: pandas, openpyxl

* **Why I chose it:** I frequently work with datasets that are too large for Google Sheets or Excel to handle efficiently (e.g., 250,000+ rows). Attempting complex filtering in Power BI using M Code was becoming sluggish. Python does operations that can process millions of rows in seconds.
  
* **End Goal:** To build a reusable script that reads a massive raw data file, applies conditional exclusion rules based on store accounts and product brands, and automatically outputs a clean CSV file.


## 1. Installation & Setup Instructions
On the terminal of vscode: "pip install pandas openpyxl"

## 2. Minimal Working Exaample
I used a sample dataset to anonymize the data I was working with for privacy.
This script takes a raw dataset, standardizes the text columns, applies specific exclusion rules based on the "Store Account" and "Brand," and exports the cleaned data and the removed exceptions.

## 3. Prompt Journal
Prompt 1: "I'm a junior data analyst analyzing data in Power BI and would like to have my data as an excel from the Power Bi which I had applied given criteria from. I want to use python to clean a dataset that would apply these exemptions in my file. The file is too big to load to google sheets and sluggish on excel. These are the conditions set on power bi using M Code [Inserted the Code]. Translate it to use python code."

AI Response Summary: The AI provided a full Python script utilizing pandas and boolean masking (~exclude) to process the data via vectorization rather than slow loops. It introduced me to .isin() and .str.contains() methods for efficient text matching.

Prompt 2: "The code ran but reached this particular instant and am not sure if it's completed or what. It seems like i has hannged or stopped running. The goal was to have a downloadable excel file but am not seeing any in my folder at the moment. Explain what this could mean and how to resolve it if it is something from my end"

AI Response Summary: The AI explained that writing 260,000+ rows to an .xlsx file is computationally heavy and takes minutes. It suggested switching the output to .csv. Switching to_excel() to to_csv() reduced my save time from several minutes to a few seconds.

## 4. Common Issues & Fixes
Issue 1: CommandNotFoundException for pip

Error: The term 'pip' is not recognized as the name of a cmdlet...

Cause: Python was not added to the Windows PATH environment variable during standard installation.

Fix: Reinstalled Python directly from the Microsoft Store, which automatically manages PATH variables and then tried to reinstall it again

Issue 2: The Hidden Space KeyError

Error: KeyError: 'Store Account'

Cause: Pandas could not find the column name because the raw Excel file had an invisible trailing space in the header (e.g., "Store Account ").

Fix: Added df.columns = df.columns.str.strip() immediately after loading the dataframe to automatically clean all column headers.

Issue 3: File Not Found Error

Error: [Errno 2] No such file or directory

Cause: Typing the file path manually in the terminal failed because the folder name contained spaces, breaking the command string.

Fix: Used the VS Code "run" button "Run Python File in Terminal") to let the IDE automatically handle absolute file paths and string quotes.

## 5. References
Pandas Official Documentation - boolean indexing

Python Official Docs - Raw Strings for Windows Paths

StackOverflow: How to drop rows from pandas data frame that contains a particular string
