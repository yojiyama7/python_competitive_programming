import requests
import re

all_contests_url = "https://kenkoooo.com/atcoder/resources/contests.json"
all_contests = requests.get(all_contests_url).json()
all_ploblems_url = "https://kenkoooo.com/atcoder/resources/merged-problems.json"
all_problems = requests.get(all_ploblems_url).json()
def search_contest_by(contest_id):
    for contest in all_contests:
        if contest["id"] == contest_id:
            return contest
def search_problems_by(contest_id):
    for problem in all_problems:
        if problem["contest_id"] == contest_id:
            yield problem

def folder_name_from(contest_id):
    pattern = r"[A-Za-z]+|[0-9]+"
    parts = re.findall(pattern, contest_id)
    parts = [p.lower() for p in parts]
    name = "_".join(parts)
    # print(name, r_i["id"], parts)
    return name

# for contest in contests:
#     # if r_i["id"][:3] == "abc":
#     name = folder_name_from(contest["id"])

input_text = input("contest url: ")

match_obj = re.search(r"(?:^https://)?atcoder.jp/contests/([^/]+)(?:/.+)?", input_text)
if match_obj:
    # print(type(match_obj.group(1)))
    contest_id = match_obj.group(1)
    contest = search_contest_by(contest_id)
    problems = list(search_problems_by(contest_id))
    print(contest)
    [print(p) for p in problems]
else:
    print(">>> It is invalid url.")