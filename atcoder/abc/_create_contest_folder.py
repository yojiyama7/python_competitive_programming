import os
import requests
import re

CONTEST_URL_PATTERN = r"(?:^https://)?atcoder.jp/contests/([^/]+)(?:/.+)?"
STANDARD_PROBLEM_NUM = 8

# Atcoder Problems API
ALL_CONTEST_URL = "https://kenkoooo.com/atcoder/resources/contests.json"
ALL_PROBLEMS_URL = "https://kenkoooo.com/atcoder/resources/merged-problems.json"
all_contests = requests.get(ALL_CONTEST_URL).json()
all_problems = requests.get(ALL_PROBLEMS_URL).json()

# all_contests_by_contest_id = dict([(contest["id"], contest) for contest in all_contests])
all_problems_by_contest_id = dict()
for problem in all_problems:
    contest_id = problem["contest_id"]
    if contest_id not in all_problems_by_contest_id:
        all_problems_by_contest_id[contest_id] = []
    all_problems_by_contest_id[contest_id].append(problem)

current_path = os.getcwd()

def main():
    input_text = input("contest url: ")
    # if input_text == "":
    #     input_text = input("rename contest files? (Y/n): ")
    #     if re.match(r"^([yY](es)?)?$", input_text):
    #         rename_contest_files()
    if check_if_valid_url(input_text):
        if is_already_exists(input_text):
            print("rename")
            rename_contest_files(input_text)
        else:
            print("create")
            create_contest_folder(input_text)
    else:
        print("This url is invalid.")

def check_if_valid_url(url):
    if re.search(CONTEST_URL_PATTERN, url):
        return True
    else:
        return False

def convert_url_to_contest_id(url):
    match_obj = re.search(CONTEST_URL_PATTERN, url)
    if match_obj:
        contest_id = match_obj.group(1)
        return contest_id
    return None

def is_already_exists(url):
    contest_id = convert_url_to_contest_id(url)
    contest_name = convert_id_to_name(contest_id)
    contest_path = os.path.join(current_path, contest_name)
    is_exist = os.path.isdir(contest_path)
    print(is_exist, contest_path)
    return is_exist

def convert_id_to_name(contest_id):
    pattern = r"[A-Za-z]+|[0-9]+"
    parts = re.findall(pattern, contest_id)
    parts = [p.lower() for p in parts]
    name = "_".join(parts)
    # print(name, r_i["id"], parts)
    return name

def rename_contest_files(url):
    contest_id = convert_url_to_contest_id(url)
    contest_name = convert_id_to_name(contest_id)
    folder_path = os.path.join(current_path, contest_name)
    # print(all_problems_by_contest_id[contest_id])
    for problem in all_problems_by_contest_id[contest_id]:
        problem_title = problem["title"]
        print(problem_title)
        problem_name = convert_id_to_name(problem_title)
        problem_old_file_path = os.path.join(folder_path, f"{problem_name[:2]}.py")
        problem_new_file_path = os.path.join(folder_path, f"{problem_name}.py")
        if os.path.isfile(problem_old_file_path):
            os.rename(problem_old_file_path, problem_new_file_path)

def create_contest_folder(url):
    contest_id = convert_url_to_contest_id(url)
    contest_name = convert_id_to_name(contest_id)
    os.mkdir(os.path.join(current_path, contest_name))
    create_contest_files(url)

def create_contest_files(url):
    contest_id = convert_url_to_contest_id(url)
    contest_name = convert_id_to_name(contest_id)
    folder_path = os.path.join(current_path, contest_name)
    if contest_id in all_problems_by_contest_id:
        problems = all_problems_by_contest_id[contest_id]
        for problem in problems:
            problem_title = problem["title"]
            print(problem_title)
            problem_name = convert_id_to_name(problem_title)
            problem_file_path = os.path.join(folder_path, f"{problem_name}.py")
            with open(problem_file_path, "w", encoding="utf-8") as f:
                pass
    else:
        problem_names = [f"{chr(97+i)}_" for i in range(STANDARD_PROBLEM_NUM)]
        for problem_name in problem_names:
            problem_file_path = os.path.join(folder_path, f"{problem_name}.py")
            with open(problem_file_path, "w", encoding="utf-8") as f:
                pass
if __name__ == "__main__":
    main()