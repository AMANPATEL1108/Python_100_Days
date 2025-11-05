import os

def rename_png_files_in_folder(folder_path):
    filenames = []
    try:
        all_entries = os.listdir(folder_path)
        png_files = [entry for entry in all_entries if os.path.isfile(os.path.join(folder_path, entry)) and entry.lower().endswith('.png')]
        png_files.sort()

        for index, old_filename in enumerate(png_files, start=1):
            old_file_path = os.path.join(folder_path, old_filename)
            new_filename = f"{index}.png"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            filenames.append((old_filename, new_filename))

    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return filenames

folder_to_check = "path of folder"
renamed_files = rename_png_files_in_folder(folder_to_check)

if renamed_files:
    print(f"Renamed PNG files in '{folder_to_check}':")
    for old_name, new_name in renamed_files:
        print(f"{old_name} -> {new_name}")
else:
    print(f"No PNG files found in '{folder_to_check}' or the folder does not exist.")