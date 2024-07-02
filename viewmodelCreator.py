def viewModelCreator(base_path, useCaseNames, packageName):
    use_case_list = useCaseNames.split(',')

    template = """package """+packageName+""".presentation.viewmodel


import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject
import androidx.lifecycle.ViewModel

@HiltViewModel
class ViewModel @Inject constructor(
    
) : ViewModel() {



}
"""
    path = base_path + "/ViewModel.kt"
    with open(path, "w") as file:
        file.write(template)