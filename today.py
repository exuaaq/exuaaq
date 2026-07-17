import datetime
from lxml import etree

def daily_readme(birthday):
    """
    Returns the exact age formatted to 9 decimal places
    """
    now = datetime.datetime.today()
    time_difference = now - birthday
    # 365.2425 accounts for leap years accurately over time
    age = time_difference.total_seconds() / (365.2425 * 24 * 3600)
    return f"{age:.9f} years"

def justify_format(root, element_id, new_text, length=0):
    """
    Updates the text of the element, and modifies the dots to keep alignment
    """
    new_text = str(new_text)
    find_and_replace(root, element_id, new_text)
    
    # Calculate how many dots we need to keep the alignment perfect
    just_len = max(0, length - len(new_text))
    if just_len <= 2:
        dot_map = {0: '', 1: ' ', 2: '. '}
        dot_string = dot_map[just_len]
    else:
        dot_string = ' ' + ('.' * just_len) + ' '
    
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
    Parses the SVG and replaces the Loading text with your real uptime age
    """
    try:
        parser = etree.XMLParser(remove_blank_text=False)
        tree = etree.parse(filename, parser)
        root = tree.getroot()
        
        # Updates the uptime string and balances it against 20 dot slots
        justify_format(root, 'uptime_data', age_data, 20)
        
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"Successfully updated {filename}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")

if __name__ == '__main__':
    # Your birthdate: July 24, 2003
    birth_date = datetime.datetime(2003, 7, 24, 0, 0, 0)
    
    # Calculate precision uptime age
    age_str = daily_readme(birth_date)
    
    # Update both layout SVGs natively
    svg_overwrite('dark_mode.svg', age_str)
    svg_overwrite('light_mode.svg', age_str)
