# Google-Drive-Transfer-Validation
This repository briefly describes the process of transferring all Google Drive content from an academic GSuite account to a private account. Python is used for validation and for correcting copy errors.

Academic or organizational GSuite accounts are used by a large number of universities, and students or teachers may end up accumulating large volumes of data in Drive that can be painful to transfer through manual downloading and re-uploading. Even if this process was to be automated, uploads can be very slow.

Google Drive provides an alternate approach which can be a lot faster, called Takeout Transfer. Details on the process are available at the following links: \
https://takeout.google.com/transfer \
https://www.youtube.com/watch?v=CyoMqPTS6YQ&ab_channel=TechnologyDepartmentVideos \
https://www.youtube.com/watch?v=6lN26m4i_xw&ab_channel=LanceYoder \
https://www.youtube.com/watch?v=B-eGHN6vo2M 

While this procedure is generally very effective, it can run into problems when transferring very large volumes of data. In particular, there may be file types that are not properly uploaded, or damaged files that are not uploaded (see Error Code 100078, as an example). While Google Drive recommends restarting the process, this might not help.

This repository contains Python files that can help to diagnose the extent of the issue in case of a failed transfer, and provide some workarounds. The code may be equally helpful when large folders are copied between two separate drives, or from a backup disc. When used for Google Drive, it is meant to be applied to Google Drive File Stream (https://support.google.com/a/answer/7491144?hl=en), which creates a local folder structure for files in the cloud.

<br></br>
**Extracting File Paths and Mapping**

The module recover_file_paths.py contains two functions. The first, recover_paths, traverses all paths within a chosen directory, and stores paths to individual files and their corresponding sizes. This can be done to identify all unique files within a large directory, and get a sense of the size of different folders or files. The code saves these paths as Pandas dataframes stored as Pickle (.pkl) files.

The second function, compare_paths, uses as its inputs the output from the previous function. It can be used to perform a diff on two different directories, and highlights files that exist in one directory but not in the other. This is helpful to diagnose which files failed to copy over. Once the code is run, a set of failed files that need to be transfered can be saved down to manually transfer over.

<br></br>
**Recovering Failed Transfers**

The module copy_files.py contains a function, copy_dir, which copies all files from an input path list (such as a list of failed transfers from the function above), and recreates the same directory structure in the target directory. So, files that fail to transfer through the cloud can be recorded, and copied over to the File Stream folder. The code retains the flexibility to recreate a new directory structure in a separate folder, or can be run to find the correct directory to copy a failed file into. This is equally applicable when copying between local folders or drives. 



