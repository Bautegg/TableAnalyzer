import table_analyzer as ta

# TODO: DONE run all table_analyer methods in this file, file_path should be there

def main():
    json_path = "config.json"
    file_name = "SampleSalesData/sales_data_sample.csv"
    ta.ExecutorUTA(json_path, file_name).run()




if __name__ == "__main__":
    main()
    