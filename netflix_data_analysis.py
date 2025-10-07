#importing neccesarry libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading The dataset
df = pd.read_csv("C:\\Users\\Admin\\Downloads\\Netflix Dataset.csv")
print(df)

#FIRST STEP IS Data Understanding
 #1) What is the size of the dataset?
# (How many rows and columns does it have?)

df.size

# What are the different columns available in the dataset?
# (What kind of information does each column hold?)
df.columns
# What are the data types of each column?
# (Are they numerical, categorical, or datetime?)
df.dtypes
# Does the dataset have any missing values?
# (If yes, how many in each column?)
df.isnull()
df.isnull().sum()
# Are there any duplicate records in the dataset?
df[df.duplicated()]

# Data Cleaning

# Check Wether duplicates values are removed are not
df[df.duplicated()]

#Drop Duplicated Values 
df.drop_duplicates(inplace = True)

# What is the overall summary of the dataset?
# (Basic statistics like counts, unique values, min/max, etc.)
df.describe(include = "all")

#Which columns have missing or null values, and how should they be handled?

df.isnull().sum()

# Showing Null Values With The Heatmap
sns.heatmap(df.isnull())

# We Dont Know The Director Insted Removing This We are Replacing Null Value With The
# Unknown director
df['Director'].fillna("Unknown Director", inplace = True)

df['Cast'].fillna("Unknown Cast" , inplace = True)

df['Country'].fillna("Unknown Country" , inplace = True)

df.dropna(inplace = True)
#Are data types correct, or do we need to convert
#  (e.g., Release_Date to datetime, Duration to numeric)?
df.dtypes
# We have to convert dtype of release from Object To Datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'], format = "mixed")

# EDA


df['Category'].value_counts()
df['Category'].value_counts().plot(kind='bar', title='Movies vs TV Shows')

df['Release_Date'].value_counts().sort_index().plot(kind='line', title='Content Added Over Years')
#importing neccesarry libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading The dataset
df = pd.read_csv("C:\\Users\\Admin\\Downloads\\Netflix Dataset.csv")
print(df)

#FIRST STEP IS Data Understanding
 #1) What is the size of the dataset?
# (How many rows and columns does it have?)

df.size

# What are the different columns available in the dataset?
# (What kind of information does each column hold?)
df.columns
# What are the data types of each column?
# (Are they numerical, categorical, or datetime?)
df.dtypes
# Does the dataset have any missing values?
# (If yes, how many in each column?)
df.isnull()
df.isnull().sum()
# Are there any duplicate records in the dataset?
df[df.duplicated()]

# Data Cleaning

# Check Wether duplicates values are removed are not
df[df.duplicated()]

#Drop Duplicated Values 
df.drop_duplicates(inplace = True)

# What is the overall summary of the dataset?
# (Basic statistics like counts, unique values, min/max, etc.)
df.describe(include = "all")

#Which columns have missing or null values, and how should they be handled?

df.isnull().sum()

# Showing Null Values With The Heatmap
sns.heatmap(df.isnull())

# We Dont Know The Director Insted Removing This We are Replacing Null Value With The
# Unknown director
df['Director'].fillna("Unknown Director", inplace = True)

df['Cast'].fillna("Unknown Cast" , inplace = True)

df['Country'].fillna("Unknown Country" , inplace = True)

df.dropna(inplace = True)
#Are data types correct, or do we need to convert
#  (e.g., Release_Date to datetime, Duration to numeric)?
df.dtypes
# We have to convert dtype of release from Object To Datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'], format = "mixed")

# EDA


df['Category'].value_counts()
df['Category'].value_counts().plot(kind='bar', title='Movies vs TV Shows')

df['Release_Date'].value_counts().sort_index().plot(kind='line', title='Content Added Over Years')

# Top 10 Countries with most content
df['Country'].value_counts().head(10).plot(kind='barh', title='Top 10 Countries')



