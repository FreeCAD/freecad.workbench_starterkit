import os
import FreeCADGui as gui  # use "from freecad import gui" once its available
from freecad.template_extension import ICONPATH


class template_workbench(gui.Workbench):
    """frame workbench"""

    MenuText = "template workbench"
    ToolTip = "template workbench"                                      # TODO
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """here is the place to import all the commands"""
        from freecad.template_extension import my_numpy_function
        print("switching to template_extension")
        print("run a function: ", my_numpy_function.my_foo(100))

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

    def Activated(self):
        pass

    def Deactivated(self):
        pass


gui.addWorkbench(template_workbench())
