def check_year_columns(df):
    """
    This function will compare the YearEnd and YearStart columns in the designated dataframe to check if they are the same value
    It will only print out a statement confirming they are the same value or that they are not the same value   
    
    For the parameter df enter in the name of the dataframe that you want to be checked
    """


    #This code will show me if the YearStart column and the YearEnd column are all the same or not
    same_years = (df['YearStart'] == df['YearEnd']).all()

    if same_years:
        print("The 'YearStart' and 'YearEnd' columns have the same values in all rows.")
    else:
        print("The 'YearStart' and 'YearEnd' columns do not have the same values in all rows.")
        df['YearDifference'] = df['YearEnd'] - df['YearStart']
    return df

def group_sort(df):
    """
    Uses Groupby to group all the columns together first by Question
    then by StratificationCategory1, Stratifcation1 and last by LocationAbbr
    It then uses a lambda function to sort the values by "YearEnd"

    for the parameter enter the disired dataframe
    Returns 
    """    
    df = df.groupby(['YearEnd','Question',]).apply(
        lambda x: x.sort_values(by = 'YearEnd')).reset_index(drop = True)
    return df

def question_us_overall(df):
    """
    
    
    
    
    """
    questions = df['Question'].unique().tolist()


    dfs = {}

    for question in questions:
        filter_df = df.loc[df['Question'] == question]\
            .loc[df['LocationAbbr'] == 'US']\
            .loc[df['StratificationCategory1'] == 'Overall']
        if not filter_df.empty:
            dfs[question] = filter_df
    return dfs


def datavalue_type_filter(dfs):
    """
    
    
    """
    target_data_type = ['Average Annual Number','Age-adjusted Prevalence', 'Age-adjusted Mean']

    datavalue_filter_dfs = {}

    for df_name, df in dfs.items():
        if any(df['DataValueType'].isin(target_data_type)):
            datavalue_filter_df = df[df['DataValueType'].isin(target_data_type)]
        else:
            datavalue_filter_df = df
        datavalue_filter_dfs[df_name] = datavalue_filter_df
    return datavalue_filter_dfs


import matplotlib.pyplot as plt
def plot_graph_dict_red(dfs, figsize = (10, 6)):

    """
    
    
    """
    graphs = {}

    for df_name, df in dfs.items():
        fig, ax = plt.subplots(figsize = figsize)

        for datavalue_type, group_df in df.groupby('DataValueType'):
            label = f'Data Points: {group_df["DataValue"].count()}\nData Value Type: {datavalue_type}'
            if 'YearDifference' in df.columns and df['YearDifference'].max() > 0:
                year_diff = group_df['YearDifference'].unique()
                label += f'\nNumber of Years in 1 Data Point: {year_diff}'

            ax.plot(group_df['YearEnd'], group_df['DataValue'], label=label, color = 'red')


            for year, value in zip(df['YearEnd'], df['DataValue']):
                ax.axvline(x=year, ymin=0, ymax=value / df['DataValue'].max(), linestyle='--', color='gray', alpha=0.5)

        ax.set_xlabel('YearEnd')
        ax.set_ylabel('DataValue')
        ax.set_title(df_name.replace('_', ' ').title())
        ax.legend()
        graphs[df_name] = fig
    return graphs




import matplotlib.pyplot as plt
def plot_graph_dict_green(dfs, figsize = (10, 6)):

    """
    
    
    """
    graphs = {}

    for df_name, df in dfs.items():
        fig, ax = plt.subplots(figsize = figsize)

        for datavalue_type, group_df in df.groupby('DataValueType'):
            label = f'Data Points: {group_df["DataValue"].count()}\nData Value Type: {datavalue_type}'
            if 'YearDifference' in df.columns and df['YearDifference'].max() > 0:
                year_diff = group_df['YearDifference'].unique()
                label += f'\nNumber of Years in 1 Data Point: {year_diff}'

            ax.plot(group_df['YearEnd'], group_df['DataValue'], label=label, color = 'green')


            for year, value in zip(df['YearEnd'], df['DataValue']):
                ax.axvline(x=year, ymin=0, ymax=value / df['DataValue'].max(), linestyle='--', color='gray', alpha=0.5)

        ax.set_xlabel('YearEnd')
        ax.set_ylabel('DataValue')
        ax.set_title(df_name.replace('_', ' ').title())
        ax.legend()
        graphs[df_name] = fig
    return graphs



def customize_plot(graph, color='blue'):
    """
    
    
    
    """
    ax = graph.get_axes()[0]  # Get the first (and only) axes
    for line in ax.get_lines():
        if line.get_linestyle() == '-':  # Check if it's the main line
            line.set_color(color)  # Change the main line color
    # Update the legend to reflect the new color
    handles, labels = ax.get_legend_handles_labels()
    for handle in handles:
        if isinstance(handle, plt.Line2D):
            handle.set_color(color)
    ax.legend(handles, labels)