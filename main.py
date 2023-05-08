import os
import shutil

start_input = input("Do you want to organize the files? (Y/N)\n- ")

if start_input.lower() == "y":
    extensions = {
        "PNG": "Images",
        "JPG": "Images",
        "WEBP": "Images",
        "MP3": "Musics",
        "MP4": "Videos",
    }
    
    files = os.listdir()

    for file in files:
        file_extension = file.split(".")[-1]
        for extension in extensions:
            if extension.lower() == file_extension.lower():
                if not os.path.exists(extensions[extension]):
                    os.makedirs(extensions[extension])
                else:
                    pass
                shutil.move(file, extensions[extension])
                break

    input("Successfully organized!")
else:
    quit()
