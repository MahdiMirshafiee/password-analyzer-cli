import re

COMMON_PASSWORDS = {"password", "123456", "qwerty", "111111", "letmein"}

def score_password(password: str) -> tuple[str, int]:
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if password.lower() in COMMON_PASSWORDS:
        score -= 2

    if score <= 1:
        return "Weak", score
    elif score <= 3:
        return "Medium", score
    else:
        return "Strong", score