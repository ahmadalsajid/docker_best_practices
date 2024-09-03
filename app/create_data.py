import requests
import random
import json
from faker import Faker

fake = Faker()
available_courses = ['BBA', 'English', 'Architecture', 'CSE']
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
for _ in range(1000):
    f_name = fake.first_name()
    l_name = fake.last_name()
    email = f"{f_name.lower()}_{l_name.lower()}@{fake.domain_name()}"
    cgpa = round(random.uniform(2.5, 4), 2)

    _data = {
        "course": ", ".join(random.choices(available_courses, k=2)),
        "email": email,
        "gpa": cgpa,
        "name": f"{f_name} {l_name}"
    }
    # print(json.dumps(_data))

    r = requests.post(url='http://localhost:1337/students/', data=json.dumps(_data), headers=headers)
    print(r.text)
