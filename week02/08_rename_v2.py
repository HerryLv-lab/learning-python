import os

folder = "test_files2"
files =  os.listdir(folder)

groups = {}
for name in files:
    base,ext = os.path.splitext(name)
    if ext == "":
        continue
    if ext not in groups:
        groups[ext] = []
    groups[ext].append(name)


print("===重命名计划===")
for ext,names in groups.items():
    for i,old_name in enumerate(names,start=1):
        new_name = f"{i:02d}_{old_name}"
        print(f"{old_name} -> {new_name}")

answer = input("确定执行？输入 y 回车：")
if answer.lower() == "y":
    for ext,names in groups.items():
        for i,old_name in enumerate(names,start=1):
            new_name = f"{i:02d}_{old_name}"
            os.rename(folder + "/" +old_name,folder + "/" +new_name)

    print("重命名结束")
else:
    print("已取消")

