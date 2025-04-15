import pandas
url = "https://docs.google.com/spreadsheets/d/1SPRn475iIWIPP85NFV50nMBjvDKni6bq1RLuE2LyF1A/gviz/tq?tqx=out:csv&sheet=Sekretariat"
data = pandas.read_csv(url)

print(data)