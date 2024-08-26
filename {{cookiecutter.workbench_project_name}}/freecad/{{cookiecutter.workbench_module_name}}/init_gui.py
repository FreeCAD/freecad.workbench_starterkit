import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.{{cookiecutter.workbench_module_name}}.TranslateUtils import translate
from freecad.{{cookiecutter.workbench_module_name}} import ICONPATH, TRANSLATIONSPATH


class {{cookiecutter.workbench_class_name}}(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("{{cookiecutter.workbench_translation_context}}", "{{cookiecutter.workbench_menu_text}}")
    ToolTip = translate("{{cookiecutter.workbench_translation_context}}", "a simple {{cookiecutter.workbench_menu_text}}")
    Icon = os.path.join(ICONPATH, "{{cookiecutter.workbench_icon}}")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        # Add translations path
        Gui.addLanguagePath(TRANSLATIONSPATH)
        Gui.updateLocale()

        from freecad.{{cookiecutter.workbench_module_name}} import my_numpy_function
        App.Console.PrintMessage(translate("Console",
            "Switching to {{cookiecutter.workbench_module_name}}") + "\n")
        App.Console.PrintMessage(translate("Console", "Run a numpy function:") \
            + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
        self.appendMenu(translate("Menu", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench({{cookiecutter.workbench_class_name}}())
