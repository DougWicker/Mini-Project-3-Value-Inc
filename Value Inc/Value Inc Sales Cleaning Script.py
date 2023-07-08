
import pandas as pd

# Importing csv file to dataframe-'data' pd.read_csv('file.csv')
data = pd.read_csv('transaction.csv', sep=';')  # Read the 'transaction.csv' file and store it in the 'data' dataframe

# Example of defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Financial mathematical operations
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SalesPerTransaction = NumberofItemsPurchased * SellingPricePerItem

# Assigning Series Variable using data['Column']
CostPerItem = data['CostPerItem']  # Assign the 'CostPerItem' column from the 'data' dataframe to the variable 'CostPerItem'
NumberofItemsPurchased = data['NumberOfItemsPurchased']  # Assign the 'NumberOfItemsPurchased' column from the 'data' dataframe to the variable 'NumberofItemsPurchased'
CostPerTransaction = CostPerItem * NumberofItemsPurchased  # Calculate the 'CostPerTransaction' by multiplying 'CostPerItem' with 'NumberofItemsPurchased'

# Create a new column with values based on mathematical operation
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']  # Create a new column 'CostPerTransaction' in the 'data' dataframe by multiplying 'CostPerItem' with 'NumberOfItemsPurchased'
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']  # Create a new column 'SalesPerTransaction' in the 'data' dataframe by multiplying 'SellingPricePerItem' with 'NumberOfItemsPurchased'
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']  # Create a new column 'ProfitPerTransaction' in the 'data' dataframe by subtracting 'CostPerTransaction' from 'SalesPerTransaction'
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']  # Create a new column 'Markup' in the 'data' dataframe by dividing the difference of 'SalesPerTransaction' and 'CostPerTransaction' by 'CostPerTransaction'

# Round Function
roundMarkup = round(data['Markup'],2)  # Round the values in the 'Markup' column of the 'data' dataframe to 2 decimal places and assign it to the variable 'roundMarkup'
data['Markup'] = round(data['Markup'],2)  # Update the 'Markup' column in the 'data' dataframe with the rounded values

# Re-format date for Sep so Tableau can recognize (caused by temporary Tableau bug)
data['Month'] = data['Month'].replace('Sep', 'Sept')  # Replace the value 'Sep' with 'Sept' in the 'Month' column of the 'data' dataframe

# Change Column Data Type
day = data['Day'].astype(str)  # Convert the 'Day' column in the 'data' dataframe to string data type and assign it to the variable 'day'
month = data['Month'].astype(str)  # Convert the 'Month' column in the 'data' dataframe to string data type and assign it to the variable 'month'
year = data['Year'].astype(str)  # Convert the 'Year' column in the 'data' dataframe to string data type and assign it to the variable 'year

# Assign series variable with values based on joining three existing variables
my_date = day + '-' + month + '-' + year  # Concatenate the 'day', 'month', and 'year' variables to form a date in the format 'day-month-year'

# Add new column to 'data' with values based on series variable
data['Date'] = my_date  # Add a new column 'Date' to the 'data' dataframe and assign the 'my_date' values to it

# Using split to split the Client Keywords Field
split_col = data['ClientKeywords'].str.split(',', expand=True)  # Split the values in the 'ClientKeywords' column by comma and expand into separate columns

# Creating new columns for split columns
data['ClientAge'] = split_col[0]  # Create a new column 'ClientAge' in the 'data' dataframe and assign the values from the first split column
data['ClientType'] = split_col[1]  # Create a new column 'ClientType' in the 'data' dataframe and assign the values from the second split column
data['LengthofContract'] = split_col[2]  # Create a new column 'LengthofContract' in the 'data' dataframe and assign the values from the third split column

# Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')  # Remove the opening square bracket '[' from the values in the 'ClientAge' column
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')  # Remove the closing square bracket ']' from the values in the 'LengthofContract' column

# Using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()  # Convert the values in the 'ItemDescription' column to lowercase using the lower() function

# -------------------   Merging Files  ----------------------
# 1. Introduce New Dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')  # Read the 'value_inc_seasons.csv' file and store it in the 'seasons' dataframe

# 2. Merge Statement
data = pd.merge(data, seasons, on='Month')  # Merge the 'data' and 'seasons' dataframes based on the 'Month' column and update the 'data' dataframe

# -----------------------------------------------------------

# Deleting Columns w/ Drop Function
data = data.drop('ClientKeywords', axis=1)  # Remove the 'ClientKeywords' column from the 'data' dataframe
data = data.drop('Day', axis=1)  # Remove the 'Day' column from the 'data' dataframe
data = data.drop(['Year', 'Month'], axis=1)  # Remove the 'Year' and 'Month' columns from the 'data' dataframe

# Export to CSV
data.to_csv('ValueInc_Cleaned.csv')  # Export the 'data' dataframe to a CSV file named 'ValueInc_Cleaned.csv' (excluding the index column from export)





















