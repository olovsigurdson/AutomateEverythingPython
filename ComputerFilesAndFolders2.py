from pathlib import Path
from datetime import datetime

# p = Path('files/2021/December/test1.txt')
# created_time = p.stat()
# date_createdtime = datetime.fromtimestamp(created_time.st_ctime)
# datetime_str = date_createdtime.strftime("%Y%m%d_%H%M%S")
# new_filename = datetime_str + '-' + p.name
# new_name = p.with_name(new_filename)
# p.rename(new_name)

root_dir = Path('files')
file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        created_time = path.stat()
        date_createdtime = datetime.fromtimestamp(created_time.st_ctime)
        datetime_str = date_createdtime.strftime("%Y%m%d_%H%M%S")

        new_filename = datetime_str + '-' + path.name
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