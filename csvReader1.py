import pandas as pd

filename = '1.csv'
df = pd.read_csv(filename, dtype=str)
# try:
#     df = pd.read_csv(filename)
# except pd.errors.ParserError as e:
#     # Print the error message
#     print(e)
#     # Get the line number of the error
#     line_number = int(str(e).split(' ')[-1])
#     # Delete the line with the error
#     with open(filename, 'r' ,encoding='utf-8') as f:
#         lines = f.readlines()
#     with open(filename, 'w', encoding='utf-8') as f:
#         for i, line in enumerate(lines):
#             if i != line_number - 1:
#                 f.write(line)
#     # Try reading the file again
#     df = pd.read_csv(filename)

# Print the first five rows of the data frame


# import pandas as pd
# import csv


# filename = '1.csv'
# # df = pd.read_csv(filename, dtype=str)


# with open(filename, 'r') as f:
#     reader = csv.reader(f, strict=False)
#     for row in reader:
#         # Process the row data
#         print(row)


# print(df.head(100))

# df.head(100).to_excel('1.xlsx', index=False)

import xlsxwriter

# open the input file
with open('1.csv', 'r', encoding='utf-8') as f:
    # initialize a list to hold the rows
    rows = []

    # read the file line by line
    for line in f:
        # split the line by commas
        fields = line.strip().split(',')
        # append the fields to the list of rows
        rows.append(fields)

# create a new Excel workbook
workbook = xlsxwriter.Workbook('output_file.xlsx')
# create a new worksheet
worksheet = workbook.add_worksheet()

# write the rows to the worksheet
for row_idx, row in enumerate(rows):
    for col_idx, value in enumerate(row):
        worksheet.write(row_idx, col_idx, value)

# close the workbook
workbook.close()
