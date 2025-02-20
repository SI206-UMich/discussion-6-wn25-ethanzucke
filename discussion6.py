import unittest
import os
import csv

def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    
    data = {}
    
    with open(full_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            year = row['Year']
            month = row['Month']
            visitors = row['Visitors']
            
            if year not in data:
                data[year] = {}
                
            data[year][month] = visitors
            
    return data

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month
    '''
    annual_max = []
    
    for year, months in d.items():
        max_visitors = -1
        max_month = None
        
        for month, visitors in months.items():
            visitors_count = int(visitors)
            if visitors_count > max_visitors:
                max_visitors = visitors_count
                max_month = month
                
        annual_max.append((year, max_month, max_visitors))
    
    return annual_max

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year
    '''
    month_avg = {}
    
    for year, months in d.items():
        total_visitors = 0
        month_count = len(months)
        
        for visitors in months.values():
            total_visitors += int(visitors)
        
        avg_visitors = total_visitors / month_count
        month_avg[year] = round(avg_visitors)
    
    return month_avg

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
