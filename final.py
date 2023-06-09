import csv
data_1 = []
data_2 = []

with open("brightest_stars_formatted.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        data_1.append(row)

with open("brown_dwarfs_formatted.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        data_2.append(row)

headers_1 = data_1[0]
star_data_1 = data_1[1:]

headers_2 = data_2[0]
star_data_2 = data_2[1:]

headers = headers_1 + headers_2
merged_data = []

for index, data_row in enumerate(data_1):
    if index == 0:
        continue
    merged_data.append(data_1[index] + data_2[index])

with open("final_merged_data.csv", "a+") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(merged_data)
