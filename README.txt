
            █▀▀ █▀ █░█   ▀█▀ █▀█   █░░ ▄▀█ ▀█▀ █▀▀ ▀▄▀
            █▄▄ ▄█ ▀▄▀   ░█░ █▄█   █▄▄ █▀█ ░█░ ██▄ █░█


# Introduction

This script has the the aim to automate the generation of LaTex tables form csv
files, giving the possibility to customize the table an its style according to
the user needs.
The script has to be called from command line. It has been written on Windows for
Windows, therefore the correct execution of the script on other OS in not ensured.
Python version: 3.7.7

# Syntax

The minimum command required for the correct execution includes only the name
of the csv file targetted or its directory, as reported in the example:

>> py csv2tex.py -file [filename.csv]

The output would then be the whole file csv reported in the form of a LaTex
table in the command prompt, ready to be copied and pasted in any editor.

The list of other possible inputs for the personalization of the table are the
following:

1. tabular vs longtable
Syntax:
>> py csv2tex.py -file [filename.csv] -tab table
>> py csv2tex.py -file [filename.csv] -tab longtable
In the first case, the table is created in the table environment, if the "longtable"
option is used, than the table will be able to span across multiple pages.
For the "longtable" case, the "longtable" package is required.
If this input is not specified, the default option is set as "table".

2. Which and in which order columns must be organised
Syntax: >> py csv2tex.py -file [filename.csv] -cols [3,1,2]
This command is used to change the order of the tables of the file and to
include in the table only some of them. The number in the brackets is the number
of the columns in the csv file ordered from left to right. The columns number
must be included in brackets and be separated by commas, without spaces between
them.

3. Header of the table
Syntax:
>> py csv2tex.py -file [filename.csv] -header False
This command remove the first line from the tables. Usually the first line includes
the name of the variables stored in each column. The command can be used only as
showed above. If the command is not expressed, then the header will appear

4. Caption
Syntax:
>> py csv2tex.py -file [filename.csv] -caption 'My caption'
This command includes the caption of the table as specified by the user.

5. Label
Syntax:
>> py csv2tex.py -file [filename.csv] -label 'tab:mylabel'
This command includes the label of the table as specified by the user.

6. Separator
Syntax:
>> py csv2tex.py -file [filename.csv] -separator ,
This command is used to specify which separator is used inside the csv file.
The default option is the comma.

7. Quotes mark
Syntax:
>> py csv2tex.py -file [filename.csv] -quotes "
This command is used to specify which character identifies the beginning of a text
string inside the csv file. The default option is "

8. Output
Syntax:
>> py csv2tex.py -file [filename.csv] -output [target_file.txt]
This command specifies the file where the table shall be written. If the command
is not specified, the table will be printed in the cmd. If the command is
specified and the file already exists, the file will be overwritten, if the file
was not existing, it will be created.

9. Newline
Syntax:
>> py csv2tex.py -file [filename.csv] -newline 2
This command specifies how many solid lines are there between the rows of the
table.

10. Special formatting
Syntax:
>> py csv2tex.py -file [filename.csv] -special 3-textit/2-math/4-verb
This command is used to set certain columns to bold, italic or to be inserted
in the math or verb environment of LaTex. Those option can be called with the
keywords:
- "textbf" for bold
- "textit" for italic
- "verb" for code-like text
- "math" for the math enviroment
The syntax follows this rule: for every column with a special formatting, the
number of the column has to be followed by '-' and then the keyword. If more then
one rule must be applied, they have to be separated by '/'


Those additional command can be inserted in any order and none of the is necessary
for the correct execution of the script


# Authors and contacts

Massimiliano Bussolino
massimiliano.bussolino@mail.polimi.it
