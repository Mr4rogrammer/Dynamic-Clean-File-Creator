def repositoryImplCreator(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')
    for useCaseName in use_case_list:
        use_case_name_case = useCaseName[0].lower() + useCaseName[1:]
        repository_temp ="""package """+packageName+""".data.repository

import """+packageName+""".domain.repository."""+useCaseName+"""Repository
import """+packageName+""".data.data_source."""+useCaseName.lower()+"""."""+useCaseName+"""DataSource

import javax.inject.Inject

class """+useCaseName+"""RepositoryImpl @Inject constructor(
    private val """+use_case_name_case+"""DataSource: """+useCaseName+"""DataSource,
    ) : """+useCaseName+"""Repository  {
   
}
    """
        
        path = base_path + "/" + useCaseName +"RepositoryImpl.kt"
        with open(path, "w") as file:
            file.write(repository_temp)