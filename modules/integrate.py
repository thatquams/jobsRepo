from .jobberman import jobberman
from .myjobmag import myjobmag
import pandas as pd 



def dataIntegration(**datasets):
    """
    Concatenates multiple pandas DataFrames passed as keyword arguments.

    Parameters:
    ------------
    datasets : dict
        Keyword arguments where each value is a pandas DataFrame.

    Returns:
    ---------
    pd.DataFrame
        A single concatenated DataFrame.
    """
    return pd.concat(datasets.values(), axis=0, ignore_index=True)


combined_df = dataIntegration(jobberman=jobberman, myjobmag=myjobmag)
