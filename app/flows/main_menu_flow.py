from app.services.knowledge_base import get_services
from app.services.knowledge_base import get_solution_categories
from app.flows.support_flow import support_flow

def main_menu_flow(session, message):

    message = message.strip().lower()

    if message == "services":

        session["state"] = "SERVICES"

        services = get_services()

        return {
            "message": "We provide the following services. Please choose one.",
            "options": [service["name"] for service in services],
            "state": "SERVICES",
            "input_type": "buttons"
        }

    elif message == "solutions":

        session["state"] = "SOLUTION_CATEGORY"

        return {
            "message": "Please choose a solution category.",
            "options": get_solution_categories(),
            "state": "SOLUTION_CATEGORY",
            "input_type": "buttons"
        }

    elif message == "careers":

        session["state"] = "CAREERS"

        return {
            "message": "Looking for opportunities at F1 InfoTech?",
            "options": [
                "Yes",
                "No"
            ],
            "state": "CAREERS",
            "input_type": "buttons"
        }

    elif message.lower() == "support":
        session["state"] = "SUPPORT"
        return support_flow(session)
    else:

        return {
            "message": "I'm here to help with F1 InfoTech related questions.",
            "options": [
                "Solutions",
                "Services",
                "Careers",
                "Support"
            ],
            "state": "MAIN_MENU",
            "input_type": "buttons"
        }