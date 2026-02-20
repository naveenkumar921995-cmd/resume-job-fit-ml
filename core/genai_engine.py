def generate_feedback(fit_score):
    if fit_score > 85:
        return "Excellent alignment. Focus on refining leadership highlights."
    elif fit_score > 70:
        return "Good match. Improve quantified achievements."
    else:
        return "Consider adding relevant skills and measurable outcomes."
