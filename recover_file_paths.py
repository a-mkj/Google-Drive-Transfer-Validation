
#Importing modules
import os
import pickle
import pandas as pd



def recover_paths( root, save_path, save_name ):
	#Extracts the paths and size of all files in a root directory and saves the results

	#Inputs:
	#root - The directory within which file paths are to be mapped out (str)
	#save_path - The directory within which results are to be saved (str)
	#save_name - Prefix for the saved results (str)

	#Outputs:
	#save_path + '/' + save_name  +'.pkl' - A .pkl file containing a dataframe with all unique file paths and file size in bytes
	#save_path + '/paths_' + save_name  +'.pkl' - A .pkl file containing a dataframe with all unique file paths
	#save_path + '/err_' + save_name  +'.pkl' - A .pkl file containing a dataframe with file paths which could not be visited/size computed

	#Example of Usage:
	#recover_paths( 'Users/Test_User/Desktop', 'Users/Test_User/Downloads', 'test_results'  )
	#This will recover all file paths and sizes in the directory called 'Users/Test_User/Desktop'
	#Result will be three files, test_results.pkl, paths_test_results.pkl and err_test_results.pkl which are saved in 'Users/Test_User/Downloads'

	#Initializing lists
    paths_list = list()
    file_path_list = list()
    file_size_list = list()
    err_lists = list()

    #Traversing all paths
    for path, subdirs, files in os.walk(root):
        for name in files:
            try: #Attempting to compute file size and save path/size
                temp  = os.path.join(path, name)
                paths_list.append( temp )
                file_size_list.append( os.stat( temp ).st_size  )
                file_path_list.append( temp )
            except: #Tracking fails
                err_lists.append( os.path.join(path, name) )


    #Saving results as dataframes stores as .pkl
    df = pd.DataFrame( { 'path':file_path_list, 'size':file_size_list } )
    df.to_pickle( save_path + '/' + save_name  +'.pkl' )

    names = pd.DataFrame( { 'path':paths_list } )
    df.to_pickle( save_path + '/paths_' + save_name  +'.pkl' )

    err = pd.DataFrame( { 'path':err_lists } )
    err.to_pickle( save_path + '/err_' + save_name  +'.pkl' )




def compare_paths( root_a, root_b ):
	#Conducts a diff to extract file paths in one of the input root paths but not in the other
	#This is useful when identifying files missing due to errors when copying directories
	#Input files are similar to the output files from the function above

	#Inputs:
	#root_a - The .pkl dataframe containing list of files from the first directory
	#root_b - The .pkl dataframe containing list of files from the second directory

	#Outputs:
	#in_a_not_in_b - A .pkl dataframe containing a list of files in directory root_a but not in root_b
	#in_b_not_in_a - A .pkl dataframe containing a list of files in directory root_b but not in root_a

	#Example of Usage:
	#compare_paths( 'Users/Test_User/Desktop/test1.pkl', 'Users/Test_User/Desktop/test2.pkl' )
	#Here, the files test1.pkl and test2.pkl contain all file paths of two different directories
	#The output will be two files, in_test1_not_in_test2.pkl and in_test2_not_in_test1.pkl

	#Reading in files
	root_a = pd.read_pickle( 'root_a' )
	root_a = list( root_a.path )
	root_b = pd.read_pickle( 'root_b' )
	root_b = list( root_b.path )

	#Processing differences
	in_a_not_in_b = pd.DataFrame( { 'missing_paths' : [ i in root_a if i not in root_b ] } )
	in_b_not_in_a = pd.DataFrame( { 'missing_paths' : [ i in root_b if i not in root_a ] } )

	#Saving results
	in_a_not_in_b.to_pickle( 'in_' + root_a.rsplit('/',1)[1] + 'not_in_' + root_b.rsplit('/',1)[1] )
	in_b_not_in_a.to_pickle( 'in_' + root_b.rsplit('/',1)[1] + 'not_in_' + root_a.rsplit('/',1)[1] )












