# Linear Regression
from time import sleep
from numpy import genfromtxt
import streamlit

from line import draw


def compute_error_for_line_given_points(constant: float, gradient: float, points: list[tuple[float, float]]) -> float:
    """
    Computes the mean squared error for a given line defined by its constant and gradient.
    """
    error = 0.0
    for time_studied, grade in points:
        error += (grade - (gradient * time_studied) + constant) ** 2
    return error / len(points)


def compute_gradient_descent(constant: float, gradient: float, points: list[tuple[float, float]], iterations: int, learning_rate: float) -> tuple[float, float]:
    """
    Performs gradient descent to optimize the constant and gradient for the line.
    """
    for _ in range(iterations):
        constant, gradient = step(constant, gradient, points, learning_rate)
    return constant, gradient


def step(constant: float, gradient: float, points: list[tuple[float, float]], learning_rate: float) -> tuple[float, float]:
    """
    Computes a single step of gradient descent for the constant and gradient.
    """
    b = 0.0
    m = 0.0
    for time_studied, grade in points:
        b += -2 / len(points) * (grade - ((gradient * time_studied)) + constant)
        m += -2 / len(points) * time_studied * (grade - ((gradient * time_studied)) + constant)
    return constant - (learning_rate * b), gradient - (learning_rate * m)


def main(filename: str = "data.csv") -> tuple[float, float, list[tuple[float, float]]]:
    """
    Main function to load data, perform gradient descent, and compute the final error.
    """
    data = genfromtxt(filename, delimiter=",", skip_header=1)
    learning_rate = 0.0001
    constant = 0.0
    gradient = 0.0
    iterations = 1000

    error = compute_error_for_line_given_points(constant, gradient, list(data))
    print(f"{constant=} {gradient=} {error=}")

    constant, gradient = compute_gradient_descent(constant, gradient, list(data), iterations, learning_rate)

    error = compute_error_for_line_given_points(constant, gradient, list(data))
    print(f"{constant=} {gradient=} {error=}")
    draw(constant, gradient, data)


if __name__ == "__main__":
    main()