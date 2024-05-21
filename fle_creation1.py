import csv

# Open the CSV file
csv_file = r"C:\Users\LENOVO\Desktop\aiml\Paid Students (1).csv"

# Initialize dictionaries to store counts
count_by_column5 = {}
count_by_column3_and_column5 = {}

# Read the CSV file and process the data
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        # Assuming there are at least 6 columns in your CSV
        if len(row) >= 6:
            column3 = row[3]
            column5 = row[5]

            # Count occurrences in column 5
            if column5 not in count_by_column5:
                count_by_column5[column5] = 1
            else:
                count_by_column5[column5] += 1

            # Count occurrences in column 5, grouped by column 3
            if column3 not in count_by_column3_and_column5:
                count_by_column3_and_column5[column3] = {}
            if column5 not in count_by_column3_and_column5[column3]:
                count_by_column3_and_column5[column3][column5] = 1
            else:
                count_by_column3_and_column5[column3][column5] += 1

# Print the results
print("Count by Column 5:")
print(count_by_column5)

print("\nCount by Column 3 and Column 5:")
print(count_by_column3_and_column5)
