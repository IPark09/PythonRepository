import pandas as pd
import numpy as np
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "Cars93_missing.csv")

def task1():
    df = pd.read_csv(CSV_PATH, na_values=["NA"])
    print(df.head())
    return df

def task2(df):
    s = df.iloc[:, 0]
    df2 = df.set_index(s)
    print(df2.head())
    return df2

def task3(df, col=None):
    col = col or df.select_dtypes(include=np.number).columns[0]
    df[col] = df[col].apply(lambda x: x * 2 if pd.notna(x) and x > df[col].mean() else x)
    print(df[[col]].head())
    return df

def task4(df):
    print("Columns:", list(df.columns))
    print("Missing values per column:\n", df.isnull().sum())

def task5(df, col_a=None, col_b=None):
    cols = list(df.columns)
    col_a = col_a or cols[0]
    col_b = col_b or cols[1]

    def swap_columns(frame, c1, c2):
        cols = list(frame.columns)
        i1, i2 = cols.index(c1), cols.index(c2)
        cols[i1], cols[i2] = cols[i2], cols[i1]
        return frame[cols]

    df = swap_columns(df, col_a, col_b)
    df = df[sorted(df.columns)]
    print(df.head())
    return df

def task6(df, col=None):
    col = col or df.select_dtypes(include=np.number).columns[0]
    low, high = df[col].quantile(0.05), df[col].quantile(0.95)
    trimmed = df[(df[col] >= low) & (df[col] <= high)]
    print(f"Rows before: {len(df)}, after trimming {col}: {len(trimmed)}")
    return trimmed

def task7(df, col=None):
    col = col or df.select_dtypes(include=np.number).columns[0]
    df[col] = df[col].fillna(df[col].mean())
    print(df[[col]].head())
    return df

def task8():
    dict1 = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Carol']}
    dict2 = {'id': [1, 2, 3], 'score': [90, 85, 95]}
    df1 = pd.DataFrame(dict1)
    df2 = pd.DataFrame(dict2)

    merged = pd.merge(df1, df2, on='id')
    print("Merged:\n", merged)

    appended = df1.join(df2.drop(columns='id'))
    print("Appended as new column:\n", appended)
    return merged, appended

def task9(df, col=None):
    col = col or df.select_dtypes(include=np.number).columns[0]
    ax = df[col].plot.hist(title=f"Histogram of {col}")
    fig = ax.get_figure()
    fig.savefig("histogram.png")
    print(f"Saved histogram.png for column '{col}'")

def task10(df):
    corr = df.select_dtypes(include=np.number).corr()
    print(corr)
    return corr


if __name__ == '__main__':
    df = task1()
    task2(df.copy())
    task3(df.copy())
    task4(df)
    task5(df.copy())
    task6(df.copy())
    task7(df.copy())
    task8()
    task9(df.copy())
    task10(df)