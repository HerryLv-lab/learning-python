import os


folder = "test_files"
files = os.listdir(folder)
txt_files = []
for name in files:
    if name.endswith(".txt"):
        txt_files.append(name)

print("要重命名的文件",txt_files)


number = 1
for old_name in txt_files:
    new_name = f"{number:02d}_{old_name}"
    os.rename(folder + "/" + old_name,folder + "/" +new_name)
    print(f"{old_name} -> {new_name}")
    number += 1
