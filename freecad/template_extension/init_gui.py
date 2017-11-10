import os
import FreeCADGui as gui
from freecad.template_extension import ICONPATH


class template_workbench(gui.Workbench):
    """
    class which gets initiated at starup of the gui
    """

    MenuText = "template workbench"
    ToolTip = "a simple template workbench"
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.template_extension import my_numpy_function
        print("switching to template_extension")
        print("run a function: ", my_numpy_function.my_foo(100))

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

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


gui.addWorkbench(template_workbench())
