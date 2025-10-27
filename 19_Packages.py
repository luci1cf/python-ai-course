import os

# path = r'C:\Users\fluci\Desktop'

# Check if Folder Exists or Create if It Doesn't
# if os.path.isdir(path):
#     print("Path exists.")
# else:
#     print("Path doesn't exist.")
#     # Create new Folder
#     os.makedirs(path)
#     print("Folder created successfully.")

# Join Paths
# path = r'C:\Users\fluci\Desktop'
# list_folder = ['Folder_A', 'Folder_B', 'Folder_C']
#
# for folder in list_folder:
#     new_path = os.path.join(path, folder)
#
#     if not os.path.exists(new_path):
#         os.makedirs(new_path)
#         print('Created folder: {}'.format(folder))

# Rename Files
# path = r'C:\Users\fluci\Desktop\Folder'
#
# for filename in os.listdir(path):
#     print(filename)
#
#     if '.png' in filename:
#         new_filename = filename.replace('.png', '_250125.png')
#
#         abs_old_filepath = os.path.join(path, filename)
#         abs_new_filepath = os.path.join(path, new_filename)
#         os.rename(abs_old_filepath, abs_new_filepath)
#
#         print('Renamed file: {} to {}'.format(filename, new_filename))

# Get Nested Folders
# path = r"C:\Users\fluci\Desktop"
#
# for root, dirs, files in os.walk(path):
#     for file in files:
#         if 'test' in files:
#             # Get Absolute Path
#             abs_path = os.path.join(root, file)
#             print(abs_path)

# Sys.exit - Stop Script Execution
# import sys
# print('Before')
#
# if 100 < 10:
#     sys.exit(0)     # Stop script execution
# print('After')

# Datetime
# from datetime import datetime
#
# now = datetime.now()
# formatted_date = now.strftime("%Y-%m-%d")
# formatted_time = now.strftime("%H:%M:%S")
#
# print(now)
# print(formatted_date)
# print(formatted_time)

# Time Module
# import time
#
# for i in range(50):
#     time.sleep(1)
#     print('Second has passed.')

# Math
# import math
#
# num = 16
# root = math.sqrt(num)
# print(root)

# Pi
# r = 3
# area = math.pi * r**2
# print(area)

# Ceiling (Round UP) / Floor (Round DOWN)
# num = 15.7
# ceil_num = math.ceil(num)
# floor_num = math.floor(num)
# print(ceil_num)
# print(floor_num)

# Random
# import random

# Random Number Generator
# R = random.randint(0, 255)
# G = random.randint(0, 255)
# B = random.randint(0, 255)
# print(R, G, B)

# Random Item Selector
# materials = ['Wood', 'Glass', 'Brick', 'Concrete']
# random_material = random.choice(materials)
# print(random_material)