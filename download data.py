import requests

period = int(input("Välj 2008 eller 2007"))

url = f'https://www.stats.govt.nz/assets/Uploads/Annual-balance-sheets/Annual-balance-sheets-2022-provisional/Downloads/Accumulation-accounts-{period}-2022-provisional.csv'
print(url)

#content funkar för både binary och non-binary. Typ musik också
contents = requests.get(url).content
print(contents)

with open(f"finance{period}.txt", "wb") as file_temp:
    file_temp.write(contents)
