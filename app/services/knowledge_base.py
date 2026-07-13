import json
from pathlib import Path
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SOLUTION_FILE = os.path.join(BASE_DIR, "data", "solutions.json")


def get_solution_categories():

    with open(SOLUTION_FILE, encoding="utf-8") as f:

        data = json.load(f)

    return [item["category"] for item in data]


def get_solutions_by_category(category):

    with open(SOLUTION_FILE, encoding="utf-8") as f:

        data = json.load(f)

    for item in data:

        if item["category"].lower() == category.lower():

            return item["solutions"]

    return []


def get_solution(name):

    with open(SOLUTION_FILE, encoding="utf-8") as f:

        data = json.load(f)

    for category in data:

        for solution in category["solutions"]:

            if solution["name"].lower() == name.lower():

                return solution

    return None
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CAREER_FILE = os.path.join(BASE_DIR, "data", "careers.json")


def get_careers():

    with open(CAREER_FILE, "r", encoding="utf-8") as file:

        return json.load(file)
DATA_PATH = Path(__file__).parent.parent / "data" / "services.json"


def get_services():

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_service_by_name(name):

    services = get_services()

    for service in services:

        if service["name"].lower() == name.lower():
            return service

    return None