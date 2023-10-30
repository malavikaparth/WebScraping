import pandas as pd
from sklearn import datasets
import missingno as msno

diabetes = datasets.load_diabetes()
# Create a Pandas DataFrame from the Iris data
diabetes_df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
print(diabetes_df.info())
'''
#removing cabin info as it will not probable show the survival rate
titanic.drop('Cabin', axis=1, inplace=True) 

#Filling missing values with mean, median or mode
Impute with Mean: Use mean imputation when dealing with continuous numerical data, such as age, income, or any other data that can take on a wide range of numeric values.
Median imputation is a good choice when dealing with continuous numerical data that is skewed or contains outliers.
Mode imputation is typically used for categorical or discrete data where you have categories or labels. Examples include imputing missing values in a "gender" column with "male" or "female."

titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)
titanic['Fare'].fillna(titanic['Fare'].mean(), inplace=True)

#Checking for duplicates This means no duplicates
duplicates_titanic = titanic[titanic.duplicated()]
print(duplicates_titanic)
'''

msno.matrix(diabetes_df)