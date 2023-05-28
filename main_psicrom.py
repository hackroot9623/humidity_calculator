import sys
import os
import math
#from decimal import *
from PyQt5.QtWidgets import QDialog, QApplication
from psicrom import *

class Psicrometer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_psicrom()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dothemath)
        self.show()

    def dothemath(self):
        if len(self.ui.temp_seca.text())!=0:
            ts=float(self.ui.temp_seca.text())
        else:
            ts=0
        if len(self.ui.pto_rocio.text())!=0:
            pr=float(self.ui.pto_rocio.text())
        else:
            pr=0

        d1=112.0-0.1*ts + pr
        d2=112.0+0.9*ts
        calc=math.pow(d1/d2, 8)
        hr= 100.0*calc
        self.ui.hum.setText("Humedad: " +str(round(hr)) +"%")

###########Second part of the calculator#################

        self.ui.pushButton_2.clicked.connect(self.calc_sen)
        self.show()

    def calc_sen(self):
        if len(self.ui.temp_normal.text())!=0:
            taire=float(self.ui.temp_normal.text())
        else:
            taire=0
        if len(self.ui.wind_speed.text())!=0:
            wspeed=float(self.ui.wind_speed.text())
        else:
            wspeed=0

        term=math.sqrt(wspeed - 0.0454*wspeed)
        senterm= 33 + (taire-33)*(0.474 + 0.454*term)
        self.ui.sterm.setText("S.Term: " +str(round(senterm)) +"ºC")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Psicrometer()
    w.show()
    sys.exit(app.exec_())