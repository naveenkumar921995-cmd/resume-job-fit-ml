import re

def extract_experience_years(text):
    """
    Extract years of experience from resume text.
    """
    pattern = r'(\d+)\+?\s*(years|yrs)'
    matches = re.findall(pattern, text.lower())

    if matches:
        years = max([int(match[0]) for match in matches])
        return years

    return 0
