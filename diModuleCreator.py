def createDiModule(base_path, packageName):
    template = """package """+packageName+""".di
    
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.components.ViewModelComponent

@Module
@InstallIn(ViewModelComponent::class)
object Module {

}
    """
        
    path = base_path + "/Module.kt"
    with open(path, "w") as file:
        file.write(template)
    