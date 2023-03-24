import pandas as pd


def getting_started():
    # Input Data
    scores = {
        "name": ['Ray', 'Ben', 'Jacob'],
        "city": ['Denver', 'Seattle', 'New York'],
        "score": [75, 95, 91]
    }

    # Turn Data into a Pandas Data Frame
    df = pd.DataFrame(scores)
    print(df)

    # Columns can be added to data like this
    df['name_city'] = df['name'] + '_' + df['city']
    print(df)

    # Apply boolean logic to data frame to return scores above 90
    print("Scores above 90: ")
    print(df[df['score'] > 90])


def reading_data():
    # Import existing data using built in pandas functions
    iris = pd.read_csv('iris.csv')
    print("Data shape is: ", iris.shape)

    # View top n rows and bottom n rows
    print(iris.head(3))
    print(iris.tail(3))

    # Show data types
    print("Data types: ")
    print(iris.dtypes)

    # Pandas will output data to a csv
    iris.to_csv('iris_output.csv', index=False)  # Setting index to false makes sures index on left is dropped


if __name__ == "__main__":
    # getting_started()
    # reading_data()

    emissions = pd.DataFrame({
        "country": ['USA', 'China', 'India'],
        "year": [2018, 2018, 2018],
        "co2_emissions": [5410000000.0, 10060000000.0, 2650000000.0]
    })

    # print(emissions)

    # Configure maximum row size to display for data frame
    pd.set_option('display.max_rows', 2)
    print(emissions)

    # Configure maximum column size to display for data frame
    pd.set_option('display.max_columns', 2)
    print(emissions)

    # Supress scientific notation
    pd.options.display.float_format = '{:,.2f}'.format
    print(emissions)
