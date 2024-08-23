import pandas as pd

def read_file(file_name):
    # TO DO  use proper function depending from file extension: (.xlsx, .csv, .parquet)
    df = pd.read_csv(file_name)
    
    print(f"** information about each column and whole DataFrame**")
    print(df.info())
    print(f"** count not-empty values, mean, standar deviation, minimal value, 25% percentile, 50% percentile, 75% percentile, maximal value**")
    print(df.describe())
    print(f"** unique elements of each column **")
    for i in df.columns:
        print(i,":", pd.unique(df[i]), "\n")
    print(f"** sumarize Nan, None, NaT for each column **")
    print(df.isnull().sum())
    

if __name__ == "__main__":
    # change value of file_name variable acording to the name of your file
    file_name = "table.csv" 
    print(read_file(file_name))
    
#XD
