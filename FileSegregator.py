import os            #only segregates
import shutil

def segregate_files(source_dir, target_dir):
    # Define file extensions for each category
    file_extensions = {
        'audio': ['.mp3', '.wav', '.mpeg', '.flac'],
        'video': ['.mp4', '.avi', '.mkv', '.mov'],
        'text': ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx'],
        'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    }

    # Create target directories if they don't exist
    for category in file_extensions:
        os.makedirs(os.path.join(target_dir, category), exist_ok=True)
  

    # Traverse through the source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Check file extension and move it to the appropriate folder
            for category, extensions in file_extensions.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    target_folder = os.path.join(target_dir, category)
                    shutil.move(file_path, target_folder)
                    print(f"Moved '{file}' to '{category}' folder.")
                    break
        # Remove the source directory if it's empty
        if not os.listdir(root):
            os.rmdir(root)

if __name__ == "__main__":
    source_directory = input("Enter the path to the source directory: ")
    target_directory = input("Enter the path to the target directory: ")
    segregate_files(source_directory, target_directory)


#  retains the original source directory after segregation
 
# import os   
# import shutil

# def segregate_files(source_dir, target_dir):
#     # Define file extensions for each category
#     file_extensions = {
#         'audio': ['.mp3', '.wav', '.mpeg', '.flac'],
#         'video': ['.mp4', '.avi', '.mkv', '.mov'],
#         'text': ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx'],
#         'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
#     }

#     # Create target directories if they don't exist
#     for category in file_extensions:
#         os.makedirs(os.path.join(target_dir, category), exist_ok=True)

#     # Copy the source directory to the target directory
#     shutil.copytree(source_dir, os.path.join(target_dir, os.path.basename(source_dir)))

#     # Traverse through the source directory
#     for root, _, files in os.walk(os.path.join(target_dir, os.path.basename(source_dir))):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # Check file extension and move it to the appropriate folder
#             for category, extensions in file_extensions.items():
#                 if any(file.lower().endswith(ext) for ext in extensions):
#                     target_folder = os.path.join(target_dir, category)
#                     shutil.move(file_path, target_folder)
#                     print(f"Moved '{file}' to '{category}' folder.")
#                     break
#         # Remove the source directory if it's empty
#         if not os.listdir(root):
#             os.rmdir(root)

# if __name__ == "__main__":
#     source_directory = input("Enter the path to the source directory: ")
#     target_directory = input("Enter the path to the target directory: ")
#     segregate_files(source_directory, target_directory)