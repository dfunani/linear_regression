from time import sleep
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def draw(constant: float, gradient: float, points: list[tuple[float, float]]) -> None:
    """
    Draws a line and plots data points using Streamlit and Matplotlib.
    """
    st.title("Drawing a Line with Streamlit")
    st.subheader(f"Line Equation: y = {gradient:.1f}x + {constant:.1f}")

    # Generate x values
    x = np.linspace(-100, 100, 100)

    # Calculate corresponding y values
    y = gradient * x + constant

    # Create a Pandas DataFrame for plotting with Streamlit
    data = pd.DataFrame({"x": x, "y": y})

    if len(points):
        points_df = pd.DataFrame(points, columns=["x_point", "y_point"])

        st.subheader("Combined Plot:")
        fig, ax = plt.subplots()

        # Plot the line
        ax.plot(data["x"], data["y"], label=f"y = {gradient:.1f}x + {constant:.1f}")

        # Plot the points
        ax.scatter(
            points_df["x_point"],
            points_df["y_point"],
            color="red",
            marker="o",
            label="Data Points",
        )

        # Add labels and title
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Line and Data Points")
        ax.legend()
        ax.grid(True)

        # Display the Matplotlib figure in Streamlit
        st.pyplot(fig)
    else:
        st.info("Please enter some data points to display.")

    st.subheader("Data Points Entered:")
    st.write(points)

    # Create a Matplotlib figure and axes
    fig, ax = plt.subplots()