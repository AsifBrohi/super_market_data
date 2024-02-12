import pandas as pd 
import unittest

from src.extract import Extract

class test_dataframe(unittest.TestCase):
    def test_turn_df(self):
        file_path = "../supermarket_data/All_Data_Aldi.csv"
        extractor=Extract(file_path)
        df = extractor.turn_into_df()
        self.assertIsInstance(df,pd.DataFrame,"No Dataframe was created")
 

if __name__ == "__main__":
    unittest.main()

    