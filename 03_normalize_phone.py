#------------------------------------------------------------------------------
# Приймає: рядок з телефонним номером у будь-якому-форматі
# Повертає: '+38XXXYYYYYYY'
# Якщо немає "+" або міжнародного коду "+38", він додається
#------------------------------------------------------------------------------
def normalize_phone(phone_number):
    import re
    phone = re.sub(r"\D", "", phone_number)
    pattern = r"(?:\+38)?(?:38)?(\d{3})(\d{3})(\d{4})"
    replacement = r"+38(\1)\2-\3"
    try:
        formatted = re.sub(pattern, replacement, phone)
        if len(formatted) != 16:
            return "Not a phone number"
    except ValueError:
        return "Not a phone number"
    return formatted
        
print(normalize_phone("0505646374"))
