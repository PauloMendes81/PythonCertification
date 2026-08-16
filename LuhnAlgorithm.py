def verify_card_number(card_number):
    """
    Verify if the provided card number is valid using the Luhn algorithm.

    Parameters:
    card_number (str): The credit card number as a string.

    Returns:
    str: "VALID!" if the card number is valid, "INVALID!" otherwise.
    """
    # Remove any spaces or hyphens from the card number
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if the card number consists only of digits
    if not card_number.isdigit():
        return "INVALID!"

    # Convert the card number into a list of integers
    digits = [int(d) for d in card_number]
    
    # Reverse the digits for processing
    digits.reverse()
    
    # Apply the Luhn algorithm
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Calculate the sum of all digits
    total_sum = sum(digits)
    
    # A valid card number will have a total sum that is a multiple of 10
    return "VALID!" if total_sum % 10 == 0 else "INVALID!"

verify_card_number('4111-1111-1111-1111')
verify_card_number('453914881')
verify_card_number('1234 5678 9012 3456')