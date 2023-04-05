# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:55:53 2023

@author: neham
"""
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


def data_frame(file):
    """
    The function accepts a file and reads it into a pandas DataFrame and 
    cleans it and transposes it. It returns the cleaned original and 
    transposed DataFrame.


    Parameters
    ----------
    file : string
        The file name to be read into DataFrame.

    Returns
    -------
    df_clean : pandas DataFrame
        The cleaned version of the ingested DataFrame.
    df_t : TYPE
        The transposed version of the cleaned DataFrame.

    """

    # reads in an excel file
    if ".xlsx" in file:
        df = pd.read_excel(file, index_col=0)
    # reads in a csv file
    elif ".csv" in file:
        df = pd.read_csv(file, index_col=0)
    else:
        print("invalid filetype")
    # cleans the DataFrame
    df_clean = df.dropna(axis=1, how="all").dropna()
    # transposes the cleaned DataFrame
    df_t = df_clean.transpose()

    return df_clean, df_t


# list of countries and years needed
countries = ['Japan', 'Brazil', 'China', 'India', 'United States',
             'United Kingdom', 'Australia', 'Germany']
years = ['2004', '2006', '2008', '2010', '2012', '2014']


"""
Plots the bar graph of the Total greenhouse gas emissions by the countries
over a decade from 2004 to 2014.
"""
# calls the data_frame() function to ingest the needed file
df_g, df_g_t = data_frame("Total greenhouse gas emissions.csv")

# extracts the needed data from the original Dataframe into another DataFrame
df_g_count = df_g[years].copy()
df_g_count = df_g_count.loc[df_g_count.index.isin(countries)]
print(df_g_count)

# colors of bars needed for plotting the bar graph
c = ['xkcd:light green', 'xkcd:green', 'xkcd:teal', 'xkcd:turquoise',
     'xkcd:cyan', 'xkcd:sky blue']

# plots the bar graph
df_g_count.plot(kind='bar', width=0.4, figsize=(7, 3), color=c,
                edgecolor='black', fontsize=12)
plt.legend(labels=years)
plt.xticks(range(len(df_g_count.index)), df_g_count.index, fontsize=12)
plt.xlabel('Countries', fontsize=13)
plt.ylabel('Total greenhouse gas emissions\n' + '(kt of CO2 equivalent)',
           fontsize=13)
plt.title('Total Greenhouse gas Emissions', fontsize=15)
plt.savefig("Greenhouse.png", dpi=300)
plt.show()


"""
Plots a bar graph of the Population of the countries over a decade from
2004 to 2014.
"""
# calls the data_frame() function to ingest the needed data
df_pop, df_pop_t = data_frame("Population.csv")

# extracts the needed data from the original Dataframe into another DataFrame
df_pop_count = df_pop[years].copy()
df_pop_count = df_pop_count.loc[df_pop_count.index.isin(countries)]
print(df_pop_count)

# colors of bars needed for plotting the bar graph
co = ['xkcd:purple', 'xkcd:royal purple', 'xkcd:violet',
      'xkcd:dark lavender', 'xkcd:lavender', 'xkcd:light purple']

# plots the bar graph
df_pop_count.plot(kind='bar', figsize=(7, 3), width=0.4, color=co,
                  edgecolor='black', fontsize=12)
plt.legend(labels=years)
plt.xticks(range(len(df_pop_count.index)), df_pop_count.index, fontsize=12)
plt.xlabel('Countries', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.title('Total Population', fontsize=15)
plt.savefig("Population.png", dpi=300)
plt.show()


# list of the years needed
years2 = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
          '2012', '2013', '2014']


"""
Plots the line plot of the Fossil fuel energy consumption of the countries
over a decade from 2004 to 2014.
"""
# calls the data_frame() function to ingest the needed data
df_f, df_f_t = data_frame("Fossil fuel energy consumption.csv")

# extracts the needed data from the original Dataframe into another DataFrame
df_f_count = df_f_t[countries].copy()
df_f_count = df_f_count.loc[df_f_count.index.isin(years2)]
print(df_f_count)

# plots the line plot
plt.plot(df_f_count.index, df_f_count[countries])
plt.ylim(40, 100)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Fossil fuel energy consumption\n' + '(% of total)', fontsize=14)
plt.title('Fossil Fuel Energy Consumption', fontsize=14)
plt.legend(countries, loc='best', bbox_to_anchor=(-0.4, 0.8, 0.2, 0.2))
plt.savefig("Fossil.png", dpi=300)
plt.show()


"""
Plots the line plot of the Renewable energy consumption of the countries 
over a decade frome 2004 to 2014.
"""
# calls the data_frame() function to ingest the needed data
df_r, df_r_t = data_frame("Renewable energy consumption.csv")

# extracts the needed data from the original Dataframe into another DataFrame
df_r_count = df_r_t[countries].copy()
df_r_count = df_r_count.loc[df_r_count.index.isin(years2)]
print(df_r_count)

# plots the line graph
plt.plot(df_r_count.index, df_r_count[countries])
plt.xlabel('Years', fontsize=14)
plt.ylabel('Renewable energy consumption\n'
           + '(% of total energy consumption)', fontsize=14)
plt.title('Renewable Energy Consumption', fontsize=14)
plt.legend(countries, loc='best', bbox_to_anchor=(-0.4, 0.8, 0.2, 0.2))
plt.savefig("Renewable.png", dpi=300)
plt.show()


"""
Plots the line plot of the GDP per capita of the countries over a decade
from 2004 to 2014.
"""
# calls the data_frame() function to ingest the needed data
df_gdp, df_gdp_t = data_frame("GDP per capita.csv")

# extracts the needed data from the original Dataframe into another DataFrame
df_gdp_count = df_gdp_t[countries].copy()
df_gdp_count = df_gdp_count.loc[df_gdp_count.index.isin(years2)]
print(df_gdp_count)

# plots the line graph
plt.plot(df_gdp_count.index, df_gdp_count[countries])
plt.xlabel('Years', fontsize=14)
plt.ylabel('GDP per capita(in $US)', fontsize=14)
plt.title('GDP per Capita', fontsize=14)
plt.legend(countries, loc='best', bbox_to_anchor=(-0.4, 0.8, 0.2, 0.2))
plt.savefig("GDP.png", dpi=300)
plt.show()


"""
Extracts specific data and creates a DataFrame for China from
various Dataframes.
"""
# extracts the specific data of the country China from various DataFrames
df_g_china = df_g_t["China"].copy()
df_g_china = df_g_china.loc[df_g_china.index.isin(years2)]

df_pop_china = df_pop_t['China'].copy()
df_pop_china = df_pop_china.loc[df_pop_china.index.isin(years2)]

df_f_china = df_f_count['China']

df_r_china = df_r_count['China']

df_gdp_china = df_gdp_count['China']


# Creates a DataFrame for the country China with the specific columns
df_china = pd.DataFrame({'Greenhouse gas': df_g_china,
                         'Population': df_pop_china,
                         'Fossil fuel': df_f_china,
                         'Renewable energy': df_r_china,
                         'GDP per capita': df_gdp_china})
print(df_china)

# Uses the describe() method to obtain stastical results
des_ch = df_china.describe()
print(des_ch)

# Obtains the Kendall's correlation between various indicators
ch_corr = df_china.corr(method='kendall')
print(ch_corr)

# Obtains the skewness of the greenhouse gas emissions data of China
print("Skewness of Greenhouse gas emission of China:",
      stats.skew(df_china["Greenhouse gas"]))

# Obtains the kurtosis of the greenhouse gas emissions data of China
print("Kurtosis of Greenhouse gas emissions of China:",
      stats.kurtosis(df_china["Greenhouse gas"]))


"""
Obtains the mean value of the specific indicators for the selected 
countries
"""
df_g_mean = df_g_count.mean(axis=1)
print(df_g_mean)
df_pop_mean = df_pop_count.mean(axis=1)
print(df_pop_mean)
df_f_mean = df_f_count.mean()
print(df_f_mean)
df_r_mean = df_r_count.mean()
print(df_r_mean)
df_gdp_mean = df_gdp_count.mean()
print(df_gdp_mean)
