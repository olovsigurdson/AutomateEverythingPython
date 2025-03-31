from pathlib import Path

#p1 = Path('files')

#print(p1.name)

#if p1.exists():
#    with open(p1, 'r') as filen:
#        print(filen.read())


root_dir = Path('files')
file_paths = root_dir.iterdir()

for path in file_paths:
    for i in path.iterdir():
        pass


file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        grand_parent_name = path.parent.parent.stem
        parent_name = path.parent.stem
        new_filename = grand_parent_name + "-" + parent_name + '-' + path.name
        new_name = path.with_name(new_filename)
        path.rename(new_name)


#print(list(file_paths))

# for i in file_paths:
#     new_filename = f"new-{i.stem}{i.suffix}"
#     new_filepath = i.with_name(new_filename)
#     #i.rename(new_filepath)
#     print(new_filepath)
#
#
# # Ursprunglig sökväg
# path = Path("files/rocknroll.txt")
#
# # Byta ut filnamnet
# new_path = path.with_name("deathnroll.txt")
# path.rename(new_path)
# print(new_path)  # Output: /home/user/documents/new_file.txt