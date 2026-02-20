import re

def extract_experience_years(text):
    matches = re.findall(r"\d+\+?\s+years", text.lower())
    if matches:
        return int(matches[0].split()[0])
    return 1

def keyword_density(resume_text, job_text):
    resume_words = resume_text.lower().split()
    job_words = job_text.lower().split()
    overlap = set(resume_words) & set(job_words)
    return round((len(overlap) / len(job_words)) * 100, 2) if job_words else 0
