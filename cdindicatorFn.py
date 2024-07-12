

def check_year_columns(df):
    """
    This function will compare the YearEnd and YearStart columns in the designated dataframe to check if they are the same value
    It will print out a statement confirming they are the same value or that they are not the same value
    it creates a new column that shows the difference between YearStart and YearEnd if they are not the same values
    Returns an updated df with the new column YearDiffernce added to the data frame   
    
    For the parameter df enter in the name of the dataframe that you want to be checked
    """


    #creates a variable that returns a boolean value of true if the YearStart values are the same as the YearEnd columns in all rows
    #returns False if they are not the same in all rows
    same_years = (df['YearStart'] == df['YearEnd']).all()
    #if prints out the if the boolean value is true 
    if same_years:
        print("The 'YearStart' and 'YearEnd' columns have the same values in all rows.")
    #esle prints out if the boolean value is false and then creates the a new column to show the difference in the values
    else:
        print("The 'YearStart' and 'YearEnd' columns do not have the same values in all rows.")
        df['YearDifference'] = df['YearEnd'] - df['YearStart']
    #returns unaltered df if true and altered df with new column if false
    return df

def group_sort(df):
    """
    Uses Groupby to group all the columns together first by YearEnd
    then by Question
    It then uses a lambda function to sort the values by "YearEnd" from least to greatest

    for the parameter enter the disired data frame
    Returns the new grouped and sorted data frame
    """    
    df = df.groupby(['YearEnd','Question',]).apply(
        lambda x: x.sort_values(by = 'YearEnd')).reset_index(drop = True)
    return df

def question_us_overall(df):
    """
    uses a for loop to seperate dataframe by question with each dataframe filtered to only include
    the US from LocationAbbr and overall from StratificationCategory1 and then stores those filtered dataframes
    into a dictionary. if a particular quesition doesnt have data for the US and/or an overall strartification category
    the questions dataframe is excluded from the dictionary

    parameters: enter desired df to be filtered
    returns dfs (a dictionary of filtered data frames, seperated by question)
    """
    #creates a list with all the unique questions
    questions = df['Question'].unique().tolist()

    #creates emtpty dictionary to store filtered dataframes
    dfs = {}

    #creates question to itterate through questions list to create multiple filtered data frames using the loc funtction
    for question in questions:
        filter_df = df.loc[df['Question'] == question]\
            .loc[df['LocationAbbr'] == 'US']\
            .loc[df['StratificationCategory1'] == 'Overall']
        # if not statement creating the condition that the dataframe must have values to be stored in the dictionary
        if not filter_df.empty:
            dfs[question] = filter_df #if dataframe has values it is stored in the dictionary with question as the key
    return dfs #returns dictionary of dataframes with values


def datavalue_type_filter(dfs):
    """
    includes a list of target data type values from DataTypevalues found in earlier exploration
    creates a dictionary to store filtered dataframes
    uses a for loop to use the target list to filter the Data values to the desired Data Type

    parametes: enter in dictionary of dataframes
    returns datavalue_filter_dfs (a dictionary of filtered dataframes)
    """
    #creates list of manually entered in data type values discovered from there respective ipynb files when necessary
    target_data_type = ['Average Annual Number','Age-adjusted Prevalence', 'Age-adjusted Mean', 'Age-adjusted Rate']

    #creates empty dictionary to store filtered dataframes
    datavalue_filter_dfs = {}

    #starts a loop to iterate over items in dictionary with df_name as key and df as corresponding dataframe
    for df_name, df in dfs.items():
        if any(df['DataValueType'].isin(target_data_type)): #checking to see if DataValueType column has values from list
            datavalue_filter_df = df[df['DataValueType'].isin(target_data_type)] #if true sets DataTypeValue column to list value
        
        else: # if not true stores unaltered dataframe
            datavalue_filter_df = df
        datavalue_filter_dfs[df_name] = datavalue_filter_df #completes full dictionary of altered and unaltered dataframes and df_name keeps original keys
    return datavalue_filter_dfs


import matplotlib.pyplot as plt    #Must have import on py file for function to work on ipynb file
def plot_graph_dict_red(dfs, figsize = (10, 6)):

    """
    uses for loop to create individual line graphs based on each dataframe w/in the dictionary
    creates a new dictionary graphs to store the graphs in
    YearEnd on the x axis and Datavalue on the Y axis
    It turns all the line graphs red (use if majority of your trends are negative)
    labels: show how many data values are plotted
            shows Data value type used for the x axis
            for dataframes with Yeardiffernce column it will display the amount of years average together in each data point plotted

    Parmeters: enter in the dictionary of data frames with cleaned Datavalue Types
    Returns: graphs (a dictionary of graphs for each individual question)

    """
    #creates empty dictionary to store the graphs
    graphs = {}

    #starts a loop with a key and corresponding dataframe to iterate over items in dfs
    for df_name, df in dfs.items():
        #creats a new figure and set of subplots 
        # variable graph is a figure object where the plot will be drawn
        # variable axis is an axes object that represents the actual data that will be plotted
        graph, axis = plt.subplots(figsize = figsize)

        #nested loop that groups by data value type an iterates over the groups
        for datavalue_type, group_df in df.groupby('DataValueType'):
            #creates labels for each group with how many Datavalues used in graph and displays datavalue type
            label = f'Data Points: {group_df["DataValue"].count()}\nData Value Type: {datavalue_type}'
            # if has Yeardifference column adds label for how many years included in plotted point
            if 'YearDifference' in df.columns and df['YearDifference'].max() > 0:
                year_diff = group_df['YearDifference'].unique()
                label += f'\nNumber of Years in 1 Data Point: {year_diff}'
            #plots each group_df by Yearend y axis and datavalue on x axis
            axis.plot(group_df['YearEnd'], group_df['DataValue'], label=label, color = 'red')

            #zip is a built in python function that combines multiple iterables in a single iterable of tuples
            #zip takes the df["YearEnd"] series and pairs with the corresponding df['DataValue'] series
            for year, value in zip(df['YearEnd'], df['DataValue']):
                #draws vertical lines for each data point extending from the x axis to the data points y value
                axis.axvline(x=year, ymin=0, ymax=value / df['DataValue'].max(), linestyle='--', color='gray', alpha=0.5)

        axis.set_xlabel('YearEnd')
        axis.set_ylabel('DataValue')
        title = df_name.replace('_', ' ').title()
        axis.set_title(title)
        axis.legend()
        #uncomment next line to create image files of graphs
        #graph.savefig(f'{title}.png')
        graphs[df_name] = graph
    return graphs


# plt.savefig(f'{title}.png')
# plt.show()

#import matplotlib.pyplot as plt
import re  # Import regular expressions module only used if you are uncommented code below to create image files
def plot_graph_dict_green(dfs, figsize = (10, 6)):

    """
    uses for loop to create individual line graphs based on each dataframe w/in the dictionary
    YearEnd on the x axis and Datavalue on the Y axis
    It turns all the line graphs green (use if majority of your trends are positive)
    labels: show how many data values are plotted
            shows Data value type used for the x axis
            for dataframes with Yeardiffernce column it will display the amount of years average together in each data point plotted

    Parmeters: enter in the dictionary of data frames with cleaned Datavalue Types
    Returns: graphs (a dictionary of graphs for each individual question)

    """
    #see comments for function plot_graph_dict_red for line by line explanations
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
        title = df_name.replace('_', ' ').title()
        ax.set_title(title)
        ax.legend()
        #uncomment next line to create image files

        # safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
        # fig.savefig(f'{safe_title}.png')
        graphs[df_name] = fig
    return graphs

#import matplotlib.pyplot as plt
def plot_graph_dict_neutral(dfs, figsize = (10, 6)):

    """
    uses for loop to create individual line graphs based on each dataframe w/in the dictionary
    creates a new dictionary graphs to store the graphs in
    YearEnd on the x axis and Datavalue on the Y axis
    It turns all the line graphs blue (use as neutral color or unknown)
    labels: show how many data values are plotted
            shows Data value type used for the x axis
            for dataframes with Yeardiffernce column it will display the amount of years average together in each data point plotted

    Parmeters: enter in the dictionary of data frames with cleaned Datavalue Types
    Returns: graphs (a dictionary of graphs for each individual question)

    """
    #see comments for function plot_graph_dict_red for line by line explanations
    graphs = {}

    for df_name, df in dfs.items():
        fig, ax = plt.subplots(figsize = figsize)

        for datavalue_type, group_df in df.groupby('DataValueType'):
            label = f'Data Points: {group_df["DataValue"].count()}\nData Value Type: {datavalue_type}'
            if 'YearDifference' in df.columns and df['YearDifference'].max() > 0:
                year_diff = group_df['YearDifference'].unique()
                label += f'\nNumber of Years in 1 Data Point: {year_diff}'

            ax.plot(group_df['YearEnd'], group_df['DataValue'], label=label, color = 'blue')


            for year, value in zip(df['YearEnd'], df['DataValue']):
                ax.axvline(x=year, ymin=0, ymax=value / df['DataValue'].max(), linestyle='--', color='gray', alpha=0.5)

        ax.set_xlabel('YearEnd')
        ax.set_ylabel('DataValue')
        ax.set_title(df_name.replace('_', ' ').title())
        ax.legend()
        graphs[df_name] = fig
    return graphs



def change_plot_color(graph, color='blue'):
    """
    Allows you to change the color of individual graphs
    parameters: enter desired graph, and enter color = "desired color"
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
