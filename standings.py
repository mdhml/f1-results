import pandas as pd
import datetime
import json


YEAR = datetime.datetime.now().year
df = pd.DataFrame(
    pd.read_html(f"https://www.formula1.com/en/results.html/{YEAR}/drivers.html")[0]
)
df = df[["Driver", "PTS", "Car"]]
# reverse the order
df = df.sort_values(by="PTS", ascending=True)

# in Driver column only keep the last 3 characters
df["Driver"] = df["Driver"].str[:-5]

# add colors to the dataframe
car_colors = {
            "Red Bull Racing": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine": "#f032e6",
            "Haas F1 Team": "#ffffff",
            "McLaren": "#f58231",
            "Alfa Romeo": "#800000",
            "AlphaTauri": "#dcbeff",
            "Williams": "#4363d8",
            "Red Bull Racing Honda RBPT": "#ffe119",
            "Aston Martin Aramco Mercedes": "#3cb44b",
            "Alpine Renault": "#f032e6",
            "Haas Ferrari": "#ffffff",
            "McLaren Mercedes": "#f58231",
            "Alfa Romeo Ferrari": "#800000",
            "AlphaTauri Honda RBPT": "#dcbeff",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6"
          }
df["fill"] = df["Car"].map(car_colors)

# remove rows where points is 0
df = df[df["PTS"] != 0]
df.reset_index(inplace=True, drop=True)
df.rename(columns={"PTS": "Points"}, inplace=True)

data = {"WDC": df.to_dict("records")}

with open('f1_results.json', 'w') as f:
    f.write(json.dumps(data))
