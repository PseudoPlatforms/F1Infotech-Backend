def welcome_flow(session):

    session["state"] = "MAIN_MENU"

    return {
        "message": " Hi! Welcome to F1 InfoTech.\n\nHow can I help you today?",
        "options": [
            "Solutions",
            "Services",
            "Careers",
            "Support"
        ],
        "state": "MAIN_MENU",
        "input_type": "buttons"
    }