# from _create_contest_folder import check_if_valid_url
import os
from os import path

def main():
    input_text = input("folder name: ")
    if not path.isdir(input_text):
        print(f"The folder is not exist. ({input_text})")
        return
    folder = input_text
    for content in sorted(os.listdir(folder)):
        if not path.isfile(f"{folder}/{content}"):
            continue
        file = content
        old = f"{folder}/{file}"
        print(file)
        if all((file[0] in "abcdef", file[1] == '_', file[-3:] == '.py')):
            new = f"{folder}/{file[0]}_.py"
            os.rename(old, new)

if __name__ == "__main__":
    main()
