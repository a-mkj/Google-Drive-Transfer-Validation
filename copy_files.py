
#Importing modules
import os
import pickle
import pandas as pd
import shutil



def copy_file( original, target ):
    #Basic function that copies a file from the original source folder to the target

    #Inputs:
    #original - The directory of the source file to be copied (str)
    #target - The directory of the copied file (str)

    #Example of Usage:
    #copy_file( 'Users/Test_User/Desktop/test.txt', 'Users/Test_User/Downloads/test.txt' ) copies the file test.txt from the Desktop to Downloads

    shutil.copyfile( original, target )



def copy_dir( raw_file, target_dir, skip_pos ):
    #Copies all files from the raw_file path list, and recreates directory structure in target_dir

    #Inputs:
    #raw_file - A .pkl file containing a dataframe with a column listing the paths of all files to be copied (assumed to be within the same master directory) (str)
    #target_dir - The target directory within which the directory structure from raw_file is replicated (str)
    #skip_pos - Integer representing the number of string positions after which the directory should be replicated (int)

    #Example of Usage:
    #copy_dir( 'test_input.pkl', '~/Desktop', 25 ) 
    #An example of a path in test_input.pkl could be 'Users/Test_User/Downloads/Folder/test.txt'
    #Since we skip 25 string positions, the directory structure is replicated starting at '/Folder'
    #A folder called Folder will be created within '~/Desktop' and test.txt copied within it
    #This is done for all paths in the raw_file dataframe

    temp = pd.read_pickle( raw_file )
    paths = list( temp.path )
    errors = 0
    counter = 0
    for i in paths:
        counter = counter + 1
        #Progress message
        print( 'Processed: ' + str( counter ) + '    ' + 'Progress: ' +  str( round( 100*(counter)/len(paths), 2 ) ) + '%' + '    Errors: ' + str( errors ) , end="\r", flush = True )  
        try:
            original = i #Original path
            target = target_dir + original[ skip_pos: ] #New path 
            my_folder = target.rsplit('/',1)[0] #Target directory
            if not os.path.exists( my_folder ): #Checking same directory not re-created
                os.makedirs( my_folder )
            shutil.copyfile( original, target ) #Copying files to target directory
        except:
            errors = errors + 1







