from zxcvbn import zxcvbn


def password_strength(password):
    results = zxcvbn(password)
    # Score is a rough estimate of the password's complexity as zxcvbn sees it. 0 is worst, 4 is best
    score = results.get('score')
    messages = results.get('feedback')
    warning, suggestions = messages.get('warning'), messages.get('suggestions')

    return score, warning, suggestions


password = "you"
score, warning, suggestions = password_strength(password)

print(f"Score: {score}, Warning: {warning}, Suggestions: {suggestions}")
