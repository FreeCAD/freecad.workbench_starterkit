import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.{{cookiecutter.workbench_module_name}}.translate_utils import translate
from freecad. {{cookiecutter.workbench_module_name}} import my_numpy_function

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources/translations")

class {{cookiecutter.workbench_class_name}}(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("{{cookiecutter.workbench_module_name}}", "{{cookiecutter.workbench_menu_text}}")
    ToolTip = translate("{{cookiecutter.workbench_module_name}}", "a simple {{cookiecutter.workbench_menu_text}}")
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

        App.Console.PrintMessage(translate(
            "{{cookiecutter.workbench_module_name}}",
            "Switching to {{cookiecutter.workbench_module_name}}") + "\n")
        App.Console.PrintMessage(translate(
            "{{cookiecutter.workbench_module_name}}",
            "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
        self.appendMenu(translate("Menu", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "{{cookiecutter.workbench_module_name}}",
            "Workbench {{cookiecutter.workbench_module_name}} activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "{{cookiecutter.workbench_module_name}}",
            "Workbench {{cookiecutter.workbench_module_name}} de-activated.") + "\n")


Gui.addWorkbench({{cookiecutter.workbench_class_name}}())
