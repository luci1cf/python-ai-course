# How to work with Text, CSV and JSOnN Files
import csv

# filename = 'example.txt'

# Not recommended!
# file = open(filename, 'r')
# content = file.read()
# print(content)
# file.close()

# Read Text Files
#------------------------------------------------------------------------------------
# with open(filename, 'r') as file:
#     content = file.read()
#     # print(content)
#
#     for n, line in enumerate(content.splitlines()):
#         print(n, line)

# Append Text
#-----------------------------------------------------------------------------------
# with open(filename, 'a') as f:
#     # content = f.read()    io.UnsupportedOperation: not readable
#
#     f.write('Hello World!\n')
#     f.write('Hello World!\n')
#     f.write('Hello World!\n')

# Write Files
#------------------------------------------------------------------------------------
# with open(filename, 'w') as f:
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')

# Example
#--------------------------------------------------------------------------------------
# import os
#
# filename2 = 'example2.txt'
#
# if not os.path.exists(filename2):
#     with open(filename2, 'w') as f:
#         print(f'Creating a new file: {filename2}')
#         f.write('Hello!\n')
#         f.write('Hello!\n')
#         f.write('Hello!\n')
#         f.write('Hello!\n')
#         f.write('Hello!\n')
# else:
#     print('File {} already exists'.format(filename2))
#
#     print('Content: ' )
#     with open(filename2, 'r') as f:
#         print(f.read())

# Read CSV File
#-----------------------------------------------------------------------------------------
# filename = 'items.csv'
# with open(filename, 'r') as f:
#     # content = f.read()
#     # print(content)
#
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#         # for item in row:
#         #     print(item)

# Append/Write CSV File
#---------------------------------------------------------------------------------------
# filename = 'items.csv'
# with open(filename, 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Toilet', 'Gold', '9999'])

# filename = 'items.csv'
# with open(filename, 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Toilet', 'Gold', '9999'])

# Read JSON files
#---------------------------------------------------------------------------------------
import json
#
# with open('materials.json', 'r') as f:
#     # content = f.read()
#     # print(content)
#
#     data = json.load(f)
#     # print(data)
#     # print(type(data))
#
#     mats = data['materials']
#     for mat in mats:
#         print(mat['name'])
#         print(mat['density'])

# Append to JSON files
#-----------------------------------------------------------------------------------------
# Read JSON
with open('materials.json', 'r') as f:
    data = json.load(f)

# New Material
new_material = {
    "id": "M005",
    "name": "Plaster",
    "density": 2500,
    "cost_per_1000_units": 100
}

# Append New Material
data['materials'].append(new_material)

# Override the File
with open('materials.json', 'w') as f:
    json.dump(data, f, indent=4)