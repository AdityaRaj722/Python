# convert the following into json fromat
import json

# student_data={"name":"Aditya","age":21,"marks":93}
# print(student_data)
# print(type(student_data))
# data=json.dumps(student_data)
# print(data)
# print(type(data))

# access the vlaue age from given data
# student_data="""{"name":"Aditya","age":21,"marks":93}"""
# data=json.loads(student_data)
# print(data["age"])

# pretty print data
# student_data={"name":"Aditya","age":21,"marks":93}
# data=json.dumps(student_data,indent=4,separators=(",","="))
# print(data)

# sort  json keys
# student_data={"name":"Aditya","age":21,"marks":93}
# f=open("demo.json","w")
# data=json.dumps(student_data,indent=4,sort_keys=True)
# f.write(data)
# print("the data has been written in the file")

# access the nested key "marks from dtata
# student_data = """{
#     "student": {
#         "grade": {
#             "name": "David",
#             "marks": {
#                 "maths": 87
#             }
#         }
#     }
# }"""
# data=json.loads(student_data)
# print(data["student"]["grade"]["marks"]["maths"])

# access the key marks
student_data="""{"student":
                  {"grade":
                       {"name":"David","marks":93}}}"""

data=json.loads(student_data)
print(data["student"]["grade"]["marks"])