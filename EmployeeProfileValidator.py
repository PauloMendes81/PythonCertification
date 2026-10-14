email = 'alice.johnson@company.com'
print(f'Email: {email}')

# find() returns the index of the first match, or -1 if it is not present.
at_position = email.find('@')
print(f'Position of @: {at_position}')

# The end index is excluded, so this keeps only the text before '@'.
username = email[:at_position]
print(f'Username: {username}')

# The in operator produces a boolean indicating whether the text is present.
has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

# strip() removes whitespace at the ends; title() capitalizes each word.
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
# strip() removes surrounding spaces, and lower() converts letters to lowercase.
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

# Convert the cleaned name to an uppercase badge label.
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')
# Reuse the separator index to extract the email's local part.
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

# Replace dots with spaces before formatting the name for display.
display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

phone = '123-456-7890'
# replace() returns a new string with every dash removed.
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

full_address = '123 Main Street, Springfield, IL'
# split() creates a list at each delimiter; join() combines its items again.
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

employee_code = 'EMP-2024-SD'
# These methods check the start and end of a string without changing it.
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

# count() returns the number of occurrences of the requested character.
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

print(f"Dots in email: {dot_count}")
print(f"Dashes in code: {dash_count}")