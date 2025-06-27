import pandas as pd
import json

# Universal Table Analyzer

class UTA:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_df = self._file_to_df()
    
    def _file_to_df(self):
        if self.file_name[-8:] == ".parquet":
            print(self.file_name[-8:])
            df = pd.read_parquet(self.file_name)
            return df

        elif self.file_name[-4:] == ".csv":
            df = pd.read_csv(self.file_name, encoding="unicode_escape")
            return df
        
        elif self.file_name[-5:] == ".xlsx":
            df = pd.read_excel(self.file_name)
            return df
        
        else:
            print("not that type BRO!!!!!")        

    def print_df(self):        
        df = self._file_to_df()
        print(f"** analyzed DataFrame is: {self.file_name} **")
        print(df)

    def print_df_info(self):
        print(f"** information about each column and whole DataFrame **")
        print(self.file_df.info())

    def print_df_describe(self):
        print(f"** count not-empty values, mean, standar deviation, minimal value, 25% percentile, 50% percentile, 75% percentile, maximal value **")
        print(self.file_df.describe())

    def print_df_uniques(self):
        print(f"** unique elements of each column **")
        for i in self.file_df.columns:
            uniq_elements = pd.unique(self.file_df[i])
            print(f"{i}: {uniq_elements}; UNIQUE ELEMENTS COUNT: {len(uniq_elements)}")

    def print_df_nulls(self):          
        print(f"** sumarize Nan, None, NaT for each column **")
        print(self.file_df.isnull().sum())

class ExecutorUTA:
    def __init__(self,json_config, file_name):
        self.json_config = json_config
        self.procesor = UTA(file_name)

    def run(self):
        for i in self.json_config.get("run_this", []):
            method_name = i.get("method")
            params = i.get("params", {})

            method = getattr(self.procesor, method_name, None)

            if callable(method):
                try:
                    output = method(**params)
                    print(f"Method: {method_name} → Output: {output}")
                except Exception as e:
                    print(f"Error calling method '{method_name}': {e}")
            else:
                print(f"Method '{method_name}' not found in DataProcessor.")

if __name__ == "__main__":
    json_path = "config.json"
    file_name = "SampleSalesData/sales_data_sample.csv"
    
    with open(json_path, "r") as file:
        config = json.load(file)

    executor = ExecutorUTA(config, file_name)
    executor.run()


