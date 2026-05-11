from main import calculate_tip


def test_basic_tip():
    result = calculate_tip(100, 20)
    assert result["tip"] == 20.0
    assert result["total"] == 120.0
    assert result["per_person"] == 120.0


def test_split_bill():
    result = calculate_tip(100, 20, people=4)
    assert result["per_person"] == 30.0


def test_zero_tip():
    result = calculate_tip(50, 0)
    assert result["tip"] == 0.0
    assert result["total"] == 50.0
