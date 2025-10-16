# 🤖 ML Data Analytics & Visualization App

A comprehensive desktop application for machine learning data analysis, model training, and visualization built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-red.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Models](#supported-models)
- [File Formats](#file-formats)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This application provides an intuitive graphical interface for performing machine learning tasks without requiring extensive programming knowledge. Users can load datasets, train various ML models, visualize data patterns, and make predictions through a modern, user-friendly interface.

### Key Capabilities
- **Data Loading**: Import CSV and Excel files
- **Model Training**: Train 6 different ML algorithms
- **Data Visualization**: Generate plots and charts
- **Prediction**: Make real-time predictions with trained models
- **Model Evaluation**: View accuracy metrics and performance

## ✨ Features

### 🔧 Core Features
- **Modern GUI**: Clean, responsive interface with Bootstrap-inspired themes
- **Multiple ML Algorithms**: Support for 6 different machine learning models
- **Interactive Visualizations**: Embedded matplotlib plots with navigation tools
- **Real-time Predictions**: Input custom values and get instant predictions
- **Data Preview**: View and explore loaded datasets in tabular format
- **Model Evaluation**: Automatic accuracy calculation and performance metrics

### 📊 Visualization Features
- **Scatter Plots**: Explore relationships between variables
- **Confusion Matrix**: Evaluate classification model performance
- **Interactive Navigation**: Zoom, pan, and save plot functionality
- **Embedded Plots**: Visualizations integrated directly in the application

### 🎨 User Interface
- **Modern Themes**: Multiple theme options (Pulse, Darkly, Solar, etc.)
- **Responsive Design**: Resizable interface with minimum 1000x700 resolution
- **Menu System**: Organized file operations and help sections
- **Status Updates**: Real-time feedback on operations

## 🖼️ Screenshots

```
┌─────────────────────────────────────────────────────────────┐
│  File  Help                                    [_] [□] [×]  │
├─────────────────────────────────────────────────────────────┤
│  📁 Load Dataset    🤖 Train Model    📊 Generate Plot     │
├─────────────────────────────────────────────────────────────┤
│  Dataset: sample_data.csv                                   │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           Data Preview Table                            │ │
│  │  Feature1  Feature2  Feature3  Target                  │ │
│  │    1.2      2.3      3.4       A                       │ │
│  │    2.1      3.2      4.1       B                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                             │
│  Model: Random Forest    Accuracy: 95.2%                   │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                 Visualization Area                      │ │
│  │              [Interactive Plot Here]                    │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Model_Visulization
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Manual Installation

If you prefer to install packages manually:

```bash
pip install pandas scikit-learn matplotlib seaborn ttkbootstrap
```

### System Requirements
- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB free space
- **Display**: 1024x768 minimum resolution

## 📖 Usage

### Getting Started

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Load Your Dataset**
   - Click "Load Dataset" button
   - Select a CSV or Excel file
   - Preview your data in the table

3. **Select Features**
   - Choose input features (X variables)
   - Select target variable (y variable)

4. **Train a Model**
   - Select from 6 available algorithms
   - Click "Train Model"
   - View accuracy metrics

5. **Make Predictions**
   - Input values for each feature
   - Click "Predict" to get results

6. **Visualize Data**
   - Generate scatter plots
   - View confusion matrices
   - Explore data patterns

### Example Workflow

```python
# 1. Load dataset (iris.csv)
# 2. Select features: sepal_length, sepal_width, petal_length, petal_width
# 3. Select target: species
# 4. Train Random Forest model
# 5. Achieve 96% accuracy
# 6. Make prediction: [5.1, 3.5, 1.4, 0.2] → "setosa"
```

## 🤖 Supported Models

| Algorithm | Type | Use Case | Strengths |
|-----------|------|----------|-----------|
| **Linear Regression** | Regression | Continuous prediction | Simple, interpretable |
| **Logistic Regression** | Classification | Binary/multi-class | Fast, probabilistic |
| **Decision Tree** | Classification | Rule-based decisions | Interpretable, handles non-linear |
| **Random Forest** | Classification | Ensemble learning | High accuracy, robust |
| **SVM** | Classification | Complex boundaries | Effective in high dimensions |
| **Naive Bayes** | Classification | Text/categorical data | Fast, works with small datasets |

### Model Selection Guide

- **For beginners**: Start with Decision Tree or Logistic Regression
- **For high accuracy**: Use Random Forest or SVM
- **For interpretability**: Choose Decision Tree or Linear Regression
- **For speed**: Use Naive Bayes or Logistic Regression

## 📁 File Formats

### Supported Input Formats
- **CSV files** (`.csv`) - Comma-separated values
- **Excel files** (`.xlsx`, `.xls`) - Microsoft Excel format

### Data Requirements
- **Headers**: First row should contain column names
- **Clean data**: No missing values in target column
- **Numeric features**: Most algorithms work best with numerical data
- **Categorical targets**: Automatically encoded for regression models

### Example Data Structure
```csv
feature1,feature2,feature3,target
1.2,2.3,3.4,class_A
2.1,3.2,4.1,class_B
1.8,2.9,3.7,class_A
```

## 📂 Project Structure

```
Model_Visulization/
├── 📄 main.py              # Application entry point
├── 📄 app.py               # Main GUI application class
├── 📄 models.py            # ML model implementations
├── 📄 plots.py             # Visualization functions
├── 📄 utils.py             # Utility functions
├── 📄 requirements.txt     # Project dependencies
├── 📄 README.md           # Project documentation
├── 🖼️ icon.ico            # Application icon
├── 📄 app.spec            # PyInstaller specification
├── 📄 main.spec           # PyInstaller specification
└── 📁 __pycache__/        # Python cache files
```

### Module Descriptions

- **`main.py`**: Entry point that initializes the GUI with theme selection
- **`app.py`**: Core application logic, GUI components, and event handlers
- **`models.py`**: Machine learning model training and evaluation functions
- **`plots.py`**: Data visualization and plotting utilities
- **`utils.py`**: Helper functions for data loading and processing

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pandas` | Latest | Data manipulation and analysis |
| `scikit-learn` | Latest | Machine learning algorithms |
| `matplotlib` | Latest | Basic plotting and visualization |
| `seaborn` | Latest | Statistical data visualization |
| `ttkbootstrap` | Latest | Modern GUI themes |
| `numpy` | Auto-installed | Numerical computing |

### Installation Commands
```bash
# Core ML and data processing
pip install pandas scikit-learn numpy

# Visualization
pip install matplotlib seaborn

# Modern GUI
pip install ttkbootstrap

# All at once
pip install -r requirements.txt
```

## 🛠️ Development

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Model_Visulization
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Building Executable

To create a standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller main.spec
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
1. **Bug Reports**: Report issues or bugs
2. **Feature Requests**: Suggest new features
3. **Code Contributions**: Submit pull requests
4. **Documentation**: Improve documentation
5. **Testing**: Help test the application

### Development Guidelines
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Future Enhancements
- [ ] Support for more file formats (JSON, Parquet)
- [ ] Additional ML algorithms (XGBoost, Neural Networks)
- [ ] Advanced visualization options
- [ ] Model comparison features
- [ ] Export trained models
- [ ] Batch prediction capabilities

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Scikit-learn** team for the excellent ML library
- **Matplotlib** and **Seaborn** for visualization capabilities
- **ttkbootstrap** for modern GUI themes
- **Pandas** for data manipulation tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error messages and system information

## 🎓 Educational Use

This project is perfect for:
- **Learning ML concepts**: Hands-on experience with different algorithms
- **Data science education**: Understanding data preprocessing and visualization
- **GUI development**: Learning tkinter and modern UI design
- **Software engineering**: Understanding modular code organization

---

**Made with ❤️ for Machine Learning Education**

*Happy Learning! 🚀*