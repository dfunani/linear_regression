# Linear Regression
from time import sleep
from numpy import genfromtxt
import streamlit

from line import draw


def compute_error_for_line_given_points(constant: int, gradient: int, points: list):
    error = 0
    for time_studied, grade in points:
        error += (grade - (gradient * time_studied) + constant) ** 2
    return error/len(points)

def compute_gradient_descent(constant, gradient, points, iterations, learning_rate):
    for _ in range(iterations):
        constant, gradient = step(constant, gradient, points, learning_rate)

    return constant, gradient

def step(constant, gradient, points, learning_rate):
    b = 0
    m = 0
    for time_studied, grade in points:
        b += -2/len(points) * (grade - ((gradient * time_studied)) + constant)
        m += -2/len(points) * time_studied * (grade - ((gradient * time_studied)) + constant)
    return constant - (learning_rate * b), gradient - (learning_rate * m)

def main():
    data = genfromtxt("data.csv", delimiter=",", skip_header=1)
    learning_rate = 0.0001
    constant = 0
    gradient = 0
    iterations = 1000
    
    error = compute_error_for_line_given_points(constant, gradient, data)
    print(f"{constant=} {gradient=} {error=}")

    constant, gradient = compute_gradient_descent(constant, gradient, data, iterations, learning_rate)
    
    error = compute_error_for_line_given_points(constant, gradient, data)
    print(f"{constant=} {gradient=} {error=}")
    return constant, gradient, data


if __name__ == "__main__":
    constant, gradient, points = main()
    draw(constant, gradient, points)