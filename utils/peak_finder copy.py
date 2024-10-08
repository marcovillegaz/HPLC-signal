"""Utility function for peaks processing"""

import pandas as pd
from scipy.signal import find_peaks


def peak_finder(data, time):
    """This function finds peaks in your chromatogram. First all the peaks in
    the chropmatogram are identified using find_peaks() function from scipy. The
    the peaks area filtered to intervals sleected by the user.

    Input:
        chroma_data: DataFrame with chromatogram data.
        intervals: list with intevervals where the peak of interest are.
            ex. [[0,500],[1500,2000]]
            * The intervals can't be overlapped

    Output:
        peaks_data: Datafram with the index and intesity of peaks in intervals"""

    print(type(data))
    # Peak identification with scipy function
    # The configuration can be change here.
    peaks, prop = find_peaks(
        x=data,
        height=20000,  # [min,max]
        threshold=20000,  # Threshold is basically the noise level
        distance=300,  # Horizontal distance >=1
        prominence=300,
        width=None,
        wlen=None,
        rel_height=0.1,
        plateau_size=None,
    )

    # Dataframe with information of all peaks in the chromatogram
    residence_time = time[peaks]
    peaks_data = pd.DataFrame(
        {
            "index": peaks,
            "residence_time": residence_time,
            "height": prop["peak_heights"],
        }
    )
    peaks_data.reset_index(drop=True, inplace=True)
    return peaks_data
