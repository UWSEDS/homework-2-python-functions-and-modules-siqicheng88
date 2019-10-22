import pandas as pd

## Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov
def python_reader(url,name):
    df = pd.read_csv(url, header = None, names = name )
    return df

names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Class'] 
python_reader('http://mlr.cs.umass.edu/ml/machine-learning-databases/iris/iris.data',names)

## Create the function test_create_dataframe
def test_create_dataframe(df, colume_name):
    if list(df.columns.values) == colume_name and check_the_type(df,colume_name) and len(df.index) > 20:
            return True
    return False

def check_the_type(df,colume_name):
    if all (df[col].dtypes == df.dtypes[0] for col in df.columns):
        return True 
    return False
test_create_dataframe(df, names)
