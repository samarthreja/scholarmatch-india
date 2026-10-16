
from scholarships import find_eligible_scholarships


def test_eligible_scholarship():
    result = find_eligible_scholarships(
        70, 200000, "Undergraduate"
    )

    assert len(result) == 1
    assert result[0]["name"] == "Scholarship Demo C"


def test_no_eligible_scholarships():
    result = find_eligible_scholarships(
        50, 100000, "Undergraduate"
    )

    assert len(result) == 0


def test_income_exceeds_limit():
    result = find_eligible_scholarships(
        90, 600000, "Undergraduate"
    )

    assert len(result) == 0
