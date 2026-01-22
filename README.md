CodeAlpha_EDA_Books
This project is part of my Data Analytics Internship at CodeAlpha.
The objective of this task is to perform Exploratory Data Analysis (EDA) on a books dataset using Python to extract insights, visualize data, and detect anomalies.

Task Description
1. Loaded the books.csv dataset extracted in Task 1.
2. Cleaned the data (converted price from string to numeric).
3. Explored dataset structure, data types, and statistical summary.
4. Answered meaningful business questions such as:
5. Most expensive and cheapest book
6. Average price of books
7. Price distribution and trends
8. Availability of books in stock
9. Visualized insights using graphs:
10. Histogram of book prices
11. Bar chart of availability
12. Detected potential outliers in book prices using IQR method.

Technologies Used
1. Python
2. Pandas
3. Matplotlib

Files in this Repository
1. eda_books.py → Python script for EDA
2. books.csv → Dataset from Task 1
3. price_histogram.png → Histogram of book prices (optional saved image)
4. availability_bar.png → Bar chart of availability (optional saved image)
5. README.md → Project documentation

How to Run the Project
1. Install required libraries:
pip install pandas matplotlib
2. Run the Python script:
python eda_books.py
3. Outputs:
Console prints: first 5 rows, dataset info, statistical summary, most expensive and cheapest books, outlier info.
Graphs displayed and optionally saved in the folder (price_histogram.png and availability_bar.png).

Output
1. Statistical summary of prices (min, max, average, standard deviation)
2. Most expensive book: [Title]
3. Cheapest book: [Title]
4. Price distribution graph (Histogram)
5. Availability status graph (Bar chart)
6. Outlier detection report
