import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    iris = pd.read_csv("iris.csv")
    print(iris.head(3))
    print('\n')

    # Measures of data central tendancy (common stats)
    print("Mean: ")
    print(iris.mean())
    print('\n')
    print("Median: ")
    print(iris.median())
    print('\n')
    print("Mode: ")
    print(iris.mode())
    print('\n')

    # Variance Measures
    print("Standard Deviations")
    print(iris.std())
    # pd.plotting.boxplot(iris)
    plt1 = iris.boxplot();
    plt.show()

    # Quick Insights
    print(iris.describe())
    print('\n')

    # Relationships between variables
    print("Correlations: ")
    ir_corr = iris.corr()
    print(ir_corr)
