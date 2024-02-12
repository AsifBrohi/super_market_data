import pandas as pd

class Extract:
    def __init__(self,file_path) -> None:
        self.file_path = file_path
    def turn_into_df(self:str)->pd.DataFrame:
        
        df = pd.read_csv(self.file_path)
        return df 

if __name__=="__main__":

    filepath_aldi= "../supermarket_data/All_Data_Aldi.csv"
    filepath_asda= "../supermarket_data/All_Data_ASDA.csv"
    extractor_aldi = Extract(filepath_aldi)
    df_aldi = extractor_aldi.turn_into_df()
    extractor_asda=Extract(filepath_asda)
    df_asda = extractor_asda.turn_into_df()

    print(df_asda.head(10))