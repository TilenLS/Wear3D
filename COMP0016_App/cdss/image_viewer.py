import open3d as o3d
import win32gui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.mainWindow = None
        self.widget = None
        self.layout = None
        self.meshLower = None
        self.lowerPresent = False
        self.meshUpper = None
        self.upperPresent = False
        self.vis = None

    def initialise_viewer(self, ui):
        self.mainWindow = ui
        self.widget = ui.widget_3
        self.layout = ui.widget_3_layout
        self.vis = o3d.visualization.Visualizer()
        self.vis.create_window()
        if self.meshLower:
            self.vis.add_geometry(self.meshLower)
            self.lowerPresent = True
        if self.meshUpper:
            self.vis.add_geometry(self.meshUpper)
            self.upperPresent = True
        hwnd = win32gui.FindWindowEx(0, 0, None, "Open3D")
        window = QWindow.fromWinId(hwnd)
        windowcontainer = self.createWindowContainer(window, self.widget)
        self.layout.addWidget(windowcontainer, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        timer = QTimer(self)
        timer.timeout.connect(self.update_vis)
        timer.start(1)

    def update_vis(self):
        # self.vis.update_geometry()
        self.vis.poll_events()
        self.vis.update_renderer()

        if not self.mainWindow.pushButton_3.isChecked() and not self.upperPresent:
            self.vis.add_geometry(self.meshUpper, False)
            self.upperPresent = True
        if self.mainWindow.pushButton_3.isChecked() and self.upperPresent:
            self.vis.remove_geometry(self.meshUpper, False)
            self.upperPresent = False

        if not self.mainWindow.pushButton_4.isChecked() and not self.lowerPresent:
            self.vis.add_geometry(self.meshLower, False)
            self.lowerPresent = True
        if self.mainWindow.pushButton_4.isChecked() and self.lowerPresent:
            self.vis.remove_geometry(self.meshLower, False)
            self.lowerPresent = False

    def load_mesh(self, lowerFilePath=False, upperFilePath=False):
        if lowerFilePath == True:
            lowerFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]
            if self.meshLower:
                self.vis.remove_geometry(self.meshLower, False)
                self.meshLower = o3d.io.read_point_cloud(lowerFilePath)
                self.vis.add_geometry(self.meshLower, False)
            else:
                self.meshLower = o3d.io.read_point_cloud(lowerFilePath)
                self.vis.add_geometry(self.meshLower)
                self.lowerPresent = True
        if upperFilePath == True:
            upperFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]
            if self.meshUpper:
                self.vis.remove_geometry(self.meshUpper, False)
                self.meshUpper = o3d.io.read_point_cloud(upperFilePath)
                self.vis.add_geometry(self.meshUpper, False)
            else:
                self.meshUpper = o3d.io.read_point_cloud(upperFilePath)
                self.vis.add_geometry(self.meshUpper)
                self.upperPresent = True
        else:
            if self.meshLower:
                self.vis.remove_geometry(self.meshLower, False)
                self.meshLower = o3d.io.read_point_cloud(lowerFilePath)
                self.vis.add_geometry(self.meshLower, False)
            if not self.meshLower:
                self.meshLower = o3d.io.read_point_cloud(lowerFilePath)
                self.vis.add_geometry(self.meshLower)
                self.lowerPresent = True
            if self.meshUpper:
                self.vis.remove_geometry(self.meshUpper, False)
                self.meshUpper = o3d.io.read_point_cloud(upperFilePath)
                self.vis.add_geometry(self.meshUpper, False)
            if not self.meshUpper:
                self.meshUpper = o3d.io.read_point_cloud(upperFilePath)
                self.vis.add_geometry(self.meshUpper)
                self.upperPresent = True



    def reset_view(self):
        self.vis.reset_view_point(True)

    def tr(self, text):
        return QObject.tr(self, text)