import pandas
import pandas as pd

data={
    "student":["shrinath","Virat","rohit","dhoni","ruturaj"],
    "cities":["pune","dehli","nashik","kop","-hupari"],
    "maths":[98,99,100,98,99],
    "sports":["cricket","khokho","football","volleyball","cricket"]
}
student=pd.DataFrame(data,columns=["student","cities","maths","sports"])
print(student)
