def support_flow(session, message=None):

    session["state"] = "MAIN_MENU"

    return {
        "message": (
            "Thank you for contacting F1 InfoTech Support.\n\n"
            "For the fastest assistance, please visit our Support Portal by clicking the button below."
        ),
        "redirect": {
            "text": "Open Support Portal",
            "url": "https://support.f1infotech.in/"
        },
        "options": [
            "Solutions",
            "Services",
            "Careers"
        ],
        "state": "MAIN_MENU",
        "input_type": "buttons"
    }