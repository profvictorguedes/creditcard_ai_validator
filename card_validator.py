import re


def detect_credit_card_info(text_lines):
    card_number_pattern = r"\b(?:\d[ -]*?){13,16}\b"
    expiry_pattern = r"(0[1-9]|1[0-2])\/?([0-9]{2})"

    card_number = None
    expiry_date = None
    card_name = None

    for line in text_lines:
        if not card_number:
            match = re.search(card_number_pattern, line)
            if match:
                card_number = match.group()

        if not expiry_date:
            match = re.search(expiry_pattern, line)
            if match:
                expiry_date = match.group()

        if not card_name and line.isupper() and len(line.split()) >= 2:
            card_name = line

    if card_number:
        return {
            "card_name": card_name,
            "bank_name": "Bank not identifiable",
            "expiry_date": expiry_date
        }

    return None
