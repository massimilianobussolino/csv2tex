
# Script to convert csv files to Latex tables
# Version 1.0
# Author: Massimiliano Bussolino massimiliano.bussolino@mail.polimi.it


#packages import
import sys
import csv

#function section

#Get columns vector form command line input
def _getcols_(string_vec):
    string_vec = list(string_vec)
    string_vec.remove('[')
    string_vec.remove(']')
    string_vec = ''.join(string_vec)
    col_vec = string_vec.split(',')
    for i in range(0,len(col_vec)):
        col_vec[i] = int(col_vec[i])
    return col_vec

#Firts part of the Latex code for the table
def __tablesetup__(tab,sett,sett_string,col_len):
    if tab == 'tabular':
        string01 = '''
\\begin{table}
\\centering
\\begin{tabular}{'''
    elif tab == 'longtable':
        string01 = '''
% For this option the longtable package is required
\\begin{longtable}{'''
    if sett == 'custom':
        string02 = sett_string + '}\n\n\\hline\n'
    else:
        string02 = '|c'*col_len + '|}\n\n\\hline\n'
    return string01+string02

# Function for the last part of the latex code for the table
def __tableclosing__(caption,lab,tab):
    if tab == 'tabular':
        string01 = '''
\\end{tabular}
\\caption{'''+caption+'}'+'''
\\label{'''+lab+'}'+'''
\\end{table}'''
    elif tab == 'longtable':
        string01 = '''
\\caption{'''+caption+'}'+'''
\\end{longtable}'''+'''
\\label{'''+lab+'}'
    return string01

#get special input vector
def __special_inputs__(input):
    temp = input.split('/')
    for i in range(0,len(temp)):
        temp[i] = temp[i].split('-')
    return temp

# Add the LaTex keyword for bold italic...
def __specialformatting__(cell,col_count,special):
    for el in special:
        if col_count == int(el[0]):
            if el[1] == 'verb':
                cell = '\\'+el[1]+'|'+cell+'|'
            elif el[1] == 'math':
                cell = '$'+cell+'$'
            else:
                cell = '\\'+el[1]+'{'+cell+'}'
    return cell

# default settings
tab = 'tabular'         #table vs longtable
cols = 'all'            #columns to be inclueded
head = True             #Inclued header of the table
caption = ''            #Write caption of the table
sett = 'default'        #Columns type in the table, if default, all 'c'
sett_string = ''        #In case of lack of definition
lab = 'tab:mytab'       #Label of the table
sep = ','               #Separator for csv files
quote = '"'             #Quotation mark for csv files
newline = '\\hline'     #Horizontal line style
output = ''             #Print output in cmd vs file



#check inputs
len_argv = len(sys.argv)
filename_flag = False
for i in range(1,len_argv,2):
    # table vs longtable selection
    if sys.argv[i] == '-tab':
        if sys.argv[i+1] == 'table':
            tab = 'table'
        elif sys.argv[i+1] == 'longtable':
            tab = 'longtable'
        else:
            print('Wrong input after keyword \'-tab\'')
            sys.exit()
    # columns to be inserted
    elif sys.argv[i] == '-cols':
        cols = _getcols_(sys.argv[i+1])
    # header
    elif sys.argv[i] == '-header':
        if sys.argv[i+1] == 'False':
            head = False
    # caption
    elif sys.argv[i] == '-caption':
        caption = sys.argv[i+1]
    # settings of the columens
    elif sys.argv[i] == '-setting':
        sett_string = sys.argv[i+1]
        sett = 'custom'
    # lable of the table
    elif sys.argv[i] == '-label':
        lab = sys.argv[i+1]
    # Separator mark for csv
    elif sys.argv[i] == '-separator':
        sep = sys.argv[i+1]
    # Quotes mark for csv
    elif sys.argv[i] == '-quotes':
        quote = sys.argv[i+1]
    # file name of the csv file
    elif sys.argv[i] == '-file':
        filename = sys.argv[i+1]
        filename_flag = True
    # Output file directory
    elif sys.argv[i] == '-output':
        output = sys.argv[i+1]
    elif sys.argv[i] == '-newline':
        newline = newline*int(sys.argv[i+1])
    # Special formatting for columns (textbf/textit/verb/math)
    elif sys.argv[i] == '-special':
        special = __special_inputs__(sys.argv[i+1])
    else:
        print(sys.argv[i]+' not recognised as input.')
if not filename_flag:
    print('File name or directory shall be included as input')


# File opening and reading of the csv file
txt = ''
special = ''
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = sep,quotechar = quote)
    count_row = -1
    for row in csv_reader: #Row iteration
        count_row += 1
        if count_row != 0 or head: #Check for the header condition
            count_cell = 0
            if cols == 'all': #Check for the columns order
                col_len = len(row)
                for cell in row:
                    if count_cell == 0: #Check for first item
                        txt = txt + __specialformatting__(row[count_cell],count_cell,special)
                        count_cell += 1
                    elif count_cell == len(row)-1: #Check for last item
                        txt = txt+' & '+__specialformatting__(row[count_cell],count_cell,special)+' \\\\ '+newline+'\n'
                    else:
                        txt = txt + ' & ' + __specialformatting__(row[count_cell],count_cell,special)
                        count_cell += 1
            else:
                col_len = len(cols)
                for num in cols:
                    if count_cell == 0: #check on first item
                        txt = txt + __specialformatting__(row[num-1],count_cell,special)
                        count_cell += 1
                    elif count_cell == len(cols)-1: #check on last item
                        txt = txt+' & '+__specialformatting__(row[num-1],count_cell,special)+' \\\\ '+newline+'\n'
                    else:
                        txt = txt + ' & ' + __specialformatting__(row[num-1],count_cell,special)
                        count_cell += 1

front = __tablesetup__(tab,sett,sett_string,col_len) #front matter
bottom = __tableclosing__(caption,lab,tab) #bottom matter

txt = front + txt + bottom

if output != '': #Output file
    file_id = open(output,'w')
    file_id.write(txt)
    file_id.close()
else:
    print(txt) #Print
