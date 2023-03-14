#Imports
import sys
import pandas as pd

#Cli argument
file_name = 'Heritage_Asset.csv' #sys.argv[1]

file = pd.read_csv(file_name, keep_default_na=False) #disables default NA values and sents them to NaN, probably not needed

#TODO:: Maybe make the funciton take in the file as well as col name ot avoid hardcoding them
#TODO:: Make the forloop into a function to avoid repteaded code

#Strings containing files
image = 'Image' #in finds
condition_image = 'Condition Image' #in heritage asses
document = 'Document' #in information resource

# if image in file.columns:
#     for path in file[image].iteritems():    # Loop over all cells within the image column
#         if path[1]:
#             file_list = list(eval(path[1])) #Cast path[1] string to a list of dictionaries
#             path_string = ""
#             for fp in file_list:
#                 path_string += fp['url'] + ',' #Create a comma separated string for all file paths
#             path_string = path_string[:-1]  #Remove the trailing comma
#             file.at[path[0], image] = path_string #Replace current cell content with path string

#     file.to_csv(f'{file_name}')


if condition_image in file.columns:
    for path in file[condition_image].iteritems():
        if path[1]:
            if len(eval(path[1])) > 0:
                file_list = list(eval(path[1])) #Cast path[1] string to a list of dictionaries
                path_string = ""
                for fp in file_list:
                    path_string += fp['url'] + ',' #Create a comma separated string for all file paths
                path_string = path_string[:-1]  #Remove the trailing comma
                file.at[path[0], condition_image] = path_string #Replace current cell content with path string
    file.to_csv(f'{file_name}')

# if document in file.columns:
#     for path in file[document].iteritems():
#         if path[1]:
#             file_list = list(eval(path[1])) #Cast path[1] string to a list of dictionaries
#             path_string = ""
#             for fp in file_list:
#                 path_string += fp['url'] + ',' #Create a comma separated string for all file paths
#             path_string = path_string[:-1]  #Remove the trailing comma
#             file.at[path[0], document] = path_string #Replace current cell content with path string
#     file.to_csv(f'{file_name}')
