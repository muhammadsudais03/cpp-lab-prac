# import os
# import shutil

# source = "source"
# backup = "Backup"

# os.makedirs(backup, exist_ok=True)

# for file in os.listdir(source):
#     path = os.path.join(source, file)

#     if os.path.isfile(path):
#         shutil.copy(path, backup)

# print("Mudassir,25214")
# print("Backup created successfully")

# import os
# import shutil
# import subprocess

# while True:

#     command = input("MyShell> ").strip()

#     if command == "":
#         continue

#     if command == "exit":
#         print("Shell closed.")
#         break

#     elif command == "pwd":
#         print(os.getcwd())

#     elif command == "dir" or command == "ls":
#         print(os.listdir())

#     elif command.startswith("cd "):
#         path = command[3:]

#         try:
#             os.chdir(path)
#             print("Current Directory:", os.getcwd())
#         except FileNotFoundError:
#             print("Error: Directory not found.")
#         except NotADirectoryError:
#             print("Error: This is not a directory.")

#     elif command.startswith("mkdir "):
#         folder = command[6:]

#         try:
#             os.mkdir(folder)
#             print("Folder created:", folder)
#         except FileExistsError:
#             print("Error: Folder already exists.")

#     elif command.startswith("rmdir "):
#         folder = command[6:]

#         try:
#             os.rmdir(folder)
#             print("Folder removed:", folder)
#         except FileNotFoundError:
#             print("Error: Folder not found.")
#         except OSError:
#             print("Error: Folder is not empty.")

#     elif command.startswith("touch "):
#         filename = command[6:]

#         with open(filename, "w"):
#             pass

#         print("File created:", filename)

#     elif command.startswith("del "):
#         filename = command[4:]

#         try:
#             os.remove(filename)
#             print("File deleted:", filename)
#         except FileNotFoundError:
#             print("Error: File not found.")

#     elif command.startswith("cat "):
#         filename = command[4:]

#         try:
#             with open(filename, "r") as file:
#                 print(file.read())
#         except FileNotFoundError:
#             print("Error: File not found.")

#     elif command == "clear":
#         os.system("cls")

#     else:
#         print("Error: Invalid shell command.")

# filename = "test.txt"

# with open(filename, "w") as file:
#     pass

# print("File created:", filename)

filename = "sample.txt"

with open(filename, "r") as file:
    content = file.read()

print(content)