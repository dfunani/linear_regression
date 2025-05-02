from types import NoneType
from typing import Any
from linear_regression.line import draw
from unittest.mock import patch

@patch("linear_regression.line.st.pyplot")
@patch("linear_regression.line.st.write")
@patch("linear_regression.line.st.subheader")
@patch("linear_regression.line.st.title")
def test_draw(mock_title: Any, mock_subheader: Any, mock_write: Any, mock_pyplot: Any) -> None:
    constant = 1.0
    gradient = 2.0
    points = [(1, 3), (2, 5), (3, 7)]

    # Call the draw function
    draw(constant, gradient, points)

    # Check if Streamlit functions were called
    mock_title.assert_called_once_with("Drawing a Line with Streamlit")
    mock_subheader.assert_any_call("Line Equation: y = 2.0x + 1.0")
    mock_write.assert_called_once_with(points)
    mock_pyplot.assert_called_once()