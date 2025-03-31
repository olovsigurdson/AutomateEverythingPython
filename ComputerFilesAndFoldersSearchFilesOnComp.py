from pathlib import Path
from datetime import datetime

root_dir = Path('files')
file_paths = root_dir.glob("**/*")

searched_string = "2"

for path in file_paths:
    if path.is_file():
        if searched_string.lower() in path.stem.lower():
            print(path.absolute())


