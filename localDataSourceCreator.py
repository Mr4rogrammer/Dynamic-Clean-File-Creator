import os

def createLocalDataSoruceFile(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')

    for useCaseName in use_case_list:
        folder_path = os.path.join(base_path, useCaseName.lower())

        remote_folder = base_path+"/"+useCaseName.lower()+"/remote"
        local_folder = base_path+"/"+useCaseName.lower()+"/local"

        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(remote_folder, exist_ok=True)
        os.makedirs(local_folder, exist_ok=True)
        


        #Datasoruce interface file creation

        dataSoruce = """package """+packageName+""".data.data_source."""+useCaseName.lower()+"""

interface """+useCaseName+"""DataSource {
   
}
"""
        path = base_path + "/" + useCaseName +"/"+useCaseName+"DataSoruce.kt"
        with open(path, "w") as file:
            file.write(dataSoruce)



        #Local datasoruce interface file creation

        
        localDataSoruce = """package """+packageName+""".data.data_source."""+useCaseName.lower()+""".local

import javax.inject.Inject
import """+packageName+""".data.data_source."""+useCaseName.lower()+"""."""+useCaseName+"""DataSource

class """+useCaseName+"""LocalDataSourceImpl @Inject constructor() : """+useCaseName+"""DataSource {

}

"""

        path = local_folder +"/"+ useCaseName+"LocalDataSourceImpl.kt"
        with open(path, "w") as file:
            file.write(localDataSoruce)


        #Remote datasoruce interface file creation

        
        localDataSoruce = """package """+packageName+""".data.data_source."""+useCaseName.lower()+""".remote

import javax.inject.Inject
import """+packageName+""".data.data_source."""+useCaseName.lower()+"""."""+useCaseName+"""DataSource

class """+useCaseName+"""RemoteDataSourceImpl @Inject constructor() : """+useCaseName+"""DataSource {

}

"""

        path = remote_folder +"/"+ useCaseName+"RemoteDataSourceImpl.kt"
        with open(path, "w") as file:
            file.write(localDataSoruce)