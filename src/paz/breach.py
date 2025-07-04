from pyhibp import pwnedpasswords, set_user_agent

set_user_agent("password-analyzer-cli (contact: mirshafieemahdi001@gmail.com)")

def check_breach(password: str) -> int | None:
    """
    Checks if the password has been breached using Have I Been Pwned API.
    Returns:
        - Number of times password has appeared in breaches
        - None if API/network failed
    """
    try:
        result = pwnedpasswords.is_password_breached(password)
        return result or 0
    except Exception:
        return None  