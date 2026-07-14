def get_in_touch_flow(session):

    session["state"] = "MAIN_MENU"

    return {
        "message": (
            "Thank you for your interest in F1 InfoTech.\n\n"
            "Our team would be happy to assist you. Please click the button below to visit our Get In Touch page and submit your enquiry."
        ),
        "redirect": {
            "text": "Get In Touch",
            "url": "/getintouch.html"
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