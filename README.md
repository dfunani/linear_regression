# Linear Regression Application

This application implements a simple linear regression model using gradient descent. It calculates the best-fit line for a given dataset and visualizes the results.

## Features

- Computes the mean squared error for a line.
- Optimizes the line's parameters (constant and gradient) using gradient descent.
- Visualizes the resulting line and data points using the `line.draw` function.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `numpy`
  - `streamlit`

## File Structure

- `app.py`: Main application file containing the linear regression logic.
- `line.py`: Contains the `draw` function for visualizing the results.
- `data.csv`: Input dataset file (must be in CSV format with two columns: `time_studied` and `grade`).

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd linear_regression
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `data.csv` file is in the same directory as `app.py`. The file should have the following format:
   ```
   time_studied,grade
   1,2
   2,4
   3,6
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. The program will output the optimized constant, gradient, and error values. It will also visualize the results using the `draw` function.

## Example Output

```
constant=0.123 gradient=1.456 error=0.789
```

## Notes

- The learning rate and number of iterations can be adjusted in the `main` function.
- Ensure the `line.py` file contains a valid `draw` function for visualization.

## License

This project is licensed under the MIT License.