import os


def update(file_path: str, root: str):
    with open(file_path, "r") as file:
        paths = file.readlines()

    updated_paths = list[str]()
    for path in paths:
        path = path.strip()
        updated_paths.append(root + path + "\n")

    new_file_name = "updated_" + os.path.basename(file_path)
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    with open(new_file_path, "w") as file:
        file.writelines(updated_paths)

    print("Updated file created successfully: " + new_file_path)


def main():
    root = "/your/path/to/dataset/directory"
    update(file_path=r"/full/path/to/train_files.txt", root=root)
    update(file_path=r"/full/path/to/test_files.txt", root=root)


if __name__ == "__main__":
    main()
