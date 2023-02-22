import os
import sys
from sign_in_page import *
from register_page import *
from ui_interface import *
from Custom_Widgets.Widgets import *
from ui_interface import *
from Custom_Widgets.Widgets import *
from image_viewer import ImageViewer

os.environ['QT_MAC_WANTS_LAYER'] = '1'

settings = QSettings()

from model import AppFunctions


class MainWindow(QMainWindow, Ui_SignInPage):
    def __init__(self):
        Ui_SignInPage.__init__(self)
        Ui_RegisterPage.__init__(self)
        Ui_HomePage.__init__(self)
        QMainWindow.__init__(self)
        self.ui1 = Ui_SignInPage()
        self.ui2 = Ui_RegisterPage()
        self.ui3 = Ui_HomePage()
        self.lowerFilePath = None
        self.upperFilePath = None
        self.imageViewer = ImageViewer()
        self.startSignInPage()

    def startSignInPage(self):
        self.ui1.setupUi(self)
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ToothWear.db'))
        AppFunctions.main(dbFolder)
        self.ui1.sign_in_button.clicked.connect(lambda: AppFunctions.checkSignInDetails(self, dbFolder))
        self.ui1.register_button.clicked.connect(self.startRegisterPage)

    def startRegisterPage(self):
        self.ui2.setupUi(self)
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ToothWear.db'))
        AppFunctions.main(dbFolder)
        self.ui2.register_button.clicked.connect(lambda: AppFunctions.addDentist(self, dbFolder))
        self.ui2.sign_in_button.clicked.connect(self.startSignInPage)

    def startHomePage(self):
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ToothWear.db'))
        num_of_patient = AppFunctions.getPatientNumber(dbFolder)
        self.ui3.setupUi(self, num_of_patient)
        loadJsonStyle(self, self.ui3)
        self.show()
        self.imageViewer.initialise_viewer(self.ui3)
        AppFunctions.main(dbFolder)
        self.ui3.addPatientButton.clicked.connect(lambda: AppFunctions.addPatient(self, dbFolder))
        self.ui3.upperJawScanButton.clicked.connect(lambda: AppFunctions.choose_file(self, False, True))
        self.ui3.lowerJawScanButton.clicked.connect(lambda: AppFunctions.choose_file(self, True, False))
        self.ui3.loadUpperMesh.clicked.connect(lambda: self.imageViewer.load_mesh(False, True))
        self.ui3.loadLowerMesh.clicked.connect(lambda: self.imageViewer.load_mesh(True, False))
        self.ui3.resetViewPoint.clicked.connect(lambda: self.imageViewer.reset_view())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
