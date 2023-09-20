import os


def search_dir(path):
    content = os.listdir(path)

    if not content:  # base case
        return path
    else:
        item_path = os.path.join(path, content[0])
        return search_dir(item_path)


print(search_dir("/Users/jako/private/opt/recursive"))
