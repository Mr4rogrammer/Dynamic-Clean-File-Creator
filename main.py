import os
from useCaseCreator import createUseCaseFile
from repositoryCreator import createRepositoryFile
from exceptionCreator import createExceptionFile
from localDataSourceCreator import createLocalDataSoruceFile
from repositoryImplCreator import repositoryImplCreator
from uiStateCreator import uiStateCreator
from viewmodelCreator import viewModelCreator
from diModuleCreator import createDiModule

#Folder creation

def is_path_exists(path):
    if not os.path.exists(base_path):
        print("The specified path does not exist.")
        return False
    else: 
        return True

def create_directorys(base_path, clean_folder_ist):
    for folder_name in clean_folder_ist:
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

def create_directory_for_clean_layer(base_path):
    clean_folder_ist = ["data", "di", "domain", "presentation"]
    create_directorys(base_path, clean_folder_ist)

def create_directory_for_presentation(base_path):
    presentation_layer_folder= ["states","ui","viewmodel"]
    create_directorys(base_path + "/presentation" , presentation_layer_folder)
  
def create_directory_for_domain(base_path):
    presentation_layer_folder= ["exception","repository","use_cases"]
    create_directorys(base_path + "/domain" , presentation_layer_folder)
  
def create_directory_for_data(base_path):
    presentation_layer_folder= ["data_source","repository"]
    create_directorys(base_path + "/data" , presentation_layer_folder)
  

def create_all_directorys(base_path):
    create_directory_for_clean_layer(base_path)
    create_directory_for_presentation(base_path)
    create_directory_for_domain(base_path)
    create_directory_for_data(base_path)





#Usecase creation

def create_files(base_path, packageName):
    use_case_name = input("Enter the name of the case you want to create (ex: Login,Logout,Reset) :-> ")
  

    #domain File Creation
    createUseCaseFile(base_path+"/domain/use_cases", use_case_name, packageName)
    createRepositoryFile(base_path+"/domain/repository", use_case_name, packageName)
    createExceptionFile(base_path+"/domain/exception", use_case_name, packageName)


    #data File Creation
    createLocalDataSoruceFile(base_path + "/data/data_source" , use_case_name, packageName)
    repositoryImplCreator(base_path + "/data/repository" , use_case_name, packageName)


    #presentation File Creation
    viewModelCreator(base_path + "/presentation/viewmodel" , use_case_name, packageName)
    uiStateCreator(base_path + "/presentation/states" , use_case_name, packageName)


    #Di File Creation
    createDiModule(base_path+"/di", package_name)

    print("Template File Created Succfully...")

base_path = input("Enter the path where you want to create folders (ex : /Users/krish-18770/Pictures/Mr.Shop) :-> ")
package_name = input("Enter project package name (ex : com.gofrugal.sellquick.shopping) :-> ")
if is_path_exists(base_path):
    create_all_directorys(base_path)
    create_files(base_path, package_name)