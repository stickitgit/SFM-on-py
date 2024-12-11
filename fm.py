import os
import shutil
import subprocess
from datetime import datetime

class FileManager:
    def __init__(self):
        self.current_path = os.getcwd()
        self.history = []

    def clear_screen(self):
        os.system('clear')

    def show_header(self):
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                         File Manager                           ║")
            print("║                         By    syvxzs                           ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(f"Current Directory:{self.current_path}")
            print("=" * 64)

    def show_menu(self):
            print("\nCommands:")
            print("1. List files and directories")
            print("2. Change directory")
            print("3. Create directory")
            print("4. Create file")
            print("5. Delete file/directory")
            print("6. Copy file/directory")
            print("7. Move file/directory")
            print("8. File/Directory details")
            print("9. Back to previous directory")
            print("0. Exit")

    def list_contents(self):
            try:
                contents = os.listdir(self.current_path)
                print("\nContents:")
                for i, item in enumerate(contents, 1):
                    if os.path.isdir(os.path.join(self.current_path, item)):
                        print(f"{i}. 📁 {item}/")
                    else:
                        print(f"{i}. 📄 {item}")
            except Exception as e:
                print(f"Error: {e}")

    def change_directory(self):
            dir_name = input("Enter directory name (or .. dor parent): ")
            old_path = self.current_path
            try:
                if dir_name == "..":
                    self.current_path = os.path.dirname(self.current_path)
                else:
                    new_path = os.path.join(self.current_path, dir_name)
                    if os.path.isdir(new_path):
                        self.current_path = new_path
                        self.history.append(old_path)
                    else:
                        print("Invalid directory!")
            except Exception as e:
                print(f"Error: {e}")

    def create_directory(self):
            dir_name = input("Enter directory name: ")
            try:
                os.mkdir(os.path.join(str(self.current_path), dir_name))
                print(f"Directory '{dir_name}' created seccessfully!")
            except Exception as e:
                print(f"Error: {e}")

    def create_file(self):
            file_name = input("Enter file name: ")
            try:
                with open(str(os.path.join(str(self.current_path), file_name)), 'w') as f:
                    pass
                    print(f"File '{file_name}' created successfully!")
            except Exception as e:
                print(f"Error: {e}")

    def delete_item(self):
            item_name = input("Enter file/directory name to delete: ")
            try:
                path = os.path.join(str(self.current_path), item_name)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                print(f"{item_name} deleted successfully!")
            except Exception as e:
                print(f"Error: {e}")

    def copy_item(self):
            source = input("Enter source file/directory name: ")
            dest = input("Enter destination path: ")
            try:
                source_path = os.path.join(str(self.current_path), source)
                if os.path.isdir(source_path):
                    shutil.copytree(source_path, os.path.join(dest, source))
                else:
                    shutil.copy2(source_path, dest)
                print(f"'{source}' copied successfully!")
            except Exception as e:
                print(f"Error: {e}")

    def move_item(self):
            source = input("Enter source file/directory name: ")
            dest = input("Enter destination path: ")
            try:
                source_path = os.path.join(str(self.current_path), source)
                shutil.move(source_path, dest)
                print(f"'{source}' moved successfully!")
            except Exception as e:
                print(f"Error: {e}")

    def show_details(self):
            item_name = input("Enter file/directory name: ")
            try:
                path = os.path.join(str(self.current_path), item_name)
                stats = os.stat(path)
                print("\nDetails:")
                print(f"Name: {item_name}")
                print(f"Size: {stats.st_size} bytes")
                print(f"Created: {datetime.fromtimestamp(stats.st_ctime)}")
                print(f"Last modified: {datetime.fromtimestamp(stats.st_atime)}")
                print(f"Last accessed: {datetime.fromtimestamp(stats.st_atime)}")
                print(f"Permissions: {oct(stats.st_mode)[-3]}")
            except Exception as e:
                print(f"Error: {e}")

    def go_back(self):
        if self.history:
            self.current_path = self.history.pop()
        else:
            print("No previus directory in history!")

    def run(self):
            while True:
                self.clear_screen()
                self.show_header()
                self.list_contents()
                self.show_menu()

                choice = input("\nEnter your choice (0-9): ")

                if choice == '0':
                    break
                elif choice == '1':
                    self.list_contents()
                elif choice == '2':
                    self.change_directory()
                elif choice == '3':
                    self.create_directory()
                elif choice == '4':
                    self.create_file()
                elif choice == '5':
                    self.delete_item()
                elif choice == '6':
                    self.copy_item()
                elif choice == '7':
                    self.move_item()
                elif choice == '8':
                    self.show_details()
                elif choice == '9':
                    self.go_back()

                input("\nPress Enter to continue...")

if __name__ == "__main__":
    fm = FileManager()
    fm.run()
