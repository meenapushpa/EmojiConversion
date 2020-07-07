"""
    Extracting Emojis from the given Excel
============================================
To use the script in its simplest form:
    >> python extract_emoji.py

"""
# import key libraries
import re
import xlrd
import xlsxwriter
import pandas as pd

# parsing all emojis in regex pattern and storing in a variable

regrex_pattern = re.compile(pattern = "["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff]"
                           "]+", flags = re.UNICODE)

def separate_emoji():
    workbook = xlrd.open_workbook("Test\\MyData.xlsx")
    sheet = workbook.sheet_by_index(0)
    listvalues=[]
    for rowx in range(sheet.nrows):
        values = sheet.cell_value(rowx,0)
        list1=regrex_pattern.findall(str(values))
        listvalues.append(list1)
    return listvalues

def remove_emoji():
    workbook = xlrd.open_workbook("Test\\MyData.xlsx")
    sheet = workbook.sheet_by_index(0)
    textvalues=[]
    for rowx in range(sheet.nrows):
        values = sheet.cell_value(rowx,0)
        list1=regrex_pattern.sub(' ',str(values))
        textvalues.append(list1)
    return textvalues

# Combining both seperate emoji() output and remove_emoji() output into an Excel
def main():
    result1=separate_emoji()
    result2=remove_emoji()
    df2=pd.DataFrame({'Text':result2 ,'emoji':result1})
    df2=df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
    df2.to_excel("emoji_spreadsheet.xlsx",sheet_name='sheet1',index=False,header=None)

if __name__ == "__main__":
    main()
