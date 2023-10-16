def validate_property_code(property_code):
    return len(property_code) == 10

def validate_cleaning_fee(cleaning_fee):
    return cleaning_fee >= 0