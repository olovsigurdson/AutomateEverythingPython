from pathlib import Path
import zipfile

filepath = Path('files')

# Ändra suffix på filer
# for path in filepath.glob("**/*"):
#
#     if path.is_file():
#         #new_filename = path.stem + '.csv'
#         #new_name = path.with_name(new_filename)
#         new_name = path.with_suffix('.csv')
#         path.rename(new_name)


for i in range(10, 21):
    filename = str(i) + '.txt'
    file_path = filepath / Path(filename)
    file_path.touch()

archive_path = filepath / Path("archive.zip")

with zipfile.ZipFile(archive_path, mode="w") as zf:
    for path in filepath.glob("*.txt"):
        zf.write(path)
        path.unlink()

root_dir = Path('files')
dest_path = Path('files/2021')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, mode='r') as zf:
        final_path = dest_path / Path(path.stem)
        zf.extractall(final_path)