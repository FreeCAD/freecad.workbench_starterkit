import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad. {{cookiecutter.workbench_module_name}} import my_numpy_function

translate=App.Qt.translate
QT_TRANSLATE_NOOP=App.Qt.QT_TRANSLATE_NOOP

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources", "translations")

# Add translations path
Gui.addLanguagePath(TRANSLATIONSPATH)
Gui.updateLocale()

class {{cookiecutter.workbench_class_name}}(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("Workbench", "{{cookiecutter.workbench_menu_text}}")
    ToolTip = translate("Workbench", "a simple {{cookiecutter.workbench_menu_text}}")
    Icon = os.path.join(ICONPATH, "{{cookiecutter.workbench_icon}}")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """

        App.Console.PrintMessage(translate(
            "Log",
            "Switching to {{cookiecutter.workbench_module_name}}") + "\n")
        App.Console.PrintMessage(translate(
            "Log",
            "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        # NOTE: Context for this commands must be "Workbench"
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)
        self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench {{cookiecutter.workbench_module_name}} activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench {{cookiecutter.workbench_module_name}} de-activated.") + "\n")


Gui.addWorkbench({{cookiecutter.workbench_class_name}}())
