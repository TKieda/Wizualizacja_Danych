import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
df = pd.read_excel(xlsx, header=0)
print(df)