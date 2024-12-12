import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import windrose
from windrose import WindroseAxes
from tabulate import tabulate

from IPython.display import display, HTML
from matplotlib.cm import ScalarMappable

def load_scada_data(base_path: str) -> dict:
    """Loads and processes SCADA data from multiple CSV files.
    
    Args:
        base_path: Directory path containing CSV files (with trailing /)
    Returns:
        Dict mapping turbine IDs to their DataFrames with UTC timestamps
    """
    
    
    print(f'Loading SCADA signals...')

    dct_scada = {}

    if ('edp' in base_path):

        lst_files = ['Wind-Turbine-SCADA-signals-2016.csv',  # adjust if named differently
                     'Wind-Turbine-SCADA-signals-2017_0.csv']

        if check_xlsx(lst_files):
            return

        df_scada_all = pd.DataFrame()

        #load files into df
        for i, file in enumerate(lst_files, 1):
            df_temp = pd.read_csv(base_path + file, index_col='Timestamp')
            df_temp.index = pd.to_datetime(df_temp.index, utc=True)
            df_scada_all = pd.concat([df_scada_all, df_temp])

        # organize data by turbine 
        for trb_id in np.unique(df_scada_all.Turbine_ID):
            df_turbine = df_scada_all[df_scada_all['Turbine_ID'] == trb_id]
            df_turbine = df_turbine.drop('Turbine_ID', axis='columns')
            df_turbine.index.name = trb_id
            df_turbine['power'] = df_turbine.Grd_Prod_Pwr_Avg
            df_turbine['wind_speed'] = df_turbine.Amb_WindSpeed_Avg
            df_turbine['wind_direction'] = df_turbine.Amb_WindDir_Abs_Avg

            dct_scada[trb_id] = df_turbine[~df_turbine.index.duplicated(keep='first')].sort_index()

    elif ('kelmarsh' in base_path):

        for trb_id in [i for i in range(1, 7)]:

            df_data_all = pd.DataFrame()

            for folder in np.sort(os.listdir(base_path )):
                if ('powercurve' in folder):
                    continue

                for file in np.sort(os.listdir(base_path + f'{folder}/')):
                    if not file.endswith('.csv'):
                        continue
                    if ("Data" in file) & (file.split("_")[3] == str(trb_id)):
                        path_load = base_path + f'{folder}/{file}'

                        df = pd.read_csv(path_load,
                                         skiprows=9,
                                         low_memory=False,
                                         index_col='# Date and time')

                        df_data_all = pd.concat([df_data_all, df], axis=0)

                df_data_all.index = pd.to_datetime(df_data_all.index, utc=True)
                df_data_all = df_data_all[df_data_all['Data Availability'] == 1]
                df_data_all = df_data_all.dropna(axis=1, how='all')
                df_data_all['power'] = df_data_all['Power (kW)']
                df_data_all['wind_speed'] = df_data_all['Wind speed (m/s)']
                df_data_all['wind_direction'] = df_data_all['Wind direction (°)']
                key_ = f'T0{str(trb_id)}'
                dct_scada[key_] = df_data_all

    return dct_scada


def load_scada_logs(base_path) -> dict:
    """
    Load, unify, and process SCADA log files.

    Parameters:
        base_path (str): Base directory path for the log files.

    Returns:
        dict: A dictionary where keys are turbine IDs and values are DataFrames of logs for each turbine.
    """

    print(f'Loading SCADA logs...')

    dct_logs = {}

    if ('edp' in base_path):

        lst_files = ['Wind-Turbines-Logs-2016.csv',  # adjust if named differently
                     'Wind Turbines Logs 2017.csv']

        if check_xlsx(lst_files):
            return

        dct_unify_colnames = dict({'col_time': ['TimeDetected', 'Time_Detected'],
                                   'col_trb_id': ['UnitTitle', 'Turbine_Identifier'],
                                   'col_message': ['Remark', 'Remark']})

        df_logs_all = pd.DataFrame()
        for i, path_ in enumerate(lst_files):
            df_ = pd.read_csv(base_path+path_, index_col=dct_unify_colnames['col_time'][i])
            df_.index = pd.to_datetime(df_.index, utc=True)
            columns = [dct_unify_colnames[col_name][i] for col_name in dct_unify_colnames]
            col_names = [col_name[4:] for col_name in dct_unify_colnames]
            df = pd.DataFrame(np.array(df_[columns[1:]]), 
                              columns=col_names[1:],
                              index=df_.index).sort_index()
            df_logs_all = pd.concat([df_logs_all, df])

        df_logs_all = df_logs_all.loc[pd.notnull(df_logs_all.index)].dropna() # drop all timestamps with missing values

        # sort by turbine
        dct_logs = {trb_id: group for trb_id, group in df_logs_all.groupby('trb_id')}

    elif ('kelmarsh' in base_path):

        for trb_id in [i for i in range(1, 7)]:

            df_data_all = pd.DataFrame()

            for folder in np.sort(os.listdir(base_path)):
                if ('powercurve' in folder):
                    continue

                for file in np.sort(os.listdir(base_path + f'{folder}/')):

                    if not file.endswith('.csv'): #only look at csv's
                        continue
                        
                    if ("Status" in file) & (file.split("_")[2] == str(trb_id)):
                        path_load = base_path + f'{folder}/{file}'

                        df = pd.read_csv(path_load,
                                         skiprows=9,
                                         low_memory=False,
                                         index_col='Timestamp start')

                        df_data_all = pd.concat([df_data_all, df], axis=0)

                df_data_all.index = pd.to_datetime(df_data_all.index, utc=True)
                df_data_all = df_data_all.dropna(axis=1, how='all')
                key_ = f'T0{str(trb_id)}'
                dct_logs[key_] = df_data_all

    return dct_logs


def load_annotations(base_path: str) -> dict:
    """Loads and processes SCADA data from multiple CSV files.

    Args:
        base_path: Directory path containing CSV files (with trailing /)
    Returns:
        Dict mapping turbine IDs to their DataFrames with UTC timestamps
    """

    print(f'Loading annotations...')

    dct_fail = dict()

    if ('edp' in base_path):

        lst_files = ['Historical-Failure-Logbook-2016.csv',  # adjust if named differently
                     'opendata-wind-failures-2017.csv']

        if check_xlsx(lst_files):
            return

        df_fail_all = pd.DataFrame()
        # load files into df
        for i, path_ in enumerate(lst_files):
            df_ = pd.read_csv(base_path + path_, index_col='Timestamp', parse_dates=True)
            df_fail_all = pd.concat([df_fail_all, df_])

        df_fail_all = df_fail_all.dropna().sort_index()

        # sort by turbine
        dct_fail = {trb_id: group for trb_id, group in df_fail_all.groupby('Turbine_ID')}

        return dct_fail


def load_community_annotations(path_: str) -> dict:
    """
    Load and process community annotations from a CSV file.

    Args:
        path_ (str): Path to the community annotation CSV file.

    Returns:
        dict: A dictionary mapping turbine IDs to their respective DataFrames with UTC timestamps.
    """
    print('Loading community annotations...')

    # Read the CSV file into a DataFrame
    df_com_all = pd.read_csv(path_, index_col='annot_id', parse_dates=True).dropna().sort_index()

    # Group by turbine_id and store in a dictionary
    dct_community = {trb_id: group for trb_id, group in df_com_all.groupby('turbine_id')}

    # Extract dataset name from the file path and attach to dataframes
    dct_community['dataset'] = path_.split('/')[-1].split('_')[0]

    for key_ in dct_community.keys():
        if key_=='dataset':
            continue
        df_ = dct_community[key_]
        df_.dataset= dct_community['dataset']
        dct_community[key_] = df_

    return dct_community


def generate_data_overview(dct_scada: dict, dct_logs: dict = {}) -> pd.DataFrame:
    """
    Generate an overview of turbine data metrics from SCADA data.

    Args:
        dct_scada (dict): Dictionary mapping turbine IDs to their SCADA data (pandas DataFrames).
        ar_trb_id (list): List of turbine IDs to process.

    Returns:
        pd.DataFrame: DataFrame summarizing metrics for each turbine, including:
                      - Number of variables and datapoints.
                      - Data timestamps (first and last).
                      - Maximum possible datapoints, missing datapoints, and uptime.
                      - Power produced (MWh).
    """
    print("SCADA DATA OVERVIEW")
    ar_trb_id = list(dct_scada.keys())
    df_data_overview = pd.DataFrame()

    for trb_id in ar_trb_id:
        
        df_scada_trb = dct_scada[trb_id]
        no_vars = len(df_scada_trb.columns)
        no_datapoints = len(df_scada_trb.index)
        time_first, time_last = np.sort(df_scada_trb.index)[0], np.sort(df_scada_trb.index)[-1]

        max_datapoints = (time_last - time_first) / np.timedelta64(10, 'm')
        datapoints_missing = int(max_datapoints - no_datapoints)
        data_uptime = np.round(no_datapoints / max_datapoints, 3)

        time_first_str = pd.to_datetime(time_first).strftime('%Y-%m-%d %H:%M')
        time_last_str = pd.to_datetime(time_last).strftime('%Y-%m-%d %H:%M')

        power_produced = df_scada_trb.power.sum() / 6000

        # Store the metrics in the DataFrame
        df_data_overview.loc[trb_id, '# Variables'] = no_vars
        df_data_overview.loc[trb_id, 'First Timestamp'] = time_first_str
        df_data_overview.loc[trb_id, 'Last Timestamp'] = time_last_str
        df_data_overview.loc[trb_id, '# Datapoints'] = no_datapoints
        df_data_overview.loc[trb_id, 'Datapoints missing'] = int(datapoints_missing)
        df_data_overview.loc[trb_id, 'Data uptime'] = f'{data_uptime*100} %'
        df_data_overview.loc[trb_id, 'Energy Produced Total (MWh)'] = np.round(power_produced)
        df_data_overview.loc[trb_id, 'Capacity Factor)'] = np.round(power_produced/(8760*((time_last - time_first) / np.timedelta64(1, 'Y'))*2),2)
        df_data_overview.loc[trb_id, 'FLH (h)'] = np.round(power_produced/((time_last - time_first) / np.timedelta64(1, 'Y')*2))
        
        if dct_logs!={}:
            df_log_trb = dct_logs[trb_id]
        
            df_data_overview.loc[trb_id, '# Log entries'] = len(df_log_trb)

    max_cols = 4
    if len(df_data_overview.index)<max_cols:
        print(tabulate(df_data_overview.T, headers='keys', tablefmt='pretty'))
    else:
        for i in range((len(df_data_overview.index)//max_cols)+1):
            print(tabulate(df_data_overview.iloc[i*max_cols:(i+1)*max_cols,:].T, headers='keys', tablefmt='pretty'))

        
    return df_data_overview

def get_last_n_logs(df_logs, timestamp, n=5):

    t_start = timestamp-pd.Timedelta(1, 'd')
    t_stop = timestamp
    
    last_n_logs  =df_logs.loc[t_start:t_stop].iloc[-n:,:]
    
    return last_n_logs

def check_xlsx(file_list):

    xlsx_files = [file for file in file_list if file.endswith('.xlsx')]
    is_xlsx = False
    # If there are any .xlsx files, raise a warning
    if xlsx_files:
        is_xlsx=True
        print(f"The following .xlsx files were found:")
        for file_ in xlsx_files:
            print(file_)

        print(f"--> please, save all .xlsx-files as .csv-files to ensure faster data import!")
    return is_xlsx

def plot_summary(trb_id, df_data_overview, dct_ann_owner={}):
    """
    Function to neatly display KPI summary and annotations for a given trb_id.
    
    Parameters:
    trb_id (str or int): Identifier for the data of interest.
    df_data_overview (pd.DataFrame): DataFrame containing data overview information.
    dct_fail_trb (dict): Dictionary containing owner annotations for each trb_id.
    """
    def print_section(title, content, is_tabular=False):
        print('=' * 110)
        print(f"\033[1m {title} \033[0m")
        print('=' * 110)

        if len(content)==0:
            print("No annotations...")
        elif is_tabular:
            print(tabulate(content, headers='keys'))
        else:
            print(content)
        print('\n' *2)

    print_section(f"KPI Summary {trb_id}", pd.DataFrame(df_data_overview), is_tabular=True)
    print_section(f"Owner Annotations {trb_id}", dct_ann_owner, is_tabular=True)
    
    print("\n" * 3)
    
# Function to prepare the power curve
def prepare_power_curve(path_):
    df_powercurve = pd.read_csv(path_, index_col=0)

    df_pc = pd.DataFrame(index=[np.round(i, 2) for i in np.arange(0, 30, 0.01)], columns=['power_norm'])
    df_pc[df_pc.index < df_powercurve.index[0]] = 0
    df_pc[df_pc.index > df_powercurve.index[-1]] = 0
    df_pc.loc[df_powercurve.index] = df_powercurve.values.reshape(-1, 1)
    return df_pc.astype(float).interpolate(method='linear')

# Function to plot the wind rose
def plot_wind_rose(fig, wd, ws):
    ax_windrose = WindroseAxes.from_ax(fig=fig, rect=[0.55, 0.55, 0.4, 0.4])
    ax_windrose.bar(wd, ws, normed=True, opening=0.8)
    ax_windrose.set_title('Wind Rose')
    ax_windrose.set_legend(loc='upper left')

# Function to plot the power curve and actual data

def plot_power_curve(ax, wind_speeds, actual_powers, expected_powers, df_pc):
    distances = actual_powers - expected_powers
    norm = plt.Normalize(distances.min(), distances.max())
    colors = plt.cm.viridis(norm(distances))

    scatter = ax.scatter(wind_speeds, actual_powers, c=colors, alpha=0.25, edgecolor='black', label='Measured')
    ax.plot(df_pc.index, df_pc['power_norm'], c='k', label='Standard PC')  # Plot the power curve
    cbar = plt.colorbar(ScalarMappable(norm=norm, cmap='viridis'), ax=ax)
    cbar.set_label('Distance from Power Curve')

    ax.set_xlabel('Nacelle measured Wind Speed (m/s)')
    ax.set_ylabel('Power Output (kW)')
    ax.set_title('Measured Power Curve')
    ax.grid(True)
    ax.legend()

# Function to plot data availability
def plot_data_availability(ax, time_index, full_time_index, available, data_uptime):
    ax.plot(full_time_index, available, c='grey')
    
    # Detect changes in availability
    change_indices = np.where(np.diff(available.flatten()) != 0)[0]
    
    # Iterate through the change indices to mark gaps in data availability
    for idx in range(len(change_indices)):
        if available[change_indices[idx]] == 1 and available[change_indices[idx] + 1] == 0:
            ax.axvline(full_time_index[change_indices[idx]], color='red', linestyle='--', linewidth=1)
            end_idx = change_indices[idx + 1] if idx + 1 < len(change_indices) else len(full_time_index) - 1
            ax.fill_between(full_time_index[change_indices[idx]:end_idx + 1], 0, 1, 
                            color='lightcoral', alpha=0.5, label='Data Unavailable' if idx == 0 else "")
        elif available[change_indices[idx]] == 0 and available[change_indices[idx] + 1] == 1:
            ax.axvline(full_time_index[change_indices[idx] + 1], color='red', linestyle='--', linewidth=1)

    ax.set_xlim(full_time_index[0], full_time_index[-1])
    ax.set_ylim(0, 1.025)
    #ax.set_aspect(1)
    ax.fill_between(full_time_index, 0, 1, where=available.flatten() == 1, color='forestgreen', alpha=0.2, label='Data Available')
    ax.set_title(f'Data Availability {data_uptime}')
    ax.set_ylabel('Availability')
    ax.legend()


def plot_overview_cockpit(base_path, dct_scada, df_data_overview, trb_id, freq_='10T'):

    df_pc = prepare_power_curve(base_path + 'powercurve.csv')
    df_pc = df_pc/2000*dct_scada[trb_id]['power'].max()
    # Iterate through each turbine
    print('=' * 110)
    print('=' * 110)
    display(HTML(f'<span style="font-size:24px;">Overview-Cockpit Turbine {trb_id}</span>'))

    # Create a new figure
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))

    # Left-align the suptitle
    # plt.suptitle(f'Overview-Cockpit Turbine {trb_id}', fontsize=16, fontweight='bold', x=0.05, ha='left')

    axes[0, 1].remove()  # Remove the top-right subplot
    axes[1, 1].remove()  # Remove the bottom-right subplot
    axes[1, 0].remove()

    # Wind Rose Plot
    wd = dct_scada[trb_id]['wind_direction'].values
    ws = dct_scada[trb_id]['wind_speed'].values
    plot_wind_rose(fig, wd, ws)

    # Power Curve Plot
    df_scada = dct_scada[trb_id]
    wind_speeds = df_scada['wind_speed'].values
    actual_powers = df_scada.power.values
    expected_powers = np.array([df_pc.loc[np.round(speed, 2)].values[0] for speed in wind_speeds])

    plot_power_curve(axes[0, 0], wind_speeds, actual_powers, expected_powers, df_pc)

    # Data Availability Plot
    time_index = dct_scada[trb_id].index
    time_first, time_last = np.min(time_index), np.max(time_index)
    full_time_index = pd.date_range(time_first, time_last, freq=freq_)
    available = np.array([int(time in time_index) for time in full_time_index])

    # Add new subplot for data availability
    ax_data_avail = fig.add_subplot(212)
    plot_data_availability(ax_data_avail, time_index, full_time_index, available,
                           df_data_overview.loc[trb_id, 'Data uptime'])

    # Display the plot
    plt.tight_layout()
    plt.show()
