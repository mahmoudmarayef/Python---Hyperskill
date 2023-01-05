import os
import sys
import hashlib


class FileHandler:
    def __init__(self):
        self.files_path = []
        self.files_size = {}
        self.dpl_size = []
        self.files_hash = {}
        self.file_num = 1
        self.dpl_files = {}

    def get_files_path(self):
        try:
            root_dir = sys.argv[1]
        except IndexError:
            print("Directory is not specified")
        else:
            for root, dirs, files in os.walk(root_dir, topdown=False):
                for name in files:
                    self.files_path.append(os.path.join(root, name))
        print(self.files_path)

    def get_file_size(self):
        print("Enter file format:")
        file_type = input()
        for file_path in self.files_path:
            if not file_type or os.path.splitext(file_path)[1] == "." + file_type:
                size = os.path.getsize(file_path)
                self.files_size.setdefault(size, []).append(file_path)

        for size in self.files_size:
            if len(self.files_size[size]) > 1:
                self.dpl_size.append(size)
        print(self.dpl_size)

    def compare_file_size(self):
        print('''Size sorting options:
1. Descending
2. Ascending''')
        while True:
            print('''
Enter a sorting option:''')
            sort_option = input()
            if sort_option not in ["1", "2"]:
                print("Wrong option")
                continue
            else:
                descending = sort_option == "1"
                self.dpl_size = sorted(self.dpl_size, reverse=descending)
                for size in self.dpl_size:
                    print(f"{size} bytes")
                    print(*self.files_size[size], sep="\n")
                    print()
                break

    def compute_hash(self):
        while True:
            print("Check for duplicates?")
            duplicates_option = input()
            if duplicates_option not in ["yes", "no"]:
                print("Wrong option")
                continue
            else:
                if duplicates_option == "yes":
                    for size in self.dpl_size:
                        file_hash = {}
                        for file_path in self.files_size[size]:
                            with open(file_path, "rb") as duplicate_file:
                                m = hashlib.md5()
                                m.update(duplicate_file.read())
                                hash_value = m.hexdigest()
                            # map hash value and file path for files in each duplicate size
                            file_hash.setdefault(hash_value, []).append(file_path)

                        self.files_hash[size] = file_hash

                    dpl_size_hash = {}  # duplicate files size and hash
                    for size in self.files_hash:
                        for hash_value in self.files_hash[size]:
                            if len(self.files_hash[size][hash_value]) > 1:
                                dpl_size_hash.setdefault(size, []).append(hash_value)

                    for size in dpl_size_hash:
                        print(f"{size} bytes")
                        for hash_value in dpl_size_hash[size]:
                            print(f"hash: {hash_value}")
                            for x in range(len(self.files_hash[size][hash_value])):
                                self.dpl_files[str(self.file_num + x)] = self.files_hash[size][hash_value][x]
                                print(f"{self.file_num + x}. {self.files_hash[size][hash_value][x]}")
                            self.file_num += len(self.files_hash[size][hash_value])
                break

    def delete_files(self):
        while True:
            print("Delete files?")
            delete_option = input()
            if delete_option == "yes":
                print("Enter file numbers to delete:")
                freed_size = 0
                delete_num = input().split()
                if delete_num:
                    try:
                        for num in delete_num:
                            i = int(num)
                            freed_size += int(os.path.getsize(self.dpl_files[num]))
                            os.remove(self.dpl_files[num])
                        print(f"Total freed up space: {freed_size} bytes")
                        break
                    except ValueError:
                        print("Wrong format")
                    except KeyError:
                        print("Wrong format")
                else:
                    print("Wrong format")

            elif delete_option == "no":
                break
            else:
                print("Wrong option")


handler = FileHandler()
handler.get_files_path()
handler.get_file_size()
handler.compare_file_size()
handler.compute_hash()
handler.delete_files()
