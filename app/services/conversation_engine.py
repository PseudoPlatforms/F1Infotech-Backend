from app.services.session_manager import get_session

from app.flows.welcome_flow import welcome_flow
from app.flows.main_menu_flow import main_menu_flow
from app.flows.services_flow import services_flow
from app.flows.contact_flow import contact_flow
from app.flows.careers_flow import careers_flow
from app.flows.solutions_flow import solutions_flow
from app.flows.support_flow import support_flow
from app.flows.get_in_touch_flow import get_in_touch_flow
from app.utils.intent_detector import is_get_in_touch_intent
def process_message(session_id, message):

    session = get_session(session_id)

    state = session["state"]
    if is_get_in_touch_intent(message):
        return get_in_touch_flow(session)
    if state == "WELCOME":
        return welcome_flow(session)

    elif state == "MAIN_MENU":
        return main_menu_flow(session, message)

    elif state in ["SERVICES", "SERVICE_DETAILS"]:
        return services_flow(session, message)

    elif state in ["CONTACT_NAME", "CONTACT_EMAIL", "CONTACT_PHONE"]:
        return contact_flow(session, message)
    elif state in ["CAREERS", "CAREERS_COMPLETE"]:
    

        return careers_flow(session, message)
    elif state == "SUPPORT":
        return support_flow(session)
    elif state in [

    "SOLUTIONS",

    "SOLUTION_CATEGORY",

    "SOLUTION_DETAILS",

    "SOLUTION_CONTACT_CONFIRM"

]:

        return solutions_flow(session, message)
    return {

        "message": "Something went wrong.",

        "options": [],

        "state": state,

        "input_type": "text"

    }