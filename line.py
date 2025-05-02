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
        points_df = pd.DataFrame(points, columns=["Studied (secs)", "Grade (%)"])

        st.subheader("Combined Plot:")
        fig, ax = plt.subplots()

        # Plot the line
        ax.plot(data["x"], data["y"], label=f"Line of Best Fit")

        # Plot the points
        ax.scatter(
            points_df["Studied (secs)"],
            points_df["Grade (%)"],
            color="red",
            marker="o",
            label="Grades vs Hours Studied",
        )

        # Add labels and title
        ax.set_xlabel("Time Spent Studying")
        ax.set_ylabel("Grade Received")
        ax.set_title("Time Spent Studying vs The Grade Received")
        ax.legend()
        ax.grid(True)

        # Display the Matplotlib figure in Streamlit
        st.pyplot(fig)
    else:
        st.info("Please enter some data points to display.")

    st.subheader("Data Points Entered:")
    st.write(points_df)

    # Create a Matplotlib figure and axes
    # fig, ax = plt.subplots()