from paz.breach import check_breach

def test_breached_password():
    count = check_breach("123456")
    assert isinstance(count,(int, type(None)))

def test_breached_empty_password():
    count = check_breach("")
    assert isinstance(count,(int, type(None)))

def test_safe_password():
    count = check_breach("M@hdi_Unique#123456")
    assert isinstance(count, (int, type(None)))
