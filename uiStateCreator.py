def uiStateCreator(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')

    for useCaseName in use_case_list:
        template = """package """+packageName+""".presentation.states

data class """+useCaseName+"""UiState  (


)
    """
        path = base_path + "/" + useCaseName +"UiState.kt"
        with open(path, "w") as file:
            file.write(template)