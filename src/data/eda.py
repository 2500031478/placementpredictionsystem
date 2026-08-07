
from src.data.load_data import load_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def basic_eda(df):
    print("============================================================================================")
    print("First Five rows of the DataFrame:")
    print(df.head())

    print("============================================================================================")
    print("Last Five rows of the DataFrame:")
    print(df.tail())

    print("============================================================================================")
    print("25 to 29 rows of the DataFrame:")
    print(df.iloc[25:30])

    print("============================================================================================")
    print("Random Sample of 10 records:")
    print(df.sample(10))

    print("============================================================================================")
    print("Columns in the DataFrame:")
    print(df.columns)

    print("============================================================================================")
    print("Data type of the DataFrame:")
    print(df.dtypes)

    print("============================================================================================")
    print("Complete Information of the DataFrame:")
    print(df.info())

    print("============================================================================================")
    print("Descriptive Statistics of the DataFrame:")
    print(df.describe())

    print("============================================================================================")
    print("Number of null values in the DataFrame  count :")
    print(df.isnull().sum())

    print("============================================================================================")
    print("Duplicate values of the DataFrame:")
    print(df.duplicated())

    print("============================================================================================")
    missing = df.isnull().sum()
    print("Missing Values of the DataFrame:")
    print(missing[missing > 0])

    print("============================================================================================")
    print("Target Variable status")
    print(df["PlacementStatus"].value_counts())

    print("============================================================================================")

    plt.figure(figsize=(6, 5))
    count = df["PlacementStatus"].value_counts()
    plt.bar(count.index, count.values)
    plt.title("Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\Placement_Status.png"
    )
    plt.show()
    plt.close()


def univariant(df):
    plt.figure(figsize=(6, 5))
    plt.hist(df["CGPA"], bins=10)
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\histogram.png"
    )
    plt.show()
    plt.close()


def gendercount(df):
    gendercount = df["Gender"].value_counts()

    plt.figure(figsize=(6, 5))
    plt.pie(
        gendercount,
        labels=gendercount.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Histogram of Gender")
    plt.xlabel("Gender")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\genderPieChart.png"
    )
    plt.show()
    plt.close()


def bivariate(df):
    plt.figure(figsize=(6, 5))
    plt.scatter(df["CGPA"], df["AptitudeTestScore"])
    plt.title("CGPA VS Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\cgpa_aptitude_test_score.png"
    )
    plt.show()
    plt.close()

    plt.figure(figsize=(6, 5))
    placed = df[df["PlacementStatus"] == 1]["CGPA"]
    not_placed = df[df["PlacementStatus"] == 0]["CGPA"]

    plt.boxplot(
        [placed, not_placed],
        tick_labels=["placed", "not placed"]
    )
    plt.title("CGPA vs Placement Status")
    plt.xlabel("PlacementStatus")
    plt.ylabel("CGPA")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\CGPA_PlacementStatus_boxplot.png"
    )
    plt.show()
    plt.close()


def multivariate(df):
    data = df[["CGPA", "AptitudeTestScore", "PlacementStatus"]]

    correlation = data.corr()

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation HeatMap")
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\HEATMAP.png"
    )
    plt.savefig(
        r"C:\Users\dhanu\PycharmProjects\PlacementPredictionSystem\app\static\charts\Correlation_HeatMap.png"
    )
    plt.show()
    plt.close()


if __name__ == "__main__":
    df = load_data()

    basic_eda(df)
    univariant(df)
    gendercount(df)
    bivariate(df)
    multivariate(df)

