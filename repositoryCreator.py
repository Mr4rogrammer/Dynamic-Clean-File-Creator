def createRepositoryFile(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')
    for useCaseName in use_case_list:
        

        use_case_class_template ="""package """+packageName+""".domain.repository

interface """+useCaseName+"""Repository {
    
}
    """
        
        path = base_path + "/" + useCaseName +"Repository.kt"
        with open(path, "w") as file:
            file.write(use_case_class_template)