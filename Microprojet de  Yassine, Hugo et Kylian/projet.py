import sys
import csv
from PyQt5 import QtWidgets
from ui_proj import Ui_MainWindow
from ui_aide import Ui_HelpDialog
import rc_proj 


class MaFenetre(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.datafile = "exhibits.csv"
        self.data = None
        self.connecteSignaux()
        self.achercher = ""
        self.montreData()
        return
        
    def montreAide(self, fichier):
        """
        crée une fenêtre de dialogue, avec le contenu du fichier affiché
        :param: fichier un fichier au format HTML
        """
        class monDialogue(QtWidgets.QDialog, Ui_HelpDialog):
            def __init__(self, fichier):
                QtWidgets.QDialog.__init__(self)
                self.setupUi(self)
                with open(fichier) as htmldata:
                    texte = htmldata.read()
                    self.textEdit.setText(texte)
                return
        dialogue = monDialogue(fichier)
        dialogue.exec_()

    def connecteSignaux(self):
        self.actionQuitter.triggered.connect(self.close)
        self.actionAide_F1.triggered.connect(self.montreAideF1)
        self.action_propos.triggered.connect(self.montreAidePropos)
        self.selectionEdit.editingFinished.connect(self.montreData)
        self.selectButton.clicked.connect(self.montreData)
        self.pushButton.clicked.connect(self.montrePushButton)
        self.pushButton_2.clicked.connect(self.montrePushButton_2)
        return
    
    def montreAideF1(self):
        self.montreAide("aide.html")
        return
        
    def montreAidePropos(self):
        self.montreAide("apropos.html")
        return
        
    def montrePushButton(self):
        self.montreAide("aide.html")
        return
        
    def montrePushButton_2(self):
        self.montreAide("apropos.html")
        return
        
    def appliqueSelection(self):
            self.achercher=self.selectionEdit.text()
            print("le texte était", self.achercher)
            self.montreData()
            return
            
    def montreData(self):
            if not self.data:
                   self.data = []
                   with open(self.datafile) as csvfile:
                            lecteur = csv.reader(csvfile)
                            for ligne in lecteur:
                                   self.data.append(ligne)
            html = "<table style='background:lightblue;'>"
            html += "<tr style='background:linear-gradient(to top, blue, cyan, magenta )'><th>" + "</th><th>".join(self.data[0])+"</th></tr>"
            ok = False
            for ligne in self.data[1:]:
                   print(self.achercher,"".join(ligne))
                   ok = self.achercher in "".join(ligne), self.achercher
                   if ok:
                                 html += "<tr style='background: lightgreen;'><td>" + "</td><td>".join(ligne)+"</td></tr>"
            html += "</table>"
            self.textEdit.setText(html)
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    f = MaFenetre()
    f.show()
    sys.exit( app.exec_() )
