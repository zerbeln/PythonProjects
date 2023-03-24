import pandas as pd


def handling_data_types():
    planets = pd.read_csv('planets.csv')

    # Show first 3 rows of planets.csv
    print('First 3 rows of data: ')
    print(planets.head(3))
    print('\n')

    # Show planets data types
    print("Data Types: ")
    print(planets.dtypes)
    print('\n')

    # Show average for all float/integer values in data set
    print("Data averages: ")
    print(planets.mean())
    print('\n')

    # We can change data types in Pandas
    print("Data type conversions: ")
    print(planets['number'][0].astype(float))  # Convert from int to float
    print(planets['mass'][0].astype(int))  # Convert from float to int
    print(planets['year'][0].astype(str))  # Convert integer to a string
    print('\n')

    # We can convert the year information into a date/time format
    print("Date-Time Conversions: ")
    planets['year_dt'] = pd.to_datetime(planets['year'], format='%Y')
    print(planets['year_dt'])


def handling_strings():
    names = pd.Series(['Pomeray, CODY ', ' Wagner; Jarry', 'smith, Ray'])  # Inconsistent data is intentional here

    # Replace semicolon
    names = names.str.replace(';', ',')
    print(names)
    print('\n')

    # Show the length of each string
    print("String lengths: ")
    print(names.str.len())
    print('\n')

    # Strip leading and trailing spaces in data set
    names = names.str.strip()
    print("Spaces stripped: ")
    print(names.str.len())
    print('\n')

    # Make data consistent (converting everything to lowercase)
    names = names.str.lower()
    print("Make data consistent with lowercase letters: ")
    print(names)
    print('\n')
    # Note str.upper() converts all to uppercase letters

    # Reverse the order of first & last name
    print('Present names as first last instead of last, first: ')
    names = names.str.split(', ')  # Creates a tuple of last names and first name
    names = pd.Series([i[::-1] for i in names])  # Switches the order
    names = [' '.join(i) for i in names]  # joins together first and last names seperated by a space
    print(names)


def working_with_dates():
    daterange = pd.period_range('1/1/2020', freq='30d', periods=4)  # Creat time series data
    date_df = pd.DataFrame(data=daterange, columns=['sample date'])  # Organize into a data frame
    print(date_df)
    print('\n')

    # Calculate time difference from prior date with diff function
    date_df['time difference'] = date_df['sample date'].diff(periods=1)
    print("Show time difference between periods in data: ")
    print(date_df)
    print('\n')

    # Find the first day of the month
    date_df['first of month'] = date_df['sample date'].values.astype('datetime64[M]')
    print("Find the first day of the month: ")
    print(date_df)
    print('\n')

    # Check data types
    print("date data types: ")
    print(date_df.dtypes)
    print('\n')

    # Convert 'sample date' from period type to datetime64 type
    date_df['sample date'] = date_df['sample date'].dt.to_timestamp()
    print("Show converted data type for sample date: ")
    print(date_df.dtypes)
    print('\n')

    # Date subtraction
    print("Subtracting dates: ")
    print(date_df['sample date'] - date_df['first of month'])
    print(date_df['sample date'] - date_df['time difference'])
    print(date_df['sample date'] - pd.Timedelta('30 d'))
    print('\n')

    # More datetime properties with dt
    print("Show the day name: ")
    print(date_df['sample date'].dt.day_name())


def handling_missing_data():
    temps = pd.DataFrame({
        "sequence": [1, 2, 3, 4, 5],
        "measurement_type": ['actual', 'actual', 'actual', None, 'estimated'],
        "temperature_f": [67.24, 84.56, 91.61, None, 49.64]
    })
    print(temps)
    print('\n')

    # Identify null values present in a data frame
    print("Show missing data (null values): ")
    print(temps.isna())
    print('\n')

    # See how missing data is handled
    print("Show cumulative sums of data: ")
    print(temps['temperature_f'].cumsum())  # By default, pandas skips Null values
    print("Show cumulative sums with skipna set to false: ")
    print(temps['temperature_f'].cumsum(skipna=False))
    print('\n')

    # Some methods drop null data (for example group by)
    print("Default group by drops nulls, can specify to keep them: ")
    print(temps.groupby(by=['measurement_type']).max())
    print(temps.groupby(by=['measurement_type'], dropna=False).max())  # Specify to retain N/A
    print('\n')

    # Treating nulls
    # Blunt method
    print("Drop rows with NaN: ")
    print(temps.dropna())  # Drop rows with NaN
    print("Drop columns with NaN: ")
    print(temps.dropna(axis=1))  # Drop columns with NaN
    print('\n')

    # Replace or 'fill' nulls
    print("Replace nulls with 0: ")
    print(temps.fillna(0))  # Replace nulls with 0
    print("Carry over values from prior row: ")
    print(temps.fillna(method='pad'))  # Carry over values from a prior row
    print("Interpolate data: ")
    print(temps.interpolate())


if __name__ == "__main__":
    df = pd.DataFrame({
        "Region": ['North', 'West', 'East', 'South', 'North', 'West', 'East', 'South'],
        "Team": ['One', 'One', 'One', 'One', 'Two', 'Two', 'Two', 'Two'],
        "Squad": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        "Revenue": [7500, 5500, 2750, 6400, 2300, 3750, 1900, 575],
        "Cost": [5200, 5100, 4400, 5300, 1250, 1300, 2100, 50]
    })
    print('\n')

    # Use apply() to alter values along an axis in your datafram or in a series by applying a function
    df['Profit'] = df.apply(lambda x: 'Profit' if x['Revenue'] > x['Cost'] else 'Loss', axis=1)
    print(df)
    print('\n')

    # Use map to substitute each value in a series, using either a function, dictionary, or series
    team_map = {"One": "Red", "Two": "Blue"}
    df['Team Color'] = df['Team'].map(team_map)
    print(df)
    print('\n')

    # Use applymap() to apply a function to each element in your dataframe
    print(df.applymap(lambda x: len(str(x))))
    print('\n')

    # You can also use for loops
    new_col = []
    for i in range(0, len(df)):
        rev = df['Revenue'][i] / df[df['Region'] == df.loc[i, 'Region']]['Revenue'].sum()
        new_col.append(rev)

    df['Revenue Share of Region'] = new_col
    print(df.sort_values(by='Region'))
