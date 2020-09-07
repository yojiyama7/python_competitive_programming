import os
import requests
import re

# Atcoder Problems API
all_contests_url = "https://kenkoooo.com/atcoder/resources/contests.json"
all_contests = requests.get(all_contests_url).json()
all_ploblems_url = "https://kenkoooo.com/atcoder/resources/merged-problems.json"
all_problems = requests.get(all_ploblems_url).json()

current_path = os.getcwd()

# O(N)
def search_contest_by(contest_id):
    for contest in all_contests:
        if contest["id"] == contest_id:
            return contest
def search_problems_by(contest_id):
    for problem in all_problems:
        if problem["contest_id"] == contest_id:
            yield problem

# Normalize
def name_from(contest_id):
    pattern = r"[A-Za-z]+|[0-9]+"
    parts = re.findall(pattern, contest_id)
    parts = [p.lower() for p in parts]
    name = "_".join(parts)
    # print(name, r_i["id"], parts)
    return name

def make_folder_file(folder_name, file_names):
    p = os.path.join(current_path, folder_name)
    if os.path.exists(p) == False:
        os.mkdir(p)
    # print(file_names)
    for file_name in file_names:
        p = os.path.join(current_path, folder_name, file_name+".py")
        if os.path.exists(p):
            continue
        with open(p, "w+", encoding="utf-8") as f:
            # f.write()
            pass
    

# for contest in contests:
#     # if r_i["id"][:3] == "abc":
#     name = folder_name_from(contest["id"])

input_text = input("contest url: ")

match_obj = re.search(r"(?:^https://)?atcoder.jp/contests/([^/]+)(?:/.+)?", input_text)
if match_obj:
    # print(type(match_obj.group(1)))
    contest_id = match_obj.group(1)
    contest = search_contest_by(contest_id)
    contest_name = name_from(contest["id"])
    problems = list(search_problems_by(contest_id))
    problem_names = [name_from(p["title"]) for p in problems]
    print(contest_name)
    for p in problem_names:
        print(p)
    make_folder_file(contest_name, problem_names)
else:
    print(">>> It is invalid url.")