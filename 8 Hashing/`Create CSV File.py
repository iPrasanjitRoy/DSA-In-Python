import csv

# Data to be written into the CSV file
data = [['AI20MTECH12021', 56],
        ['AI20MTECH12013', 67],
        ['AI20MTECH14010', 78],
        ['AI20MTECH14011', 89],
        ['AI20MTECH14012', 45],
        ['AI20MTECH14015', 62],
        ['AI20MTECH14016', 92],
        ['AI20MTECH14017', 78],
        ['AI20MTECH14018', 57]]

# Define the CSV file name
filename = "student_scores.csv"

# newline='': This prevents extra blank lines from appearing between rows when writing to the file.

# Writing to CSV
with open(filename, mode='w', newline='') as file:
    print(file)
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Student_Roll_Number", "Score"])
    # Write the data
    writer.writerows(data)

print("CSV file created successfully!")


# Without with, you need to manually open and close the file like this:
# file = open(filename, mode='w', newline='')
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()  # Don't forget to close the file
