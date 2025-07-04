from paz.strength import score_password

def test_very_weak_password():
    label, score = score_password("123")
    assert label == "Weak"
    assert score <= 1

def test_common_password():
    label, score = score_password("password")
    assert label == "Weak"
    assert score <= 1

def test_medium_password():
    label, score = score_password("mahdi123") 
    assert label == "Medium"
    assert score == 3

def test_strong_password_uppercase():
    label, score = score_password("Mahdi123")
    assert label == "Strong"

def test_strong_password():
    label, score = score_password("M@hd1_998877abc")
    assert label == "Strong"
    assert score >= 5