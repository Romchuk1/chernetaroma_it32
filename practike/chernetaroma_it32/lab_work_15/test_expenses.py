
from pathlib import Path

import pytest

from expenses import parse_line, total_by_category, load_expenses

def test_parse_line_valid():
    result = parse_line("2026-11-01;food;150.00;products")

    assert result == {
        "date": "2026-11-01",
        "category": "food",
        "amount": 150.0,
        "comment": "products"
    }

def test_parse_line_amount():
    result = parse_line("2026-11-02;transport;50.00;bus")

    assert result["amount"] == 50.0

def test_parse_line_category():
    result = parse_line("2026-11-03;food;200.00;lunch")

    assert result["category"] == "food"

def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-11-01;food;150.00")

def test_parse_line_wrong_amount():
    with pytest.raises(ValueError):
        parse_line("2026-11-01;food;abc;products")

@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-11-01;food;150.00;products", "food", 150.0),
        ("2026-11-02;transport;50.00;bus", "transport", 50.0),
        ("2026-11-03;food;200.00;lunch", "food", 200.0),
        ("2026-11-04;fun;120.00;cinema", "fun", 120.0),
        ("2026-11-05;transport;40.00;bus", "transport", 40.0),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    result = parse_line(line)

    assert result["category"] == expected_category
    assert result["amount"] == expected_amount

def test_total_by_category_tmp_path(tmp_path):
    file_path = tmp_path / "expenses.csv"

    file_path.write_text(
        "date;category;amount;note\n"
        "2026-11-01;food;40.00;products\n"
        "2026-11-02;food;60.00;lunch\n",
        encoding="utf-8"
    )

    records = load_expenses(file_path)

    assert total_by_category(records) == {"food": 100.0}

def test_total_by_category_real_csv():
    path = Path(__file__).parent / "data" / "expenses.csv"

    records = load_expenses(path)

    assert total_by_category(records) == {
        "food": 530.0,
        "transport": 90.0,
        "fun": 370.0
    }