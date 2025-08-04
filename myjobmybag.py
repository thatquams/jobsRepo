from extension import connectToJobSite
import pandas as pd 
pd.set_option('display.max_columns', 10)


@connectToJobSite
def myJobMyBag(content):
    pass