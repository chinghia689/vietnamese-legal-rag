import pytest

from rag.graph import classify_input


@pytest.mark.parametrize(
    ("question", "expected"),
    [
        ("Xin chào", "greeting"),
        ("Bạn là ai?", "identity"),
        ("Cảm ơn", "thanks"),
        ("Hướng dẫn", "help"),
        ("Điều 8 Luật An ninh mạng quy định gì?", "legal_question"),
    ],
)
def test_classify_input_routes_common_inputs(question: str, expected: str) -> None:
    assert classify_input(question) == expected
