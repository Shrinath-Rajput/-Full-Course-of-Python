"""dic={
    "name":"shrinath",
    "cgpa":9.6,
    "marks":[98,99,96,98],
}
dic["key"]="gopal"
print(dic)"""


#nested dictinoary

student={
    "name":"Shri",
    "cgpa":9.8,
    "marks":{
        "maths":98,
        "science":99,
        "CS":88,
    }
}
print(student)
student["marks"]["maths"]