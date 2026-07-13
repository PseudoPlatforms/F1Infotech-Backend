from app.services.knowledge_base import (
    get_solution_categories,
    get_solutions_by_category,
    get_solution
)


def solutions_flow(session, message):

    state = session["state"]

    message = message.strip()

    # ------------------------------------
    # STEP 1 : Show Categories
    # ------------------------------------

    if state == "SOLUTIONS":

        categories = get_solution_categories()

        session["state"] = "SOLUTION_CATEGORY"

        return {

            "message": "Please choose a solution category.",

            "options": categories,

            "state": "SOLUTION_CATEGORY",

            "input_type": "buttons"

        }

    # ------------------------------------
    # STEP 2 : Show Solutions
    # ------------------------------------

    elif state == "SOLUTION_CATEGORY":

        session["category"] = message

        solutions = get_solutions_by_category(message)

        session["state"] = "SOLUTION_DETAILS"

        return {

            "message": f"{message} Solutions",

            "options": [item["name"] for item in solutions],

            "state": "SOLUTION_DETAILS",

            "input_type": "buttons"

        }

    # ------------------------------------
    # STEP 3 : Explain Solution
    # ------------------------------------

    elif state == "SOLUTION_DETAILS":

        solution = get_solution(message)

        if solution is None:

            return {

                "message": "Please choose a valid solution.",

                "options": [],

                "state": "SOLUTION_DETAILS",

                "input_type": "buttons"

            }

        session["selected_solution"] = solution["name"]

        session["state"] = "SOLUTION_CONTACT_CONFIRM"

        return {
    "message":
        f"<strong>{solution['name']}</strong><br><br>"
        f"{solution['description']}<br><br>"
        "Would you like to get in touch with our solution experts?",

    "redirect": {
        "text": "Get In Touch",
        "url": "http://127.0.0.1:5500/F1Infotech-/getintouch.html"
    },

    "options": [
        "Yes",
        "No"
    ],

    "state": "SOLUTION_CONTACT_CONFIRM",
    "input_type": "buttons"
}

    # ------------------------------------
    # STEP 4 : Contact Confirmation
    # ------------------------------------

    elif state == "SOLUTION_CONTACT_CONFIRM":

        if message.lower() == "yes":

            session["service"] = session["selected_solution"]

            session["state"] = "CONTACT_NAME"

            return {

                "message": "Great! Please enter your Name.",

                "options": [],

                "state": "CONTACT_NAME",

                "input_type": "text"

            }

        elif message.lower() == "no":

            session["state"] = "MAIN_MENU"

            return {

                "message": "No worries 😊 Is there anything else I can help you with?",

                "options": [

                    "Solutions",

                    "Services",

                    "Careers",

                    "Support"

                ],

                "state": "MAIN_MENU",

                "input_type": "buttons"

            }

        return {

            "message": "Please choose Yes or No.",

            "options": [

                "Yes",

                "No"

            ],

            "state": "SOLUTION_CONTACT_CONFIRM",

            "input_type": "buttons"

        }