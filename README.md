# Mini Project 3 - Value Inc

#### Project brief:
Value Inc is a retail store that sells household items all over the world in bulk. The Sales Manager has no sales reporting but he has a brief idea of current sales. He also has no idea of the monthly cost, profit and top-selling products. He wants a dashboard on this and says the data is currently stored in an Excel sheet.

___

In order to satisfy the project brief, I will need to process and manipulate the dataset using the Pandas library in Python.  

Here's a summary of what my Python code will need to do:

1. Import the Pandas library for data manipulation.
2. Read the CSV file 'transaction.csv' and store its contents in a dataframe.
3. Perform financial calculations to determine profit per item, profit per transaction, cost per transaction, and sales per transaction and assign them specific columns.
4. Convert the 'Day', 'Month', and 'Year' columns to string data type and concatenate them to create a new 'Date' column in the 'data' dataframe.
5. Clean any remaining data e.g. tidying decimal places, tidying the Letter case of any qualitative data etc
6. Read the second CSV file named 'value_inc_seasons.csv' and store its contents in a second dataframe.
7. Merge the two dataframes based on the 'Month' column.
8. Drop any unwantedf columns from the dataframe.
9. Exports the modified dataframe to a new CSV file.

In summary, the code reads transaction data, performs calculations and data transformations, merges data from another file, removes unnecessary columns, and exports the modified data to a new CSV file.

Below is the dashboard that I created with the cleaned dataset:  
[Link to Interactive Dashboard](https://public.tableau.com/app/profile/douglas1371/viz/ValueIncDashboard_16871032271030/SalesDashboard)  
![Value Inc Sales Dashboard](https://github.com/DougWicker/Mini-Project-3-Value-Inc/blob/5e66c6b5dd25341576bd9327cb0fe3c047953f10/Value%20Inc/Value%20Inc%20Sales%20Dashboard.png)

This project was part of a Data Analysis Bootcamp, hosted on Udemy and Created by Dee Naidoo, and contributed to the following certificate:
![Certificate of Completion](https://github.com/DougWicker/Mini-Project-3-Value-Inc/blob/main/Bootcamp%20Certificate.jpg)
