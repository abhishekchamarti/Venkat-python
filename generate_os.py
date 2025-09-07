'''
🔹 Skills Practiced → File handling, OS operations, Functions
🔹 Goal → Build a script that organizes files into folders based on file type.

Steps to Build:
List all files in a directory.

Identify file types (e.g., .jpg, .pdf, .txt).

Create folders for each file type.

Move files into corresponding folders.
'''
import os 
import shutil

print(os.__file__)


'''
def organizefiles(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        '''
'''      
def listallfiles(folder_path):
    if os.path.exists(folder_path):
        for files in os.listdir(folder_path):
            if files.endswith(".sql"):
                fullpath=os.path.join(folder_path,files)
                print(fullpath)
            '''
def createnewfolderifsqlexists(folder_path):
    sql_files=[f for f in os.listdir(folder_path) if f.endswith(".sql")]
    print (sql_files)
    if not sql_files :
        print ('no sql file is found')
        
    msc_folder=os.path.join(folder_path,'miscellaneous')
    os.makedirs(msc_folder, exist_ok=True)
    
    for file in sql_files:
        src_path=os.path.join(folder_path,file)
        dest_path=os.path.join(msc_folder,file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {file} -> miscellaneous/")
    

createnewfolderifsqlexists(r"C:\Users\Venkata.Chamarti\OneDrive - Northern Tool + Equipment\Documents\Nte-Technical")    


            
#createnewfolderifsqlexists(r"C:\Users\Venkata.Chamarti\OneDrive - Northern Tool + Equipment\Documents\Nte-Technical")    
            
             

#listallfiles(r"C:\Users\Venkata.Chamarti\OneDrive - Northern Tool + Equipment\Documents\Nte-Technical")