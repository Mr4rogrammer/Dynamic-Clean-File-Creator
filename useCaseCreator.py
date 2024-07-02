def createUseCaseFile(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')
    for useCaseName in use_case_list:
        use_case_name_case = useCaseName[0].lower() + useCaseName[1:]

        use_case_class_template ="""package """+packageName+""".domain.use_cases

import """+packageName+""".domain.repository."""+useCaseName+"""Repository
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import javax.inject.Inject

class """+useCaseName+""" @Inject constructor(
    private val """+use_case_name_case+"""Repository: """+useCaseName+"""Repository,
    private val dispatcher: CoroutineDispatcher = Dispatchers.IO
) {
    suspend operator fun invoke() {
            
    }
}
    """
        
        path = base_path + "/" + useCaseName +".kt"
        with open(path, "w") as file:
            file.write(use_case_class_template)
    
