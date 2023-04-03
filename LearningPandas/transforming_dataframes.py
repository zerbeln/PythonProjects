import pandas as pd
import numpy as np


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


def merging_and_joining():
    df1 = pd.DataFrame({
        'letter': ['A', 'B', 'C', 'D'],
        'number': [1, 2, 3, 4]
    })
    df2 = pd.DataFrame({
        'letter': ['C', 'D', 'E', 'F'],
        'number': [3, 4, 5, 6]
    })
    print("DF1 and DF2")
    print(df1)
    print(df2)
    print('\n')

    # Perform a "Left Join" or the left + center part of a venn diagram
    print("Left Joined DF1 and DF2")
    print(df1.merge(df2, how='left', on='number'))
    print('\n')

    # Perform an "Inner Join" or the center part of a venn diagram
    print("Inner Joined DF1 and DF2")
    print(df1.merge(df2, how='inner', left_on='number', right_on='number'))
    print('\n')

    # Perform a "Right Join" or the right + center part of a venn diagram
    print("Right Joined DF1 and DF2")
    print(df1.merge(df2, how='right', on='number', suffixes=('', '_right')))  # suffix changes the naming for column
    print('\n')

    # Concatenate multiple dataframes
    df3 = pd.concat([df1, df2]).drop_duplicates().reset_index(
        drop=True)  # drop=True removes indexing from merged dataframes
    print("Concatenated dataframe")
    print(df3)
    print('\n')

    # Dataframes can be concatenated horizontally
    df4 = pd.concat([df1, df2], axis=1)
    print("Horizontally concatenated dataframe")
    print(df4)
    print('\n')

    # Add a new row to your data frame
    new_row = pd.Series(['Z', 26], index=df3.columns)
    print("New row appended to database")
    # print(df3.append(new_row, ignore_index=True))  # Append is being deprecated
    print(pd.concat([df3.loc[:], pd.DataFrame(new_row).transpose()]).reset_index(drop=True))
    print('\n')

    # Join dataframes using index values
    join_df = pd.DataFrame({
        'letter': ['F', 'G', 'H', 'I'],
        'number': [6, 7, 8, 9]
    })
    print("Joined Data Frames")
    print(df2.join(join_df, rsuffix='_right'))


if __name__ == "__main__":
    df = pd.DataFrame({
        "Species": ['Chinook', 'Chum', 'Coho', 'Steelhead', 'Bull Trout'],
        "Population": ['Skokomish', 'Lower Skokomish', 'Skokomish', 'Skokomish', 'SF Skokomish'],
        "Count": [1208, 2396, 3220, 6245, 8216]
         })

    print(df)
    print('\n')

    # Binning numerical data with cut
    bins = [0, 2000, 4000, 6000, 8000, np.inf]
    labels = ['Low Return', 'Below Avg Return', 'Avg Return', 'Above Avg Return', 'High Return ']
    df['Count Category'] = pd.cut(df['Count'], bins, labels=labels)
    print("Data Frame with Binned Data")
    print(df)
    print('\n')

    # Mapping data
    fed_status={
        "Chinook": "Threatened",
        "Chum": "Not Warranted",
        "Coho": "Not Warranted",
        "Steelhead": "Threatened"
    }
    print("Mapping to endangered species")
    df["Federal Status"] = df["Species"].map(fed_status)
    print(df)
    print('\n')

    # Introduction to the categorical data type
    df['Count Category'] = pd.Categorical(df['Count Category'], ordered=True, categories=labels)
    print("Categorical Data")
    print(df['Count Category'])
    print('\n')

    # We can use the categorical data to sort the data
    print(df.sort_values(by=['Count Category'], ascending=False))
    print('\n')

    # Convert categorical variable to a dummy variable
    print("Dummy Variables")
    print(pd.get_dummies(df['Count Category']))
