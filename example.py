# make_data.py
# Get some example data
from datetime import datetime
import random
import pandas as pd
from faker import Factory

faker = Factory.create()
status = 'created,delivered,returned'.split(',')

def date_between(d1, d2):
    f = '%b%d-%Y'
    return faker.date_time_between_dates(datetime.strptime(d1, f), datetime.strptime(d2, f))

def fakerecord():
    return {'user_id': faker.numerify('######'),  # random number eg:235533
            'city': faker.city(),  # random cities
            'product_id': 'random_product',  # different products
            'product_category': 'random_category',  # different categories
            'origin_city': faker.city(),  # random metro cities
            'dispatch_id': faker.numerify('##'),  # id's eg:1,20,28,27
            'dispatch_date': date_between('mar01-2015', 'mar15-2015'),  # datetime between mar01-2015 to mar15-2015
            'delivery_status': random.choice(status),  # created,delivered,returned
            'actual_delivery_date': date_between('mar16-2015', 'mar30-2015'),  # datetime between mar16-2015 to mar30-2015
            'promised_delivery_date': date_between('mar25-2015', 'apr06-2015'),  # datetime between mar25-2015 to Apr6-2015
            }

def fakedataset():
    return pd.DataFrame([fakerecord() for _ in range(10)])
