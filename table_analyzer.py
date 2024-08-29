import pandas as pd
import inspect
import table_analyzer

def read_file(file_name):
    # TO DO  use proper function depending from file extension: (.xlsx, .csv, .parquet)
    df = pd.read_parquet(file_name)

    return df

def print_df():
    df = read_file(file_name)
    print(f"** analyzed DataFrame is: {file_name} **")
    print(df)
def print_df_info():
    df = read_file(file_name)
    print(f"** information about each column and whole DataFrame **")
    print(df.info())
def print_df_describe():
    df = read_file(file_name)
    print(f"** count not-empty values, mean, standar deviation, minimal value, 25% percentile, 50% percentile, 75% percentile, maximal value **")
    print(df.describe())
def print_df_uniques():
    df = read_file(file_name)
    print(f"** unique elements of each column **")
    for i in df.columns:
        print(i,":", pd.unique(df[i]), "\n")
def print_df_nulls():
    df = read_file(file_name)        
    print(f"** sumarize Nan, None, NaT for each column **")
    print(df.isnull().sum())
def print_functions_names():
    functions = inspect.getmembers(table_analyzer, inspect.isfunction)
    functions_cleaned = [f"{x[0]}()" for x in functions]

    return functions_cleaned

def execute_all_functions():
    pass

    


if __name__ == "__main__":
    # change value of file_name variable acording to the name of your file
    file_name = "collatz_v4_100kk-gz.parquet" 
    # print(read_file(file_name))git add
    # TO DO: execute multiple functions (all in this file)
    print(print_functions_names())
    execute_all_functions()

