import os

def get_directory_sizes(directory):
    total_files = 0
    total_folders = 0
    total_size = 0

    for current_folder, subfolders, catalog_files in os.walk(directory):
        total_folders += len(subfolders)
        total_files += len(catalog_files)

        for file in catalog_files:
            file_path = os.path.join(current_folder, file)
            total_size += os.path.getsize(file_path)

    return total_files, total_folders, total_size


def build_struct(directory, depth_level = 0):
    items = os.listdir(directory)

    folders_catalog = []
    files_catalog = []

    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders_catalog.append(item)
        else:
            files_catalog.append(item)

    for folder_name in sorted(folders_catalog):
        print("    " * depth_level + folder_name + "/")
        folder_path = os.path.join(directory, folder_name)
        build_struct(folder_path, depth_level + 1)

    for file_name in sorted(files_catalog):
        print("    " * depth_level + file_name)


directory_path = os.path.join('Module22')
files, folders, size_bytes = get_directory_sizes(directory_path)

print(directory_path)
print("Размер каталога( в Кб):", round(size_bytes/1024, 2))
print("Количество подкаталогов:", folders)
print("Количество файлов:", files)
print("\nСтруктура каталога:")
build_struct(directory_path)

