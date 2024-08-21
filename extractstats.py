import pandas as pd


def extract_cols(filename):

    df = pd.read_excel(filename)
    
    sel_cols = df[['Book Name','Author Name','1st priority ','2nd priority','Type','Primary category']]

    return sel_cols


print(extract_cols('C:/Users/chven/OneDrive/Desktop/easystat/Podcast Categories.xlsx'))


def extract_list_by_category(filename):
    pass



    





