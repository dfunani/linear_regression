from ..app import (
    compute_error_for_line_given_points,
    compute_gradient_descent,
    step,
)


def test_compute_error_for_line_given_points() -> None:
    points = [(1, 2), (2, 4), (3, 6)]
    constant = 0.0
    gradient = 1.0
    error = compute_error_for_line_given_points(constant, gradient, points)
    assert isinstance(error, float)


def test_step() -> None:
    points = [(1, 2), (2, 4), (3, 6)]
    constant = 0.0
    gradient = 1.0
    learning_rate = 0.01
    new_constant, new_gradient = step(constant, gradient, points, learning_rate)
    assert new_constant != constant
    assert new_gradient != gradient


def test_compute_gradient_descent() -> None:
    points = [(1, 2), (2, 4), (3, 6)]
    constant = 0.0
    gradient = 0.0
    iterations = 10
    learning_rate = 0.01
    new_constant, new_gradient = compute_gradient_descent(
        constant, gradient, points, iterations, learning_rate
    )
    assert new_constant != constant
    assert new_gradient != gradient