from app.services.knowledge_base import get_services, get_service_by_name
from app.flows.main_menu_flow import main_menu_flow
from app.flows.support_flow import support_flow


def services_flow(session, message):

    state = session["state"]
    message = message.strip()

    if state == "SERVICES":

        service = get_service_by_name(message)

        if service:

            session["selected_service"] = service["name"]
            session["state"] = "SERVICE_DETAILS"

            return {
                "message": f"📌 {service['name']}\n\n{service['description']}",
                "options": [
                    "Get In Touch",
                    "Solutions",
                    "Services",
                    "Careers",
                    "Support"
                ],
                "state": "SERVICE_DETAILS",
                "input_type": "buttons"
            }

        return {
            "message": "Please choose a valid service.",
            "options": [s["name"] for s in get_services()],
            "state": "SERVICES",
            "input_type": "buttons"
        }

    elif state == "SERVICE_DETAILS":

        # -------------------------
        # Get In Touch
        # -------------------------
        if message.lower() == "get in touch":

            session["state"] = "MAIN_MENU"

            return {
                "message": (
                    "Thank you for your interest in F1 InfoTech.\n\n"
                    "To connect with our team, please click the button below to visit our Get In Touch page."
                ),
                "redirect": {
                    "text": "Get In Touch",
                    "url": "http://127.0.0.1:5500/F1Infotech-/getintouch.html"
                },
                "options": [
                    "Solutions",
                    "Services",
                    "Careers",
                    "Support"
                ],
                "state": "MAIN_MENU",
                "input_type": "buttons"
            }

        # -------------------------
        # Services
        # -------------------------
        elif message.lower() == "services":

            session["state"] = "SERVICES"

            return {
                "message": "Please choose a service.",
                "options": [s["name"] for s in get_services()],
                "state": "SERVICES",
                "input_type": "buttons"
            }

        # -------------------------
        # Solutions / Careers
        # -------------------------
        elif message.lower() in ["solutions", "careers"]:

            session["state"] = "MAIN_MENU"
            return main_menu_flow(session, message)

        # -------------------------
        # Support
        # -------------------------
        elif message.lower() == "support":

            session["state"] = "SUPPORT"
            return support_flow(session)

        # -------------------------
        # Invalid Option
        # -------------------------
        return {
            "message": "Please choose one of the available options.",
            "options": [
                "Get In Touch",
                "Solutions",
                "Services",
                "Careers",
                "Support"
            ],
            "state": "SERVICE_DETAILS",
            "input_type": "buttons"
        }