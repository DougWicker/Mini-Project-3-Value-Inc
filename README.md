# Mini Project 3 - Value Inc

#### Project brief:
Value Inc is a retail store that sells household items all over the world by bulk. The Sales Manager has no sales reporting but he has a brief idea of current sales. He also has no idea of the monthly cost, profit and top selling products. He wants a dashboard on this and says the data is currently stored in an excel sheet.

___

In order to satisfy the project brief, I will need to process and manipulate the dataset using the pandas library in Python.  

Here's a summary of what my Python code will need to do:

1. Import the pandas library for data manipulation.
2. Read the CSV file named 'transaction.csv' and store its contents in a dataframe.
3. Perform financial calculations to determine profit per item, profit per transaction, cost per transaction, and sales per transaction and assign them specific columns.
4. Convert the 'Day', 'Month', and 'Year' columns to string data type and concatenate them to create a new 'Date' column in the 'data' dataframe.
5. Clean any remaining data e.g. tidying decimal places, tidying the Letter case of any qualitative data etc
6. Read the second CSV file named 'value_inc_seasons.csv' and store its contents in a second dataframe.
7. Merge the two dataframes based on the 'Month' column.
8. Drop any unwantedfic columns from the dataframe.
9. Exports the modified dataframe to a new CSV file.

In summary, the code reads transaction data, performs calculations and data transformations, merges data from another file, removes unnecessary columns, and exports the modified data to a new CSV file.

Below is the dashboard that I created with the cleaned dataset:  
[Link to Interactive Dashboard](https://public.tableau.com/app/profile/douglas1371/viz/ValueIncDashboard_16871032271030/SalesDashboard)  
![Value Inc Sales Dashboard](https://github.com/TupperwareBox/DataAnalyticsShowcase/blob/3a15d2e4928ab6976012f945fb2c2dc38d212bfc/Value_Inc/Value%20Inc%20Sales%20Dashboard.png)

This project was part of a Data Analysis Bootcamp and contrbuted to the following certificate:
![Certificate of Completion](https://github.com/TupperwareBox/DataAnalyticsShowcase/blob/main/Bootcamp%20Certificate.jpg)
