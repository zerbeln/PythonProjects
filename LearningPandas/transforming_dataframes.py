import pandas as pd


def groupby_aggregations():
    iris = pd.read_csv('iris.csv')
    print(iris.head(5))
    print('\n')

    # groupby will sort data along a given dimension
    # Pandas can flatten hierarchical index with reset_index()
    print(iris.groupby(['species']).max())
    print('\n')

    # There are multiple different aggregation methods to different variables
    df = iris.groupby(['species']).agg({'sepal_length': ['mean', 'min', 'max'], 'sepal_width': 'count'})
    print(df)
    print('\n')

    # Flattening hierarchical indexes
    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    df.reset_index()
    print(df)
    print('\n')

    # Specify groupings prior to any aggregation
    groupings = iris.groupby(['species'])
    print(groupings.get_group('setosa').head())  # Displays all rows in data of the desired species
    print('\n')

    # After declaring groupings, you can then apply aggregate functions
    print(groupings.max())
    print(groupings.apply(lambda x: x.max()))  # identical to the output above
    print(groupings.filter(lambda x: x['petal_length'].max() < 5))  # only species with petal length below 5


def reshaping_dataframes():
    df = pd.DataFrame({
        "Region": ['North', 'West', 'East', 'South', 'North', 'West', 'East', 'South'],
        "Team": ['One', 'One', 'One', 'One', 'Two', 'Two', 'Two', 'Two'],
        "Revenue": [7500, 5500, 2750, 6400, 2300, 3750, 1900, 575],
        "Cost": [5200, 5100, 4400, 5300, 1250, 1300, 2100, 50]
    })
    print(df)
    print('\n')

    # Pivot 'Team' to Columns with Region as an index
    print(df.pivot(index='Region', columns=['Team'], values='Revenue'))
    print('\n')

    # We can use stack to 'pivot' the opposite direction
    df2 = df.set_index(['Region', 'Team'])  # Create a multi-index
    stacked = pd.DataFrame(df2.stack())
    print(stacked)
    print('\n')

    # Process can be reversed with unstack
    print(stacked.unstack())
    print('\n')

    # We can also specify where to unstack
    print(stacked.unstack('Region'))
    print('\n')

    # Melt allows you to specify ID variables while transforming all other columns or "measure variables" to the row lvl
    print(df.melt(id_vars=['Region', 'Team'], var_name='value type'))  # pivot rev and cost back to row level
    print('\n')

    # Using pivot_table
    print(df.pivot_table(index='Team', values='Revenue'))  # by default this uses mean to aggregate


if __name__ == "__main__":
    reshaping_dataframes()

