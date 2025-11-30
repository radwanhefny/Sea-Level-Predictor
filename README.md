
# 📊 Sea-Level-Predictor
A Python program that analyzes historical sea level data and visualizes it using scatter plots with linear regression lines. The project predicts future sea level trends using two lines of best fit: one based on all available data, and another using data from the year 2000 onward.
## ✨ Features
- Reads sea level data from a CSV file.
- Creates a scatter plot of historical sea level measurements.
- Adds a line of best fit for all years (1880–2050 prediction).
- Adds a line of best fit for recent years (2000–2050 prediction) to highlight accelerated trends.
- Saves the plot as a PNG image.
## 📋 Prerequisites
Before running this project, ensure you have:
- Python 3.8+
- Pandas, Matplotlib, SciPy libraries
- CSV dataset epa-sea-level.csv inside a data folder
- Basic understanding of Python and plotting
## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/radwanhefny/Sea-Level-Predictor.git
cd Sea-Level-Predictor

```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the visualization scripts:
```bash
python main.py
```
## 🎬 Screenshots / Demo
**Result:**  
![sea level plot](https://github.com/radwanhefny/Sea-Level-Predictor/blob/main/examples/Result.png)

## 🗂️ Project Structure
```
📁 Sea-Level-Predictor
├── main.py
├── sea_level_predictor.py   # Core calculations and plotting
├── data/
│   └── epa-sea-level.csv    # Dataset
├── examples/
│   ├── Figure_1.png         # Scatter plot with best fit lines
│   └── Result_1.png         # Final plotted result
├── requirements.txt
├── test_module.py
└── README.md
```
## 🛠️ Usage
Example usage inside Python:
```python
from sea_level_predictor import draw_plot

plot_ax = draw_plot()
plot_ax.figure.show()



```
Expected output:
- sea_level_plot.png → Scatter plot of sea level data with two lines of best fit
## ✅ Tests
Run the FreeCodeCamp test suite:
```bash
python test_module.py
```
## 🧠 How It Works
1. Reads the CSV dataset using Pandas.
2. Creates a scatter plot of historical sea levels.
3. Computes two lines of best fit using linear regression:
   - One for all years
   - One for years 2000 onward
5. Extends the lines to 2050 to visualize future trends.
6. Saves the final plot as a PNG image for reporting or analysis.

## 🤝 Contributing
Contributions are welcome!
1. Fork the repository
2. Create a new feature branch
3. Submit a pull request
Please ensure your code is clean, structured, and well-commented.
## 📝 License
This project is licensed under the MIT license - see the LICENSE file for details. 
## 📞 Support
If you have questions or need help, feel free to:
- Open an issue on this repository  
- Connect with me on LinkedIn: https://www.linkedin.com/in/radwanhefny  
