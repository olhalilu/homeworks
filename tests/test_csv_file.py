import pytest
import os
import csv


file_name = '../homeworks/cl_account_sample.csv'
expected_header = ['ParentId', 'AccountNumber',
                   'AnnualRevenue', 'BillingCountry', 'BillingCity', 'BillingState',
                   'BillingPostalCode', 'BillingStreet', 'Fax', 'Industry', 'Name',
                   'NumberOfEmployees', 'Phone', 'Rating']

def test_csv_file_exist():
    assert os.path.exists(file_name),'file not found at this path'

def test_file_not_epmty():
    assert os.path.getsize(file_name) > 0,'file is empty'

def test_csv_file_header():
    with open(file_name, "r", encoding="utf-8-sig") as csv_file:


        reader = csv.reader(csv_file)
        rows = list(reader)
        header = rows[0]

        assert header == expected_header,'header missmatch'
        assert len(header) == len(expected_header),'number of header values missmatch'
def test_columns_count():
    with open(file_name, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        header = rows[0]

        for i in rows:
            assert len(i)==len(expected_header),f'missmatch count of column and values in {i} row'

def test_count_file():
    expected_count = 10
    with open(file_name, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        content = rows[1:]
        assert len(content) == expected_count,'wrong row count'

def test_pk_not_null():
    with open(file_name, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        for i in rows[1:]:
            assert i[1] not in (" ","",'NULL','Null'), 'null in PK column'


