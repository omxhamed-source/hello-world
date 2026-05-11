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


def test_round_up_per_person():
    # $100 + 18% tip = $118 / 3 = $39.333... -> rounds up to $39.34
    result = calculate_tip(100, 18, people=3, round_up=True)
    assert result["per_person"] == 39.34
