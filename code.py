import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess(data):
    '''Preprocess the dataset to rename the target column into an easily-readable format.'''
    data = data.rename(columns={'Deaths - Road injuries - Sex: Both - Age: All Ages (Number)': 'Deaths'})
    #print(data.head())
    return data

def yearly_count(data):
    '''Wordwide count of deaths on a yearly basis'''
    plt.xticks(rotation=90)
    sns.barplot(data=data, x="Year", y="Deaths")
    plt.show()

def countries_count(data):
    '''Wordwide count of deaths on a category basis - Showing first 10 categories'''
    plt.xticks(rotation=90)
    df = data.drop(["Code"],axis=1)
    df = df.groupby(["Entity"])["Deaths"].sum().sort_values(ascending=False)[:10]
    sns.barplot(df.index, df.values)
    plt.show()
    
def us_uk_india_count(data):
    '''Wordwide count of deaths on a yearly basis'''
    sns.lineplot(data=data[data['Code'].isin(['IND', 'GBR', 'USA'])], x="Year", y="Deaths", hue="Entity")
    plt.show()

def main():
    '''This is the entry point of the program. We read the dataset and extract relevant features before further analysing using appropriate functions.'''
    data = pd.read_csv("road-traffic-deaths.csv")
    data = preprocess(data)
    yearly_count(data)
    countries_count(data)
    us_uk_india_count(data)

if __name__ == "__main__":
    main()
