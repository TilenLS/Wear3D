import os
import sys
from sign_in_page import *
from register_page import *
from ui_interface import *
from Custom_Widgets.Widgets import *
from ui_interface import *
from Custom_Widgets.Widgets import *
from image_viewer import ImageViewer
from model import AppFunctions

os.environ['QT_MAC_WANTS_LAYER'] = '1'

settings = QSettings()

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
        self.sextantFilePath = None
        self.imageViewer = ImageViewer()
        self.startSignInPage()

    def startSignInPage(self):
        self.ui1.setupUi(self)
        self.ui1.sign_in_button.clicked.connect(lambda: AppFunctions.checkSignInDetails(self))
        self.ui1.register_button.clicked.connect(self.startRegisterPage)

    def startRegisterPage(self):
        self.ui2.setupUi(self)
        self.ui2.register_button.clicked.connect(lambda: AppFunctions.addDentist(self))
        self.ui2.sign_in_button.clicked.connect(self.startSignInPage)

    def startHomePage(self):
        num_of_patient = AppFunctions.getPatientNumber()
        self.ui3.setupUi(self, num_of_patient, self.imageViewer)
        loadJsonStyle(self, self.ui3)
        self.show()
        self.imageViewer.initialise_viewer(self.ui3)

        self.ui3.addPatientButton.clicked.connect(lambda: AppFunctions.addPatient(self, self.imageViewer))
        self.ui3.upperJawScanButton.clicked.connect(lambda: AppFunctions.choose_file(self, False, True))
        self.ui3.lowerJawScanButton.clicked.connect(lambda: AppFunctions.choose_file(self, True, False))
        self.ui3.sextantScanButton.clicked.connect(lambda: AppFunctions.chooseSextantFile(self))
        self.ui3.loadUpperMesh.clicked.connect(lambda: self.imageViewer.load_mesh(False, True))
        self.ui3.loadLowerMesh.clicked.connect(lambda: self.imageViewer.load_mesh(True, False))
        self.ui3.resetViewPoint.clicked.connect(lambda: self.imageViewer.reset_view())
        self.ui3.run_analysis_button.clicked.connect(lambda: AppFunctions.show_prediction(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
