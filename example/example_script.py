from cheminot import CheminotSession
from dotenv import dotenv_values
import json

config = dotenv_values()

def get_courses():
    with open("courses.json", "r") as file:
        return json.load(file)
    
def print_res(res):
    try:
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
    except:
        print(res.status_code)
        print(res.headers)
        print(res.text)

print("Initiating Cheminot session...")
cheminot = CheminotSession(
    config["AUTH_TOKEN"],
    config["USER_AGENT"],
    config["STUDENT_ID"],
    config["PROGRAM_ID"],
    config["SEMESTER_ID"],
    "https://cheminotn.etsmtl.ca"
)

print("Fetching courses...")
courses = get_courses()

print("Registering to courses...")
for x in courses:
    res = cheminot.register_to_course(x["course_id"], x["group_number"], x["concentration"])
    print_res(res)

print("Confirming schedule...")
res = cheminot.confirm_schedule()
print_res(res)
