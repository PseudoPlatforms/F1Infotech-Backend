def careers_flow(session, message):

    message = message.strip().lower()
    state = session["state"]

    if state == "CAREERS":

        if message == "yes":

            session["state"] = "MAIN_MENU"

            return {
                "message": (
                    "Great! 🚀\n\n"
                    "Click the button below to explore our current career opportunities."
                ),
                "redirect": {
                    "text": "Open Careers Page",
                    "url": "http://127.0.0.1:5500/F1Infotech-/careers.html"
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

        elif message == "no":

            session["state"] = "MAIN_MENU"

            return {
                "message": (
                    "No worries 😊\n\n"
                    "Is there anything else I can help you with?"
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

        else:

            return {
                "message": "Please choose Yes or No.",
                "options": [
                    "Yes",
                    "No"
                ],
                "state": "CAREERS",
                "input_type": "buttons"
            }