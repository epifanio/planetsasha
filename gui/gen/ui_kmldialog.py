# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/kmldialog.ui'
#
# Created: Sat Sep 21 13:46:42 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_KmlDialog(object):
    def setupUi(self, KmlDialog):
        KmlDialog.setObjectName(_fromUtf8("KmlDialog"))
        KmlDialog.resize(505, 489)
        self.scrollArea = QtGui.QScrollArea(KmlDialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 465, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 463, 429))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.KmlGeneralgroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.KmlGeneralgroupBox.setTitle(_fromUtf8(""))
        self.KmlGeneralgroupBox.setObjectName(_fromUtf8("KmlGeneralgroupBox"))
        self.gridLayout_27 = QtGui.QGridLayout(self.KmlGeneralgroupBox)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.LineWidth = QtGui.QSpinBox(self.KmlGeneralgroupBox)
        self.LineWidth.setProperty("value", 1)
        self.LineWidth.setObjectName(_fromUtf8("LineWidth"))
        self.gridLayout_27.addWidget(self.LineWidth, 1, 1, 1, 1)
        self.Extrudelabel = QtGui.QLabel(self.KmlGeneralgroupBox)
        self.Extrudelabel.setObjectName(_fromUtf8("Extrudelabel"))
        self.gridLayout_27.addWidget(self.Extrudelabel, 3, 0, 1, 1)
        self.Tessellate = QtGui.QCheckBox(self.KmlGeneralgroupBox)
        self.Tessellate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Tessellate.setText(_fromUtf8(""))
        self.Tessellate.setObjectName(_fromUtf8("Tessellate"))
        self.gridLayout_27.addWidget(self.Tessellate, 2, 1, 1, 1)
        self.LineWidthlabel = QtGui.QLabel(self.KmlGeneralgroupBox)
        self.LineWidthlabel.setObjectName(_fromUtf8("LineWidthlabel"))
        self.gridLayout_27.addWidget(self.LineWidthlabel, 1, 0, 1, 1)
        self.Extrude = QtGui.QCheckBox(self.KmlGeneralgroupBox)
        self.Extrude.setText(_fromUtf8(""))
        self.Extrude.setChecked(True)
        self.Extrude.setObjectName(_fromUtf8("Extrude"))
        self.gridLayout_27.addWidget(self.Extrude, 3, 1, 1, 1)
        self.Tessellatelabel = QtGui.QLabel(self.KmlGeneralgroupBox)
        self.Tessellatelabel.setObjectName(_fromUtf8("Tessellatelabel"))
        self.gridLayout_27.addWidget(self.Tessellatelabel, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.KmlGeneralgroupBox)
        self.KmlElevationgroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.KmlElevationgroupBox.setObjectName(_fromUtf8("KmlElevationgroupBox"))
        self.gridLayout_28 = QtGui.QGridLayout(self.KmlElevationgroupBox)
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.Heightlabel = QtGui.QLabel(self.KmlElevationgroupBox)
        self.Heightlabel.setObjectName(_fromUtf8("Heightlabel"))
        self.horizontalLayout_10.addWidget(self.Heightlabel)
        self.ExtrudeType = QtGui.QComboBox(self.KmlElevationgroupBox)
        self.ExtrudeType.setEditable(False)
        self.ExtrudeType.setObjectName(_fromUtf8("ExtrudeType"))
        self.ExtrudeType.addItem(_fromUtf8(""))
        self.ExtrudeType.setItemText(0, _fromUtf8(""))
        self.ExtrudeType.addItem(_fromUtf8(""))
        self.ExtrudeType.addItem(_fromUtf8(""))
        self.ExtrudeType.addItem(_fromUtf8(""))
        self.ExtrudeType.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.ExtrudeType)
        self.gridLayout_28.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.AltitudeModelabel = QtGui.QLabel(self.KmlElevationgroupBox)
        self.AltitudeModelabel.setObjectName(_fromUtf8("AltitudeModelabel"))
        self.horizontalLayout_11.addWidget(self.AltitudeModelabel)
        self.AltitudeMode = QtGui.QComboBox(self.KmlElevationgroupBox)
        self.AltitudeMode.setObjectName(_fromUtf8("AltitudeMode"))
        self.AltitudeMode.addItem(_fromUtf8(""))
        self.AltitudeMode.setItemText(0, _fromUtf8(""))
        self.AltitudeMode.addItem(_fromUtf8(""))
        self.AltitudeMode.addItem(_fromUtf8(""))
        self.AltitudeMode.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.AltitudeMode)
        self.gridLayout_28.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.Offsetlabel = QtGui.QLabel(self.KmlElevationgroupBox)
        self.Offsetlabel.setObjectName(_fromUtf8("Offsetlabel"))
        self.horizontalLayout_8.addWidget(self.Offsetlabel)
        self.Offset = QtGui.QDoubleSpinBox(self.KmlElevationgroupBox)
        self.Offset.setMaximum(20000000.0)
        self.Offset.setProperty("value", 1000.0)
        self.Offset.setObjectName(_fromUtf8("Offset"))
        self.horizontalLayout_8.addWidget(self.Offset)
        self.gridLayout_28.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.KmlElevationgroupBox)
        self.KmlColorgroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.KmlColorgroupBox.setObjectName(_fromUtf8("KmlColorgroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.KmlColorgroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelcolor = QtGui.QToolButton(self.KmlColorgroupBox)
        self.labelcolor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.labelcolor.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.labelcolor.setObjectName(_fromUtf8("labelcolor"))
        self.gridLayout_3.addWidget(self.labelcolor, 0, 0, 1, 1)
        self.linecolor = QtGui.QToolButton(self.KmlColorgroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linecolor.sizePolicy().hasHeightForWidth())
        self.linecolor.setSizePolicy(sizePolicy)
        self.linecolor.setAcceptDrops(False)
        self.linecolor.setAutoFillBackground(False)
        self.linecolor.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.linecolor.setAutoRaise(False)
        self.linecolor.setObjectName(_fromUtf8("linecolor"))
        self.gridLayout_3.addWidget(self.linecolor, 1, 0, 1, 1)
        self.polygoncolor = QtGui.QToolButton(self.KmlColorgroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polygoncolor.sizePolicy().hasHeightForWidth())
        self.polygoncolor.setSizePolicy(sizePolicy)
        self.polygoncolor.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.polygoncolor.setObjectName(_fromUtf8("polygoncolor"))
        self.gridLayout_3.addWidget(self.polygoncolor, 2, 0, 1, 1)
        self.LabelColorhorizontalLayout = QtGui.QHBoxLayout()
        self.LabelColorhorizontalLayout.setObjectName(_fromUtf8("LabelColorhorizontalLayout"))
        self.labelcolorlabel = QtGui.QLineEdit(self.KmlColorgroupBox)
        self.labelcolorlabel.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.labelcolorlabel.setReadOnly(True)
        self.labelcolorlabel.setObjectName(_fromUtf8("labelcolorlabel"))
        self.LabelColorhorizontalLayout.addWidget(self.labelcolorlabel)
        self.LabelAlpha = QtGui.QSpinBox(self.KmlColorgroupBox)
        self.LabelAlpha.setStyleSheet(_fromUtf8("background-color: rgb(231, 231, 231);"))
        self.LabelAlpha.setMaximum(255)
        self.LabelAlpha.setProperty("value", 255)
        self.LabelAlpha.setObjectName(_fromUtf8("LabelAlpha"))
        self.LabelColorhorizontalLayout.addWidget(self.LabelAlpha)
        self.gridLayout_3.addLayout(self.LabelColorhorizontalLayout, 0, 1, 1, 1)
        self.LineColorhorizontalLayout = QtGui.QHBoxLayout()
        self.LineColorhorizontalLayout.setObjectName(_fromUtf8("LineColorhorizontalLayout"))
        self.linecolorlabel = QtGui.QLineEdit(self.KmlColorgroupBox)
        self.linecolorlabel.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.linecolorlabel.setReadOnly(True)
        self.linecolorlabel.setObjectName(_fromUtf8("linecolorlabel"))
        self.LineColorhorizontalLayout.addWidget(self.linecolorlabel)
        self.LineAlpha = QtGui.QSpinBox(self.KmlColorgroupBox)
        self.LineAlpha.setStyleSheet(_fromUtf8("background-color: rgb(231, 231, 231);"))
        self.LineAlpha.setMaximum(255)
        self.LineAlpha.setProperty("value", 255)
        self.LineAlpha.setObjectName(_fromUtf8("LineAlpha"))
        self.LineColorhorizontalLayout.addWidget(self.LineAlpha)
        self.gridLayout_3.addLayout(self.LineColorhorizontalLayout, 1, 1, 1, 1)
        self.PolyColorhorizontalLayout = QtGui.QHBoxLayout()
        self.PolyColorhorizontalLayout.setObjectName(_fromUtf8("PolyColorhorizontalLayout"))
        self.polygoncolorlabel = QtGui.QLineEdit(self.KmlColorgroupBox)
        self.polygoncolorlabel.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.polygoncolorlabel.setReadOnly(True)
        self.polygoncolorlabel.setObjectName(_fromUtf8("polygoncolorlabel"))
        self.PolyColorhorizontalLayout.addWidget(self.polygoncolorlabel)
        self.PolygonAlpha = QtGui.QSpinBox(self.KmlColorgroupBox)
        self.PolygonAlpha.setStyleSheet(_fromUtf8("background-color: rgb(231, 231, 231);"))
        self.PolygonAlpha.setMaximum(255)
        self.PolygonAlpha.setProperty("value", 255)
        self.PolygonAlpha.setObjectName(_fromUtf8("PolygonAlpha"))
        self.PolyColorhorizontalLayout.addWidget(self.PolygonAlpha)
        self.gridLayout_3.addLayout(self.PolyColorhorizontalLayout, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addWidget(self.KmlColorgroupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.buttonBox = QtGui.QDialogButtonBox(KmlDialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 450, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(KmlDialog)
        self.ExtrudeType.setCurrentIndex(3)
        self.AltitudeMode.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(KmlDialog)

    def retranslateUi(self, KmlDialog):
        KmlDialog.setWindowTitle(_translate("KmlDialog", "KML Settings", None))
        self.Extrudelabel.setText(_translate("KmlDialog", "Extrude", None))
        self.LineWidthlabel.setText(_translate("KmlDialog", "Line Width", None))
        self.Tessellatelabel.setText(_translate("KmlDialog", "Tessellate", None))
        self.KmlElevationgroupBox.setTitle(_translate("KmlDialog", "Elevation", None))
        self.Heightlabel.setText(_translate("KmlDialog", "Extrude Type", None))
        self.ExtrudeType.setItemText(1, _translate("KmlDialog", "2D", None))
        self.ExtrudeType.setItemText(2, _translate("KmlDialog", "3D", None))
        self.ExtrudeType.setItemText(3, _translate("KmlDialog", "Offset", None))
        self.ExtrudeType.setItemText(4, _translate("KmlDialog", "Attribute", None))
        self.AltitudeModelabel.setText(_translate("KmlDialog", "Altitude  Mode", None))
        self.AltitudeMode.setItemText(1, _translate("KmlDialog", "clampToGround", None))
        self.AltitudeMode.setItemText(2, _translate("KmlDialog", "relativeToGround", None))
        self.AltitudeMode.setItemText(3, _translate("KmlDialog", "absolute", None))
        self.Offsetlabel.setText(_translate("KmlDialog", "OffSet", None))
        self.KmlColorgroupBox.setTitle(_translate("KmlDialog", "Color", None))
        self.labelcolor.setText(_translate("KmlDialog", "Label", None))
        self.linecolor.setText(_translate("KmlDialog", "Line", None))
        self.polygoncolor.setText(_translate("KmlDialog", "Polygon", None))

