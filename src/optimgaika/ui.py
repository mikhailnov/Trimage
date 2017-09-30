from PyQt4.QtCore import *
from PyQt4.QtGui import *
from os import path

class OptimgaikaTableView(QTableView):
    """Init the table drop event."""
    def __init__(self, parent=None):
        super(OptimgaikaTableView, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()
        filelist = []
        for url in event.mimeData().urls():
            filelist.append(unicode(url.toLocalFile()))

        self.emit(SIGNAL("fileDropEvent"), (filelist))


class Ui_optimgaika(object):
    def get_image(self, image):
        """ Get the correct link to the images used in the UI """
        imagelink = path.join(path.dirname(path.dirname(path.realpath(__file__))), "optimgaika/" + image)
        return imagelink

    def setupUi(self, optimgaika):
        """ Setup the entire UI """
        optimgaika.setObjectName("optimgaika")
        optimgaika.resize(600, 170)

        optimgaikaIcon = QIcon(self.get_image("pixmaps/optimgaika-icon.png"))
        optimgaika.setWindowIcon(optimgaikaIcon)

        self.centralwidget = QWidget(optimgaika)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.widget = QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")

        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QFrame(self.widget)
        self.frame.setObjectName("frame")

        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.addfiles = QPushButton(self.frame)
        font = QFont()
        font.setPointSize(9)
        self.addfiles.setFont(font)
        self.addfiles.setCursor(Qt.PointingHandCursor)
        icon = QIcon()
        icon.addPixmap(QPixmap(self.get_image("pixmaps/list-add.png")), QIcon.Normal, QIcon.Off)
        self.addfiles.setIcon(icon)
        self.addfiles.setObjectName("addfiles")
        self.addfiles.setAcceptDrops(True)
        self.horizontalLayout.addWidget(self.addfiles)

        self.label = QLabel(self.frame)
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setMargin(1)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        spacerItem = QSpacerItem(498, 20, QSizePolicy.Expanding,
                                 QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.recompress = QPushButton(self.frame)
        font = QFont()
        font.setPointSize(9)
        self.recompress.setFont(font)
        self.recompress.setCursor(Qt.PointingHandCursor)

        icon1 = QIcon()
        icon1.addPixmap(QPixmap(self.get_image("pixmaps/view-refresh.png")), QIcon.Normal, QIcon.Off)

        self.recompress.setIcon(icon1)
        self.recompress.setCheckable(False)
        self.recompress.setObjectName("recompress")
        self.horizontalLayout.addWidget(self.recompress)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.processedfiles = OptimgaikaTableView(self.frame)
        self.processedfiles.setEnabled(True)
        self.processedfiles.setFrameShape(QFrame.NoFrame)
        self.processedfiles.setFrameShadow(QFrame.Plain)
        self.processedfiles.setLineWidth(0)
        self.processedfiles.setMidLineWidth(0)
        self.processedfiles.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.processedfiles.setTabKeyNavigation(True)
        self.processedfiles.setAlternatingRowColors(True)
        self.processedfiles.setTextElideMode(Qt.ElideRight)
        self.processedfiles.setShowGrid(True)
        self.processedfiles.setGridStyle(Qt.NoPen)
        self.processedfiles.setSortingEnabled(False)
        self.processedfiles.setObjectName("processedfiles")
        self.processedfiles.resizeColumnsToContents()
        self.processedfiles.setSelectionMode(QAbstractItemView.NoSelection)
        self.verticalLayout_2.addWidget(self.processedfiles)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        optimgaika.setCentralWidget(self.centralwidget)

        self.retranslateUi(optimgaika)
        QMetaObject.connectSlotsByName(optimgaika)

    def retranslateUi(self, optimgaika):
        """ Fill in the texts for all UI elements """
        optimgaika.setWindowTitle(QApplication.translate("optimgaika",
            "Optimgaika image compressor", None, QApplication.UnicodeUTF8))
        self.addfiles.setToolTip(QApplication.translate("optimgaika",
            "Add file to the compression list", None,
            QApplication.UnicodeUTF8))
        self.addfiles.setText(QApplication.translate("optimgaika",
            "&Add and compress", None, QApplication.UnicodeUTF8))
        self.addfiles.setShortcut(QApplication.translate("optimgaika",
            "Alt+A", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("optimgaika",
            "Drag and drop images onto the table", None,
            QApplication.UnicodeUTF8))
        self.recompress.setToolTip(QApplication.translate("optimgaika",
            "Recompress all images", None, QApplication.UnicodeUTF8))
        self.recompress.setText(QApplication.translate("optimgaika",
            "&Recompress", None, QApplication.UnicodeUTF8))
        self.recompress.setShortcut(QApplication.translate("optimgaika",
            "Alt+R", None, QApplication.UnicodeUTF8))
        self.processedfiles.setToolTip(QApplication.translate("optimgaika",
            "Drag files in here", None, QApplication.UnicodeUTF8))
        self.processedfiles.setWhatsThis(QApplication.translate("optimgaika",
            "Drag files in here", None, QApplication.UnicodeUTF8))
