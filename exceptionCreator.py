def createExceptionFile(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')

    for useCaseName in use_case_list:
        

        use_case_class_template ="""package """+packageName+""".domain.exception

sealed class """+useCaseName+"""Failure : Failure.FeatureFailure() {
   
}
    """
        
        path = base_path + "/" + useCaseName +"Failure.kt"
        with open(path, "w") as file:
            file.write(use_case_class_template)
    
