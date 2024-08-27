# -*- coding: utf8 -*-

#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2020 kbwbe                                              *
#*                                                                         *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

# Too many errors, commenting out for now
# 22:35:17  During initialization the error "'NoneType' object has no attribute 'setObjectName'" occurred in freecad.cool_wb
# 22:35:17  --------------------------------------------------------------------------------
# 22:35:17  Traceback (most recent call last):
# File "<string>", line 235, in InitApplications
# File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
# return _bootstrap._gcd_import(name[level:], package, level)
# File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
# File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
# File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
# File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
# File "<frozen importlib._bootstrap_external>", line 883, in exec_module
# File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
# File "/media/toddg/data1/repos/forked/freecad-source/build/Mod/CoolWB/freecad/cool_wb/init_gui.py", line 4, in <module>
# from freecad.cool_wb.TranslateUtils import translate
# File "/usr/lib/python3/dist-packages/shiboken2/files.dir/shibokensupport/__feature__.py", line 142, in _import
# return original_import(name, *args, **kwargs)
# File "/media/toddg/data1/repos/forked/freecad-source/build/Mod/CoolWB/freecad/cool_wb/translate_utils.py", line 31, in <module>
# from DraftGui import translate
# File "/usr/lib/python3/dist-packages/shiboken2/files.dir/shibokensupport/__feature__.py", line 142, in _import
# return original_import(name, *args, **kwargs)
# File "/media/toddg/data1/repos/forked/freecad-source/build/Mod/Draft/DraftGui.py", line 1805, in <module>
# FreeCADGui.draftToolBar = DraftToolBar()
# File "/media/toddg/data1/repos/forked/freecad-source/build/Mod/Draft/DraftGui.py", line 209, in __init__
# self.tray.setObjectName("Draft tray")
# AttributeError: 'NoneType' object has no attribute 'setObjectName'
# 22:35:17  --------------------------------------------------------------------------------
#
# import FreeCAD
#
#
# if FreeCAD.GuiUp:
#     from PySide.QtCore import QT_TRANSLATE_NOOP
#     from DraftGui import translate
# else:
#     def QT_TRANSLATE_NOOP(context, text):
#         return text
#
#     def translate(context, text):
#         return text

def QT_TRANSLATE_NOOP(context, text):
    return text

def translate(context, text):
    return text

