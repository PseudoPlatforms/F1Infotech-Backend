import re


def is_get_in_touch_intent(message: str) -> bool:
    """
    Returns True if the user is trying to contact F1 InfoTech.
    """

    message = message.lower().strip()

    patterns = [

        r"\bget in touch\b",
        r"\bcontact\b",
        r"\bcontact us\b",
        r"\breach (out|you)\b",
        r"\bconnect\b",
        r"\bcall me\b",
        r"\bcall us\b",
        r"\btalk to\b",
        r"\bspeak to\b",
        r"\bexpert\b",
        r"\bsales\b",
        r"\benquiry\b",
        r"\binquiry\b",
        r"\bdemo\b",
        r"\bquotation\b",
        r"\bquote\b",
        r"\bpricing\b",
        r"\bproject\b",
        r"\bconsultation\b",
        r"\bbook (a )?(meeting|call)\b",
        r"\binterested\b",
        r"\bneed help\b",
        r"\bneed assistance\b",
        r"\bwant to discuss\b",
        r"\bcan someone contact me\b",
        r"\bhow can i contact\b",
        r"\bhow do i contact\b",
        r"\bhow can i reach\b",
        r"\bhow do i reach\b",
    ]

    return any(re.search(pattern, message) for pattern in patterns)