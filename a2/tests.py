from FGPA2 import *
import unittest

class TestFGPA2(unittest.TestCase):

    def test_read_df(self):
        self.assertIsInstance(read_df('finanzas2020[1].csv'), pd.DataFrame)

    def test_check_empty(self):
        df = read_df('finanzas2020[1].csv')
        self.assertEqual(len(check_empty(df).columns),12)

    def test_df_processing(self):
        df = read_df('finanzas2020[1].csv')
        df = check_empty(df)
        df = df_processing(df)
        calculos_df = calculos(df)
        self.assertTrue((calculos_df['ingresos'] > 0).any().any())

    
    def test_df_processing_1(self):
        df = read_df('finanzas2020[1].csv')
        df = check_empty(df)
        df = df_processing(df)
        calculos_df = calculos(df)
        self.assertTrue((calculos_df['gastos'] < 0).any().any())


    def test_df_processing_2(self):
        df = read_df('finanzas2020[1].csv')
        df = check_empty(df)
        df = df_processing(df)
        calculos_df = calculos(df)
        self.assertTrue((calculos_df['ahorros'] != 0).any().any())
    
if __name__ == '__main__':
    unittest.main()


