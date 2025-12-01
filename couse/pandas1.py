import random
import random

import pandas as pd
s=pd.Series(["Hello","namasteJii",101,102,23.5],index=["a","b","c","d","e"])
print(s)

d={
    "Name":"Shrinath Rajput",
    "education":"I was completed diploma is CSE and now i am aiml student",
    "Idea":"Virat kohli",
    "dream":"become a good job in MNC company"
}
s1=pd.Series(d)
print(s1)

k1={
    "pattankodoli":100,
    "kolhpur":1500,
    "lanodn":2000,
    "mumbai":3000,
    "pune":500
}
s2=pd.Series(k1)
s2[s2<200]=500
print(s2)

