import re

from app.services.lead_service import save_lead


def contact_flow(session, message):

    state = session["state"]

    message = message.strip()

    if state == "CONTACT_NAME":

        session["name"] = message

        session["state"] = "CONTACT_EMAIL"

        return {

            "message": "Please enter your Email Address.",

            "options": [],

            "state": "CONTACT_EMAIL",

            "input_type": "text"

        }

    elif state == "CONTACT_EMAIL":

        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.match(email_regex, message):

            return {

                "message": "Please enter a valid Email Address.",

                "options": [],

                "state": "CONTACT_EMAIL",

                "input_type": "text"

            }

        session["email"] = message

        session["state"] = "CONTACT_PHONE"

        return {

            "message": "Please enter your Phone Number.",

            "options": [],

            "state": "CONTACT_PHONE",

            "input_type": "text"

        }

    elif state == "CONTACT_PHONE":

        if not message.isdigit() or len(message) != 10:

            return {

                "message": "Please enter a valid 10-digit Phone Number.",

                "options": [],

                "state": "CONTACT_PHONE",

                "input_type": "text"

            }

        session["phone"] = message

        save_lead(

            session["name"],

            session["email"],

            session["phone"],

            session.get("service", "General Inquiry")

        )

        session["state"] = "MAIN_MENU"

        return {

            "message": (
                "✅ Thank you!\n\n"
                "Our team will contact you shortly."
            ),

            "options": [

                "Solutions",

                "Services",

                "Careers",

                "Support"

            ],

            "state": "MAIN_MENU",

            "input_type": "buttons"

        }