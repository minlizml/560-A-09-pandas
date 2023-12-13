# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player={"Last Name": ["Bacot","Davis","Cadeau","Wojcik","Farris","Lebo","Landry","Okonkwo","Ingram","Trimble"],
        "First Name":["Armando","RJ","Elliot","Paxson","Duwe","Creighton","Rob","James","Harrison","Seth"],
        "height":[83,72,73,65,67,61,64,68,67,63],
        "weight":[240,180,180,195,210,180,190,240,235,195]}

data=pd.DataFrame(player)

#bmi = weight in kg/ height in meters squared
data["bmi"]=(data["weight"]/2.205)/((data["height"]/39.37)**2)

data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")

