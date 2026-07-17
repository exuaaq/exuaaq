from datetime import datetime
import os

def calculate_age(birth_date):
    now = datetime.now()
    # Calculate the time difference
    time_difference = now - birth_date
    
    # Convert total seconds alive into an exact decimal age
    # 365.2425 accounts for leap years accurately over time
    age = time_difference.total_seconds() / (365.2425 * 24 * 3600)
    return age

def generate_svg(age):
    # Format the age to 9 decimal places for that high-precision "uptime" look
    age_str = f"{age:.9f}"
    
    # This is your SVG template. You can customize the colors, text, or dark theme styles here!
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="320" height="20">
    <style>
        .label {{ font: bold 11px 'Segoe UI', Montserrat, sans-serif; fill: #fff; }}
        .value {{ font: 11px 'Segoe UI', Montserrat, sans-serif; fill: #00ff66; }}
    </style>
    <rect width="90" height="20" fill="#2d2d2d" rx="3" />
    <rect x="90" width="230" height="20" fill="#1e1e1e" rx="3" />
    <text x="10" y="14" class="label">🎂 Uptime</text>
    <text x="100" y="14" class="value">{age_str} years</text>
</svg>"""
    
    return svg_content

def main():
    # Your birthdate: July 24, 2003
    birth_date = datetime(2003, 7, 24, 0, 0, 0) 
    
    # Calculate current precision age
    current_age = calculate_age(birth_date)
    
    # Generate the fresh SVG code
    svg_code = generate_svg(current_age)
    
    # Save it to a file named profile-uptime.svg
    output_filename = "profile-uptime.svg"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    print(f"Successfully generated {output_filename} with age: {current_age:.9f}")

if __name__ == "__main__":
    main()
