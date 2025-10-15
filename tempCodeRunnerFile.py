import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from models import train_model, calculate_accuracy
from plots import generate_plot
from utils import load_dataset
from sklearn.model_selection import train_test_split