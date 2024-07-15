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

## Results: 

### Mental Health Indicators

Figure 1: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/ty_branch/At%20Least%2014%20Recent%20Mentally%20Unhealthy%20Days%20Among%20Women%20Aged%2018-44%20Years.png)
    Age-adjusted Mean: adjusted for variations in age distribution across different demographic groups
    Mentally Unhealthy Days: includes stress, depression, and problems with emotions
    DataValue: shows on average how many mentally unhealthy days in the past 30 days an adult in the US had
    YearEnd: represents the full year the data was collected from january 1rst to December 31 st 
    Indicator is illustrated in red to indicate Negative results


Figure 2: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/patricia_branch/ty_s_slide_Mental%20health.png)
    Crude Prevalence: a raw estimate without adjusting for other factors like age distribution. These numbers are shown in percentages %
    Recent: past 30 days
    Mentally Unhealthy Days: includes stress, depression, and problems with emotions
    YearEnd: represents the full year the data was collected from january 1rst to December 31rst 
    Indicator is illustrated in red to indicate Negative results

Figure 3: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Asthma%20Mortality%20Rate.png)

    Crude Prevalence: a raw estimate without adjusting for other factors like age distribution. These numbers are shown in percentages %
    Recent: past 30 days
    Mentally Unhealthy Days: includes stress, depression, and problems with emotions
    YearEnd: represents the full year the data was collected from january 1rst to December 31rst 
    Indicator: Negative


### Tobacco Indicators

Figure 4: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/patricia_branch/ty_s_slide_pneu_vax.png)
    Age-adjusted Prevalence: adjusted for variations in age distribution across different demographic groups, shown as a percentage of the target group
    Noninstitutionalized: not in staying in hospitals, nursing homes, or other similar facilities
    Pneumococcal Vaccinations: lowers risk of pneumonia


Figure 5: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/ty_branch/Current%20Cigarette%20Smoking%20Among%20Women%20Aged%2018-44%20Years.png)

    Datavalue: showing age_adjusted percentage(prevalence) of current smokers in the US 
    Indicator is positive


Figure 6:

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/ty_branch/Quit%20Attempts%20In%20The%20Past%20Year%20Among%20Current%20Smokers.png)

    Data Value: showing age-adjusted percentage (prevalence)  for quit attempts amongst smokers
    Indication: Undecided
    Indication count:
    Positive: 7
    Negative:2(vaccinations)
    Undecided: 1
    Missing: 6

### Asthma Health Indicators

Figure 7: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Asthma%20Prevalence%20Among%20Women%20Aged%2018-44%20Years.png)

    Age-adjusted Prevalence: adjusted for variations in age distribution across different demographic groups, shown as a percentage of the target group
    Over the years we see an increase in Asthma prevalence among young women. Though what we find interesting is a dip in 2016 where in other indicators show an increased vaccination rate. Is it a possible cause for the drop?
    Indication: negative


Figure 8: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Influenza%20Vaccination%20Among%20Noninstitutionalized%20Adults%20Aged%2018-64%20Years%20With%20Asthma.png)

    Age-adjusted Prevalence: adjusted for variations in age distribution across different demographic groups, shown as a percentage of the target group
    This indicator confirms influence vaccines were up in 2016 which could have led to the decrease in asthma cases and the decrease in 2018 could be the cause of an increase in Asthma cases.
    Indication: positive


### Chronic Obstructive Pulmonary Indicators

Figure 9: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Prevalence%20Of%20Activity%20Limitation%20Among%20Adults%20%3E%3D%2018%20With%20Diagnosed%20Chronic%20Obstructive%20Pulmonary%20Disease.png)

    Age-adjusted Prevalence: adjusted for variations in age distribution across different demographic groups, shown as a percentage of the target group
    Indication: negative

Figure 10:

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Prevalence%20Of%20Activity%20Limitation%20Among%20Adults%20%3E%3D%2045%20Years%20With%20Diagnosed%20Chronic%20Obstructive%20Pulmonary%20Disease.png)

    Age-adjusted Prevalence: adjusted for variations in age distribution across different demographic groups, shown as a percentage of the target group
    Indication: negative

Figure 11: 

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Prevalence%20Of%20Current%20Smoking%20Among%20Adults%20%3E%3D%2018%20With%20Diagnosed%20Chronic%20Obstructive%20Pulmonary%20Disease.png)

Figure 12:

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/dapo_branch/Prevalence%20Of%20Current%20Smoking%20Among%20Adults%20%3E%3D%2045%20Years%20With%20Diagnosed%20Chronic%20Obstructive%20Pulmonary%20Disease.png)

### Alcohol Chronic Disease Indicator

Figure 13:

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/patricia_branch/ID_s_alcohol_b4_preg.png)

Figure 14:

![](https://github.com/godzown82/analysis_of_us_chronic_diseases/blob/patricia_branch/ID_s_bindge_drinking.png)

## Conclusions:
