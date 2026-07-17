import datetime
from lxml import etree

def daily_readme(birthday):
    """
    Calculates the exact breakdown of years, months, and days
    """
    now = datetime.datetime.today()
    
    years = now.year - birthday.year
    months = now.month - birthday.month
    days = now.day - birthday.day
    
    # Handle day overflow
    if days < 0:
        months -= 1
        # Find out how many days were in the previous month
        prev_month = now.month - 1 if now.month > 1 else 12
        prev_year = now.year if now.month > 1 else now.year - 1
        
        if prev_month in [1, 3, 5, 7, 8, 10, 12]:
            days_in_prev = 31
        elif prev_month in [4, 6, 9, 11]:
            days_in_prev = 30
        else: # February leap year check
            is_leap = (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0)
            days_in_prev = 29 if is_leap else 28
            
        days += days_in_prev
        
    # Handle month overflow
    if months < 0:
        years -= 1
        months += 12
        
    return f"{years} years, {months} months, {days} days"

def justify_format(root, element_id, new_text, length=49):
    """
    Updates the text of the element, and modifies the dots to keep alignment
    """
    new_text = str(new_text)
    find_and_replace(root, element_id, new_text)
    
    # Calculate how many dots we need to keep the alignment perfect
    just_len = max(0, length - len(new_text))
    
    # Pad cleanly with spaces on either side of the dots
    dot_string = f" {'.' * just_len} "
    
    find_and_replace(root, f"{element_id}_dots", dot_string)

def find_and_replace(root, element_id, new_text):
    """
    Finds the element in the SVG file and replaces its text
    """
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = new_text

def svg_overwrite(filename, age_data):
    """
    Parses the SVG and replaces the text
    """
    try:
        parser = etree.XMLParser(remove_blank_text=False)
        tree = etree.parse(filename, parser)
        root = tree.getroot()
        
        # Updates the uptime string and balances it against 49 total slots
        justify_format(root, 'uptime_data', age_data, 49)
        
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"Successfully updated {filename}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")

if __name__ == '__main__':
    # Your birthdate: July 24, 2003
    birth_date = datetime.datetime(2003, 7, 24, 0, 0, 0)
    
    # Calculate structural uptime string
    age_str = daily_readme(birth_date)
    
    # Update both layout SVGs natively
    svg_overwrite('dark_mode.svg', age_str)
    svg_overwrite('light_mode.svg', age_str)
