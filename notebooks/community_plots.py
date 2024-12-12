import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def custom_plot_community_annotations(annot_id:int, df_scada:pd.DataFrame, dataset: str):
    """
    Generate custom plots for specific community annotations.

    Args:
        annot_id (int): Annotation ID to plot.
        df_scada (pd.DataFrame): SCADA data as a DataFrame.
        dataset (str): Dataset name (e.g., 'edp') for context-specific plots.

    Returns:
        None: Displays the plot directly.
    """

    ####################################################################################
    # exemplary custom plot for community annotation 2 of the edp dataset
    # will appear in the respective notebook next to the comunity annotation

    if (dataset=='edp'):
        
        # exemplary custom plot for community annotation 2 of the edp dataset
        # will appear in the respective notebook next to the comunity annotation
        
        if annot_id==2:
            plt.figure(figsize=(3,4))
            plt.scatter(df_scada['Grd_Prod_Pwr_Avg'].loc['2016-12'],
                        df_scada['Prod_LatestAvg_ReactPwrGen0'].loc['2016-12'],
                        label='Data Dec. 2016')

            plt.scatter(df_scada['Grd_Prod_Pwr_Avg'].loc['2017-12'],
                        df_scada['Prod_LatestAvg_ReactPwrGen0'].loc['2017-12'],
                        alpha=0.5, label='Data Dec. 2017')

            plt.xlim(-50,200)
            plt.legend()

            plt.title('Custom plot example')
            plt.tight_layout()
    ####################################################################################

def plot_community_annotations(df_community, df_scada, df_logs=False):
    """
    Plot community annotations on SCADA signal data with optional log message highlights.

    Args:
    - df_community: DataFrame containing community annotations with columns:
        - 'remarks': Description of the annotation.
        - 'signal': Signal name or pattern to match (full or partial to selectu all with '{signal}*".
        - 'related_log_message': Log message linked to the annotation (optional).
        - 'time_start': Start time of the annotated interval (optional).
        - 'time_stop': End time of the annotated interval (optional).
    - df_scada: DataFrame containing SCADA signal data with time-indexed columns.
    - df_logs: (Optional) DataFrame containing log messages with columns:
        - 'message': Log message text.

    Returns:
        None: Displays the plot and data directly.
    """
    print('=' * 110)
    print(f"\033[1m Community Annotations: \033[0m")
    print('=' * 110)

    for id_, entry in df_community.iterrows():
        print('=' * 110)
        print(f'Community Annotation {id_}: {entry.remarks}')

        # Identify related signals
        lst_signals = [signal for signal in df_scada.columns if df_community.loc[id_].signal in signal]

        # Create subplots for each related signal
        fig, ax = plt.subplots(nrows=len(lst_signals), sharex=True)
        if len(lst_signals) == 1:
            ax = [ax]

        for i, ax_ in enumerate(ax):
            # Highlight related log messages if available
            if (len(entry.related_log_message) > 2) & isinstance(df_logs, pd.DataFrame):
                for date, log_ in df_logs[df_logs.message == df_community.loc[id_].related_log_message].iterrows():
                    ax_.axvline(date, c='darkred', ls='--', alpha=0.5)

            # Plot the signal data
            ax_.plot(df_scada[lst_signals[i]], marker='x', alpha=0.75)
            ax_.set_title(lst_signals[i])

            # Highlight annotated time intervals if available
            if ((len(entry.time_start) > 2) & (len(entry.time_stop) > 2)):
                ax_.axvspan(entry.time_start, entry.time_stop, color='darkred', alpha=0.25)

            ax_.legend([f'LOG:{df_community.loc[id_].related_log_message}'])

        fig.autofmt_xdate()

        # Custom plotting hook for additional functionality
        dataset = df_community.dataset
        custom_plot_community_annotations(id_, df_scada, dataset)

        plt.show()
# def plot_community_annotations(dataset, df_community, df_scada, df_logs=False):
#
#     for id_, entry in df_community.iterrows():
#
#         print('#' * 110)
#         print(f'Community Annotation {id_}: {entry.remarks}')
#
#         lst_signals = [signal for signal in df_scada.columns if df_community.loc[id_].signal in signal]
#
#         fig, ax = plt.subplots(nrows=len(lst_signals), sharex=True)
#
#         if len(lst_signals)==1:
#             ax = [ax]
#
#         for i, ax_ in enumerate(ax):
#
#             # if related log exists - plot
#             if (len(entry.related_log_message)>2) & isinstance(df_logs, pd.DataFrame):
#                 for date, log_ in df_logs[df_logs.message==df_community.loc[id_].related_log_message].iterrows():
#                     ax_.axvline(date, c='darkred', ls='--', alpha=0.5)
#
#
#             ax_.plot(df_scada[lst_signals[i]], marker='x', alpha=0.75)
#
#             ax_.set_title(lst_signals[i])
#
#             # if start/endtime available - plot
#             if (len(entry.time_start)>2) & len(entry.time_stop)>2:
#                 ax_.axvspan(entry.time_start, entry.time_stop, color='darkred', alpha=0.25)
#
#             ax_.legend([f'LOG:{df_community.loc[id_].related_log_message}'])
#
#         fig.autofmt_xdate()
#
#         custom_plot_community_annotations(dataset, id_, df_scada)
#
#         plt.show()
