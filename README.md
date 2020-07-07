## Emoji Separation

This script is written in python3.x and will separate the emojis from the given text and keep it in next column.

### Prequisites

1.  Convert the CSV into Excel by decoding with `65001: Unicode (UTF-8)` using delimiter option.

  How to ?
    * Open excel file
    * Import csv using following options

          > Data
            > From Access
              > Choose your CSV file
                > Ensure File Origin is set to 65001: Unicode (UTF-8)
                  > Next > Next > Finish
        * Your file is now ready for parsing


2. Save your source file under the Test directory

3. Execute this script using Python3.x

Thats all you need ! the output file will be stored in the same directory.
