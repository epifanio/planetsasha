#!/usr/bin/env python

import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_ossimwindow import Ui_OssimWindow


class OssimWindow(QWidget, Ui_OssimWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

	    
