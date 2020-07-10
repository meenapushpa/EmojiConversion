"""
    Extracting Emojis from the given Csv
============================================
To use the script in its simplest form:
    >> python csvfile_emoji.py

"""

# import key libraries
import csv
import re
import pandas as pd
import codecs

#parsing all emojis in regex pattern and storing in a variable
regrex_pattern = re.compile(pattern = "["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff]"
                           "]+", flags = re.UNICODE)

# separate emoji from texts using csv reader and writer objects
with codecs.open('Csv Conversion Output\\My_Data.csv', 'r', encoding='utf-8') as csvfile, open('Csv Conversion Output\\textfile.csv', 'w', encoding='utf-8') as ofile:
    csvreader = csv.reader(csvfile)
    writer = csv.writer(ofile)
    for i in csvreader:
        valuesstr=' '.join(i)
        texts=regrex_pattern.sub(r' ',str(valuesstr))
        joinstr= texts.split(",")
        writer.writerow(joinstr)

# Getting emoji from texts using findall from regex pattern
def remove_emoji():
    with codecs.open('Csv Conversion Output\\My_Data.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        emojivalues=[]
        for row in csvreader:
            valuesstr=' '.join(row)
            emojis=regrex_pattern.findall(str(valuesstr))
            emojivalues.append(emojis)
        return emojivalues

# Combining both seperate emoji() output and remove_emoji() output into an Excel
def main():
    result1=remove_emoji()
    dfx=pd.DataFrame({'Text':result1})
    dfx.to_csv("Csv Conversion Output\\emojifile.csv",index=False,header=None)
    df1=pd.read_csv('Csv Conversion Output\\textfile.csv',sep="\t",skipinitialspace=False)
    df2=pd.read_csv('Csv Conversion Output\\emojifile.csv')
    alltexts = pd.DataFrame()
    alltexts=pd.concat([df1,df2],axis=1)
    alltexts.to_csv('Csv Conversion Output\\final.csv',index=False, sep="\t",encoding='utf-8')

if __name__ == "__main__":
    main()
