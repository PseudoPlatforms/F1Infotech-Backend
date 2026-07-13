sessions = {}


def get_session(session_id):

    if session_id not in sessions:

        sessions[session_id] = {

            "state": "WELCOME",

            "selected_service": None,

            "contact": {

                "name": "",

                "email": "",

                "phone": ""

            }

        }

    return sessions[session_id]