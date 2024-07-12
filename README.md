# <center>Analysis of United States Chronic Disease Indicators<center>




# Overview: 
This data set shows data collected by the CDC from 2001 to 2021 through various vetted sources to give numerous data values corresponding with a specific chronic disease indicator(labeled as Topic), which is broken down into subcategories(labeled Question). It has multiple additional columns that allow you to filter the data even further. We chose to filter the data by the United states as a whole, as well as the overall target group(labeled stratificationCategorey1), instead of separating by race or gender.  We then plotted these data values for each Question within their respective Topics. This gave us overall general trends for each indicator allowing us to start understanding what this data was capable of showing us. This type of analysis is critical to understanding public health practices and their overall success and/or shortcomings.


## Data Scientists and Topics

Ty Whittlesey: Mental Health, Tobacco, Cancer

Patricia Squitiero: Diabetes, Overarching Diseases

Adedapo Owolabi: Asthma, Chronic Pulmonary

Brian Willery: Chronic Kidney, Cardiovascular Disease

Idowu Lawal: Alcohol, Arthritis

### Full list of Topics in original Dataset
* Alcohol
* Arthritis
* Asthma
* Cancer
* Cardiovascular Disease
* Chronic Kidney Disease
* Chronic Obstructive Pulmonary Disease
* Diabetes
* Disability
* Immunization
* Mental Health
* Nutrition, Physical Activity and Weight Status
* Older Adults
* Oral Health
* Overarching Conditions
* Reproductive Health
* Tobacco

The link to the full csv used in our analysis:
https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi


# Installation:

To run the analysis you should have python installed on your computer using pip
You will also need to download the CSV file from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi if you want to run the data analysis on the full uncleaned data in group2_project.ipynb file.

1. clone repository:
```bash
    git clone https://github.com/godzown82/analysis_of_us_chronic_diseases.git
```
2. Install the requried python packages:
```bash
    pip install -r requirements.txt
```
Install notes: * Using python dev enviorment created from installing anaconda as Kernel
* python version 3.10.14
* Visual Studio Code
* Jupyter Notebooks
* Pandas
* numpy
* matplotlib.pyplot

## Usage: 

The analysis is performed using Jupyter notebooks; launch Jupyter Notebooks and add the appropiate files (eg. tobacco.ipynb, tobbacco.csv, & cdindicatorFn.py)
Note depending on your setup you might have to change the path on read_csv code shown below
```
    tobacco_df = pd.read_csv('Tobacco.csv')
```
All notebooks include notes above their code for explanation purposes, main functions can be found in the cdindicatorFn.py file

### key codes for group2_project.ipynb
After you create the dataframe named data using the read_csv function the codes shown below are the only relevant code to understanding how the csv included were created. (again to run these codes you must first download the original csv provided with the link above or in this ipynb file and set your path accordingly)
```
data_drop = data.copy()
data_drop['OriginalDataValue'] = data_drop['DataValue']
data_drop['DataValue'] = pd.to_numeric(data_drop['DataValue'], errors='coerce')
non_convertible_rows = data_drop[data_drop['DataValue'].isna() & data_drop['OriginalDataValue'].notna()]
data_drop = data_drop.dropna(subset=['DataValue'])
```
This converts the DataValue column to numeric values, deletes rows without values in Datavalue, and then removes and stores rows that could not be converted into numeric values into a separate dataframe

```
clean_data_df = data_drop[['YearStart', 'YearEnd', 'LocationAbbr', 'Topic',
                        'Question','DataValue','DataValueUnit','DataValueType','DatavalueFootnote','LowConfidenceLimit',
                        'HighConfidenceLimit','StratificationCategory1','Stratification1' ]]
```
This is the data frame we used to create our individual csvs, which removes columns that have no values in them or redundant columns

```
for topic, df in clean_data_df.groupby('Topic'):
    df.to_csv(f'{topic}.csv', index=False)
non_convertible_rows.to_csv(f'nonnumerical_data.csv', index = False)
```
This writes and stores separate csv files for each topic and then creates a another csv with the data frame that contains the the rows from the DataValue column that can't be converted to numeric values. NOTE do not need to run this file because the cloned repository already includes all the csv files that this code would create

### Key Functions

These functions can be used on all of the ipynb files except group2_project.ipynb and cannot be used on a newly created ipynb file that creates a dataframe with nonnumerical_data.csv file
* check_year_columns(df)
* group_sort(df)
* question_us_overall(df)
* datavalue_type_filter(dfs)
    Note: You can add or change the targeted list of Data value Types to alter the Datavalue being graphed. list to be altered shown below for cdindicatorFN.py file
```
target_data_type = ['Average Annual Number','Age-adjusted Prevalence', 'Age-adjusted Mean']
```
* plot_graph_dict_red(dfs, figsize = (10, 6))
* plot_graph_dict_green(dfs, figsize = (10, 6))
* change_plot_color(graph, color='blue')
    Note: to use this function you must use the key of the desired dataframe in the dictionary created in the either of the 2 previous functions ploting the graphs, which is stored as the full question. example below from the tobacco.ipynb file
```
change_plot_color(tobacco_graphs[
    'Quit attempts in the past year among current smokers'], color = 'blue')
```

All of these functions and further explaination can be found in the cdindicatorFn.py file

## Results / Conclusions:
### Asthma and Pulmonary diseases findings:
Looking at the Asthma prevalance among young women Aged 18-44 yrs fig 
![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Asthma%20Mortality%20Rate.png)
