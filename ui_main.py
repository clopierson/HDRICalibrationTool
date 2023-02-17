# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainrvpJdh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import os

# For file name extraction
import ntpath

# For regular expressions
import re

# Creates a region to upload a file to, given input coords, region size, and a region color.
class UploadFileRegion( QWidget ):
    # regionCoords[0]: x
    # regionCoords[1]: y
    # regionSize[0]: width
    # regionSize[1]: height
    def __init__( self, regionName="DefaultLabel", regionCoords=[0,0], regionSize=[128, 128] ):
        QWidget.__init__(self)

        # Store input parameters as class attributes
        self.regionName = regionName
        self.regionXPosition = regionCoords[0]
        self.regionYPosition = regionCoords[1]
        self.regionWidth = regionSize[0]
        self.regionHeight = regionSize[1]

        # Visible region background
        self.uploadRegion = QLabel( self )

        # Spacers for QVBox/QHBox layouts
        self.regionSpacer = QLabel( self )

        # Region label
        regionNameWithSpaces = re.sub(r"(\w)([A-Z])", r"\1 \2", regionName)
        self.regionLabel = QLabel( regionNameWithSpaces, self )
        
        # File icon pixmap
        self.fileIcon = QLabel( self )
        self.pixmap = QPixmap( './assets/blank-file-128.ico' )

        # File path label
        self.filePathLabel = QLabel( self )

        # File name label
        self.fileNameLabel = QLabel( self )

        # Create remove button for an uploaded file
        self.removeBtn = QPushButton( "Remove", self )


        # Allow dropping files in this region
        self.setAcceptDrops( True )

        # Init. flag that stores if region has an uploaded file.
        self.hasFile = False

        # Adjust elements of object
        self.create()


    def create( self ):
        # Stylesheet path
        stylesheetPath = "./styles/upload_file_region_styles.css"

        # -------------------------------------------------------------------------------------
        # Upload Region

        # Set object name
        self.uploadRegion.setObjectName( "UploadFileRegion_{}".format( self.regionName ) )

        # Set style
        self.uploadRegion.setProperty( "hasFile", self.hasFile )

        with open(stylesheetPath, "r") as stylesheet:
            self.uploadRegion.setStyleSheet( stylesheet.read() )

        # Set size
        self.uploadRegion.setGeometry( QRect( self.regionXPosition, self.regionYPosition, self.regionWidth, self.regionHeight ) )

        # -------------------------------------------------------------------------------------
        # Region Spacer Region

        # Set object name
        self.regionSpacer.setObjectName( "regionSpacer" )

        # Set style
        self.regionSpacer.setProperty( "hasFile", self.hasFile )

        with open(stylesheetPath, "r") as stylesheet:
            self.regionSpacer.setStyleSheet( stylesheet.read() )

        # -------------------------------------------------------------------------------------
        # Region Label

        # Set object name
        self.regionLabel.setObjectName( "UploadFileRegionLabel" )

        # Set style
        self.regionLabel.setProperty( "hasFile", self.hasFile )

        with open(stylesheetPath, "r") as stylesheet:
            self.regionLabel.setStyleSheet( stylesheet.read() )

        # Adjusting font
        regionFont = QFont()
        regionFont.setPointSize( 28 )
        self.regionLabel.setFont( regionFont )

        # -------------------------------------------------------------------------------------
        # File Icon

        # Set object name
        self.fileIcon.setObjectName( "FileIcon" )

        # Set style
        self.fileIcon.setProperty( "hasFile", self.hasFile )

        with open(stylesheetPath, "r") as stylesheet:
            self.fileIcon.setStyleSheet( stylesheet.read() )

        # Visibility
        self.fileIcon.hide()

        # Resize and set pixmap : https://stackoverflow.com/questions/21802868/python-how-to-resize-raster-image-with-pyqt
        self.pixmap = self.pixmap.scaledToHeight( self.regionHeight - self.regionLabel.height() - 32 )
        self.fileIcon.setPixmap( self.pixmap )

        # -------------------------------------------------------------------------------------
        # File Path Label (Hidden)

        # Set object name
        self.filePathLabel.setObjectName( "UploadedFilePathLabel" )

        # Set text
        self.filePathLabel.setText( "" )

        # Visibility
        self.filePathLabel.hide()

        # -------------------------------------------------------------------------------------
        # File Name Label

        # Set object name
        self.fileNameLabel.setObjectName( "UploadFileNameLabel" )

        # Set style
        self.fileNameLabel.setProperty( "hasFile", self.hasFile )

        with open(stylesheetPath, "r") as stylesheet:
            self.fileNameLabel.setStyleSheet( stylesheet.read() )

        # Visibility
        self.fileNameLabel.hide()

        # Adjusting font
        labelFont = QFont()
        labelFont.setPointSize( 16 )
        self.fileNameLabel.setFont( labelFont )

        # -------------------------------------------------------------------------------------
        # Remove Button

        # Set object name
        self.removeBtn.setObjectName( "UploadFileRemoveButton" )

        # Set style
        with open(stylesheetPath, "r") as stylesheet:
            self.removeBtn.setStyleSheet( stylesheet.read() )

        # Connect event to signal
        self.removeBtn.clicked.connect( self.removeBtnClicked )

        # Visibility
        self.removeBtn.hide()

        # -------------------------------------------------------------------------------------


        # Layout creation
        self.baseVLayout = QVBoxLayout()

        self.upperHLayout = QHBoxLayout()
        self.lowerHLayout = QHBoxLayout()

        self.innerVLayout = QVBoxLayout()

        self.lowerHLayout.addWidget( self.fileIcon, stretch=1 )
        self.lowerHLayout.addLayout( self.innerVLayout, stretch=6 )

        self.baseVLayout.addLayout( self.upperHLayout, stretch=1 )
        self.baseVLayout.addLayout( self.lowerHLayout, stretch=4 )

        self.innerVLayout.addWidget( self.regionSpacer, stretch=3 )
        self.innerVLayout.addWidget( self.fileNameLabel, stretch=1 )

        self.upperHLayout.addWidget( self.regionLabel, stretch=6 )
        self.upperHLayout.addWidget( self.regionSpacer, stretch=1 )
        self.upperHLayout.addWidget( self.removeBtn, stretch=1 )

        self.uploadRegion.setLayout( self.baseVLayout )


        return
        

    # Allow the dragging of image/text files onto region.
    def dragEnterEvent( self, event ):
        # Only accept dragEnterEvents if region does not have a file already
        if (self.hasFile == False):
            if event.mimeData().hasText():
                event.acceptProposedAction()


    # On image/text file drop event
    def dropEvent(self, event):
        # Set hasFile flag
        self.hasFile = True

        # Get file path from file
        filepath = event.mimeData().text()

        # Remove 'file:///' if it exists after uploadinf file
        if ( filepath.startswith( "file:///" ) ):
            filepath = filepath[8:]

        # Set filePathLabel
        self.filePathLabel.setText( filepath )

        # Set fileNameLabel and show
        filename = self.getFilenameFromPath( filepath )
        self.fileNameLabel.setText( filename )
        self.fileNameLabel.show()

        # Show file icon
        self.fileIcon.show()

        # Show removeBtn
        self.removeBtn.show()


        # Adjust styling
        # Stylesheet path
        stylesheetPath = "./styles/upload_file_region_styles.css"

        # Set property for stylsheet to apply correct style
        self.uploadRegion.setProperty( "hasFile", self.hasFile )
        self.regionSpacer.setProperty( "hasFile", self.hasFile )
        self.regionLabel.setProperty( "hasFile", self.hasFile )
        self.fileIcon.setProperty( "hasFile", self.hasFile )
        self.fileNameLabel.setProperty( "hasFile", self.hasFile )

        # Apply style
        with open(stylesheetPath, "r") as stylesheet:
            self.uploadRegion.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.regionSpacer.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.regionLabel.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.fileIcon.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.fileNameLabel.setStyleSheet( stylesheet.read() )

        # ----------------------------------------------------------------------------------------
        # Basic validation

        # Check file size
        fileSize = os.stat(self.filePathLabel.text()).st_size

        if ( fileSize == 0 ):
            print( "File: \"{}\" at location {} is empty.".format( self.filePathLabel.text(), self.fileNameLabel.text() ) )

            # Display empty error in this case
        
        else:
            print( "File: \"{}\" at location {} has size: {} bytes.".format( self.filePathLabel.text(), self.fileNameLabel.text(), fileSize ) )

            # In this case, file is not empty so check for variable definitions and initializations (varies by calibration file)
            if (self.uploadRegion.objectName() == "UploadFileRegion_Vignetting"):
                print( "Upload region is for vignetting. Validating..." )
                self.vc_validation()

            elif (self.uploadRegion.objectName() == "UploadFileRegion_FisheyeCorrection"):
                print( "Upload region is for fisheye correction. Validating..." )
                self.fc_validation()

            elif (self.uploadRegion.objectName() == "UploadFileRegion_CameraFactor"):
                print( "Upload region is for camera factor adjustment. Validating..." )
                self.cf_validation()

            elif (self.uploadRegion.objectName() == "UploadFileRegion_NeutralDensityFilter"):
                print( "Upload region is for neutral density filter adjustment. Validating..." )
                self.nd_validation()

            else:
                print( "Upload region is unknown. self.uploadRegion.objectName(): {}".format( self.uploadRegion.objectName() ) )

        # ----------------------------------------------------------------------------------------


        event.acceptProposedAction()


    # Remove button click event
    def removeBtnClicked( self ):
        # Set hasFile flag
        self.hasFile = False

        # Clear file name/path labels' text
        self.fileNameLabel.setText("")
        self.filePathLabel.setText("")

        # Hide file name label
        self.fileNameLabel.hide()

        # Hide file icon
        self.fileIcon.hide()

        # Hide removeBtn
        self.removeBtn.hide()


        # Adjust styling
        # Stylesheet path
        stylesheetPath = "./styles/upload_file_region_styles.css"

        # Set property for stylsheet to apply correct style
        self.uploadRegion.setProperty( "hasFile", self.hasFile )
        self.regionSpacer.setProperty( "hasFile", self.hasFile )
        self.regionLabel.setProperty( "hasFile", self.hasFile )
        self.fileIcon.setProperty( "hasFile", self.hasFile )
        self.fileNameLabel.setProperty( "hasFile", self.hasFile )

        # Apply style
        with open(stylesheetPath, "r") as stylesheet:
            self.uploadRegion.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.regionSpacer.setStyleSheet( stylesheet.read() )    
        with open(stylesheetPath, "r") as stylesheet:
            self.regionLabel.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.fileIcon.setStyleSheet( stylesheet.read() )
        with open(stylesheetPath, "r") as stylesheet:
            self.fileNameLabel.setStyleSheet( stylesheet.read() )


    # Get the filename from the path
    def getFilenameFromPath( self, path ):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    

    # Basic vignetting calibration (vc) file validation
    def vc_validation( self ):
        

        return
    

    # Basic fisheye correction calibration (fc) file validation
    def fc_validation( self ):
        return
    

    # Basic calibration factor calibration (cf) file validation
    def cf_validation( self ):
        return
    

    # Basic neutral density filter calibration (nd) file validation
    def nd_validation( self ):
        return



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1150, 840)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: #EAEAEA;")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.Top_Bar)


        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.sidebar_menu = QFrame(self.Content)
        self.sidebar_menu.setObjectName(u"sidebar_menu")
        self.sidebar_menu.setMinimumSize(QSize(220, 0))
        self.sidebar_menu.setMaximumSize(QSize(250, 4000))
        self.sidebar_menu.setStyleSheet(u"background-color: #A5A5A5;")
        self.sidebar_menu.setFrameShape(QFrame.StyledPanel)
        self.sidebar_menu.setFrameShadow(QFrame.Raised)
        
        self.sidebar_menu_v_layout = QVBoxLayout(self.sidebar_menu)
        self.sidebar_menu_v_layout.setObjectName(u"sidebar_menu_v_layout")
        self.sidebar_menu_v_layout.setContentsMargins(0, 0, 0, 0)

        self.frame_top_menus = QFrame(self.sidebar_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSpacing( 8 )
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)



        # ---------------------------------------------------------------------------------------
        # Setting up page-routing buttons in menu sidebar

        # Stylesheet path
        stylesheetPath = "./styles/main_styles.css"

        # Page 1 (Welcome landing page)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))

        # Set button styling
        with open(stylesheetPath, "r") as stylesheet:
            self.btn_page_1.setStyleSheet( stylesheet.read() )


        # Page 2 (Upload LDR images)
        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
       
        # Set button styling
        with open(stylesheetPath, "r") as stylesheet:
            self.btn_page_2.setStyleSheet( stylesheet.read() )


        # Page 3 (Adjust camera settings)
        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))

        # Set button styling
        with open(stylesheetPath, "r") as stylesheet:
            self.btn_page_3.setStyleSheet( stylesheet.read() )


        # Page 4 (Adjust calibration settings)
        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))

        # Set button styling
        with open(stylesheetPath, "r") as stylesheet:
            self.btn_page_4.setStyleSheet( stylesheet.read() )


        # Go button - Starts Radiance pipeline process
        self.btn_start_pipeline = QPushButton(self.frame_top_menus)
        self.btn_start_pipeline.setObjectName(u"btn_start_pipeline")
        self.btn_start_pipeline.setMinimumSize(QSize(0, 40))
        
        # Set button styling
        with open(stylesheetPath, "r") as stylesheet:
            self.btn_start_pipeline.setStyleSheet( stylesheet.read() )


        # Add Page 1-routing button to sidebar
        self.verticalLayout_4.addWidget(self.btn_page_1)

        # Add Page 2-routing button to sidebar
        self.verticalLayout_4.addWidget(self.btn_page_2)

        # Add Page 3-routing button to sidebar
        self.verticalLayout_4.addWidget(self.btn_page_3)

        # Add Page 4-routing button to sidebar
        self.verticalLayout_4.addWidget(self.btn_page_4)

        # Add Go button to sidebar
        self.verticalLayout_4.addWidget(self.btn_start_pipeline)

        # ---------------------------------------------------------------------------------------



        self.sidebar_menu_v_layout.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.sidebar_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(40)
        labelfont = QFont()
        labelfont.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color: #000;")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_1)
        self.stackedWidget.addWidget(self.page_1)
        # edit page 1
        #teampic = QVBoxLayout(self.page_1)

        self.label_p1 = QLabel(self.page_1)
        self.pixmap = QPixmap('officeteamstock.jpg')
        #self.label_p1 = self.pixmap.scaled(64, 64, Qt.KeepAspectRatio)
        self.label_p1.setPixmap(self.pixmap)
        self.label_p1.setAlignment(Qt.AlignCenter)
        #self.label_p1.resize(self.pixmap.width(), self.pixmap.height())
        self.label_p1.resize(100,100)
        self.label_p1.move(130,300)
        
        self.label_p1_title = QLabel(self.page_1)
        self.label_p1_title.setText("Meet The Team!")
        self.label_p1_title.setStyleSheet("font: 16pt \".AppleSystemUIFont\";")
        self.label_p1_title.adjustSize()
        self.label_p1_title.move(700,450)
        
        #page_1.addWidget(label_p1)
        self.label_p1.show()

        self.intro_para = QLabel(self.page_1)
        self.intro_para.setAlignment(Qt.AlignHCenter)
        self.intro_para.setText("The ALD lighting application is a crowd-sourced and free \n built by a group of college kids...")
        self.intro_para.setFont(labelfont)
        self.intro_para.adjustSize()
        self.intro_para.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.intro_para.move(20,20)
        self.intro_para.move(100,100)

        
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        #edit page 2 

        #uploading file setup begin -------
        def upload_response(self,fileName):
            self.label.setText(fileName)
            self.update()
        def update(self):
            self.label.adjustSize()
        def openFileNameDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"choose the desired .cal file", "",".Cal Files (*.cal)", options=options)
            file_list = []
            if fileName:
                print("file path imported: " + fileName)
                file_list += [fileName]
                self.file_label.setText(os.path.basename(fileName))
            list_val = []
            list_val = readFile(fileName)
            checkVal(list_val) 
       
        #self.uploadfilebutton = QtWidgets.QPushButton(self.page_4)
        
        #uploading file setup end --------
        

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #000;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")

        self.cameraSettingsPage = QVBoxLayout(self.page_3)
        self.cameraSettingsPage.setObjectName(u"cameraSettingsPage")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #000;")
        self.label_3.setAlignment(Qt.AlignCenter)


        self.mdiArea = QMdiArea(self.page_3)
        self.mdiArea.setGeometry(QRect(10, 10, 970, 250))
        self.mdiArea.setObjectName("mdiArea_2")

        self.mdiArea_2 = QMdiArea(self.page_3)
        self.mdiArea_2.setGeometry(QRect(10, 290, 970, 140))
        self.mdiArea_2.setObjectName("mdiArea_2")


        self.mdiArea_3 = QMdiArea(self.page_3)
        self.mdiArea_3.setGeometry(QRect(10, 460, 970, 140))
        self.mdiArea_3.setObjectName("mdiArea_3")


        self.mdiArea_4 = QMdiArea(self.page_3)
        self.mdiArea_4.setGeometry(QRect(10, 610, 970, 140))
        self.mdiArea_4.setObjectName("mdiArea_4")
        self.mdiArea_4.raise_()


        self.label_cd = QLabel(self.mdiArea)
        self.label_cd.setAlignment(Qt.AlignLeft)
        self.label_cd.setText("Cropping Dimensions")
        self.label_cd.setFont(labelfont)
        self.label_cd.adjustSize()
        self.label_cd.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_cd.setStyleSheet("background-color: #a0a0a0")
        self.label_cd.move(10,10)


        self.label_LVA = QLabel(self.mdiArea_2)
        self.label_LVA.setAlignment(Qt.AlignLeft)
        self.label_LVA.setText("Lens Viewing Angle")
        self.label_LVA.setFont(labelfont)
        self.label_LVA.adjustSize()
        self.label_LVA.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_LVA.setStyleSheet("background-color: #a0a0a0")
        self.label_LVA.move(10,10)
        self.label_LVA.raise_()


        self.label_OID = QLabel(self.mdiArea_3)
        self.label_OID.setAlignment(Qt.AlignLeft)
        self.label_OID.setText("Output Image Dimensions")
        self.label_OID.setFont(labelfont)
        self.label_OID.adjustSize()
        self.label_OID.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_OID.setStyleSheet("background-color: #a0a0a0")
        self.label_OID.move(10,10)
        self.label_OID.raise_()


        self.label_UCR = QLabel(self.mdiArea_4)
        self.label_UCR.setAlignment(Qt.AlignLeft)
        self.label_UCR.setText("Upload Camera Response File (.rsp)")
        self.label_UCR.setFont(labelfont)
        self.label_UCR.adjustSize()
        self.label_UCR.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_UCR.setStyleSheet("background-color: #a0a0a0")
        self.label_UCR.move(10,10)
        self.label_UCR.raise_()
        
        #mdi area 1 line edits 
        self.lineEdit_md11 = QLineEdit(self.mdiArea)
        self.lineEdit_md11.setText("")
        self.lineEdit_md11.setObjectName("lineEdit_md11")
        self.lineEdit_md11.move(10,100)


        self.lineEdit_md12 = QLineEdit(self.mdiArea)
        self.lineEdit_md12.setText("")
        self.lineEdit_md12.setObjectName("lineEdit_md12")
        self.lineEdit_md12.move(160,100)


        self.label_md11 = QLabel(self.mdiArea)
        self.label_md11.setAlignment(Qt.AlignLeft)
        self.label_md11.setText("x")
        self.label_md11.setStyleSheet("background-color: #a0a0a0")
        self.label_md11.move(149,102)


        self.label_iir = QLabel(self.mdiArea)
        self.label_iir.setAlignment(Qt.AlignLeft)
        self.label_iir.setText("Input Image Resolution")
        self.label_iir.setStyleSheet("background-color: #a0a0a0")
        self.label_iir.move(10,70)

        self.lineEdit_md13 = QLineEdit(self.mdiArea)
        self.lineEdit_md13.setText("")
        self.lineEdit_md13.setObjectName("lineEdit_md13")
        self.lineEdit_md13.move(10,200)

        self.label_md13 = QLabel(self.mdiArea)
        self.label_md13.setAlignment(Qt.AlignLeft)
        self.label_md13.setText("Fisheye View Diameter")
        self.label_md13.setStyleSheet("background-color: #a0a0a0")
        self.label_md13.move(10,180)

        self.label_md14 = QLabel(self.mdiArea)
        self.label_md14.setAlignment(Qt.AlignLeft)
        self.label_md14.setText("X Crop Offset")
        self.label_md14.setStyleSheet("background-color: #a0a0a0")
        self.label_md14.move(500,70)

        self.lineEdit_md14 = QLineEdit(self.mdiArea)
        self.lineEdit_md14.setText("")
        self.lineEdit_md14.setObjectName("lineEdit_md14")
        self.lineEdit_md14.move(500,100)

        self.label_md15 = QLabel(self.mdiArea)
        self.label_md15.setAlignment(Qt.AlignLeft)
        self.label_md15.setText("Y Crop Offset")
        self.label_md15.setStyleSheet("background-color: #a0a0a0")
        self.label_md15.move(500,180)

        self.lineEdit_md15 = QLineEdit(self.mdiArea)
        self.lineEdit_md15.setText("")
        self.lineEdit_md15.setObjectName("lineEdit_md15")
        self.lineEdit_md15.move(500,200)

        self.area1button = QPushButton('Enter', self.mdiArea)
        self.area1button.move(200,300)
        #area1button.clicked.connect(self.on_click)

        #area 2 edit 
        
        self.lineEdit_md21 = QLineEdit(self.mdiArea_2)
        self.lineEdit_md21.setText("")
        self.lineEdit_md21.setObjectName("lineEdit_md21")
        self.lineEdit_md21.move(10,90)

        self.label_md21 = QLabel(self.mdiArea_2)
        self.label_md21.setAlignment(Qt.AlignLeft)
        self.label_md21.setText("View Angle Vertical")
        self.label_md21.setStyleSheet("background-color: #a0a0a0")
        self.label_md21.move(10,70)

        self.label_md22 = QLabel(self.mdiArea_2)
        self.label_md22.setAlignment(Qt.AlignLeft)
        self.label_md22.setText("View Angle Horizontal")
        self.label_md22.setStyleSheet("background-color: #a0a0a0")
        self.label_md22.move(250,70)

        self.lineEdit_md22 = QLineEdit(self.mdiArea_2)
        self.lineEdit_md22.setText("")
        self.lineEdit_md22.setObjectName("lineEdit_md22")
        self.lineEdit_md22.move(250,90)

        #area 3 edit

        self.label_md31 = QLabel(self.mdiArea_3)
        self.label_md31.setAlignment(Qt.AlignLeft)
        self.label_md31.setText("HDR Image Output Resolution")
        self.label_md31.setStyleSheet("background-color: #a0a0a0")
        self.label_md31.move(10,70)

        self.lineEdit_md31 = QLineEdit(self.mdiArea_3)
        self.lineEdit_md31.setText("")
        self.lineEdit_md31.setObjectName("lineEdit_md31")
        self.lineEdit_md31.move(10,90)

        self.label_md31x = QLabel(self.mdiArea_3)
        self.label_md31x.setAlignment(Qt.AlignLeft)
        self.label_md31x.setText("x")
        self.label_md31x.setStyleSheet("background-color: #a0a0a0")
        self.label_md31x.move(149,92)

        self.lineEdit_md32 = QLineEdit(self.mdiArea_3)
        self.lineEdit_md32.setText("")
        self.lineEdit_md32.setObjectName("lineEdit_md32")
        self.lineEdit_md32.move(160,90)


        #area 4 upload rsp

       # self.cameraSettingsPage = QVBoxLayout(self.page_3)
        self.cameraSettingsPage.setContentsMargins( 0, 0, 0, 0 )
        self.cameraSettingsPage.setSpacing( 4 )
        self.cameraSettingsPage.setMargin( 0 )

        rsp_uploadarea = UploadFileRegion("Camera Response File Upload (.rsp)",[0, 0], [900, 200] )
        
        self.cameraSettingsPage.addWidget( rsp_uploadarea, 25 )

        
        # Adding page_4 QWidget
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")

        # -------------------------------------------------------------------------------------------------
        # Upload file regions
        # Create new layout for self.page_4
        self.calibrationPage = QVBoxLayout( self.page_4 )
        self.calibrationPage.setContentsMargins( 0, 0, 0, 0 )
        self.calibrationPage.setSpacing( 4 )
        self.calibrationPage.setMargin( 0 )
        

        # Vignetting region
        # Add widget: UploadFileRegionObject class object
        vc_UploadRegion = UploadFileRegion( "Vignetting", [0, 0], [900, 200] )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( vc_UploadRegion, 25 )

        # Fisheye correction region
        # Add widget: UploadFileRegionObject class object
        fc_UploadRegion = UploadFileRegion( "FisheyeCorrection", [0, 0], [900, 200] )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( fc_UploadRegion, 25 )

        # Camera factor region
        # Add widget: UploadFileRegionObject class object
        cf_UploadRegion = UploadFileRegion( "CameraFactor", [0, 0], [900, 200] )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( cf_UploadRegion, 25 )

        # Neutral Density Filter region
        # Add widget: UploadFileRegionObject class object
        nd_UploadRegion = UploadFileRegion( "NeutralDensityFilter", [0, 0], [900, 200] )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( nd_UploadRegion, 25 )

        # -------------------------------------------------------------------------------------------------



        #adding page 5 element
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #000;")
        self.label_5.setAlignment(Qt.AlignCenter)
        #adding page 5 element end 

        self.cameraSettingsPage.addWidget(self.label_3)
        self.verticalLayout_10.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_3)
        self.stackedWidget.addWidget(self.page_4)
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HDRI Calibration Tool", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Upload LDR images", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Upload Calibration", None))
        self.btn_start_pipeline.setText(QCoreApplication.translate("MainWindow", u"GO!", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label_1.setAlignment(Qt.AlignHCenter)
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        #self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE 5", None))



def checkVal(list_val): #checking values of .cal files
    print(" (checkVal function running) ")#compare value
    if list_val[0] == "this": #placeholder
        print("correct")



def readFile(fileName):
    f = open(fileName,"r")
    list_val = []
    lines = f.readlines()
    print(lines)
    for i in lines:
        list_val.append (i.replace(";\n",""))
    print(list_val)
    return list_val



def upload_response(self,fileName):
    self.label.setText(fileName)
    self.update()



def update(self):
    self.label.adjustSize()



def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self,"choose the desired .cal file", "",".Cal Files (*.cal)", options=options)
    file_list = []
    if fileName:
        print("file path imported: " + fileName)
        file_list += [fileName]
        self.file_label.setText(os.path.basename(fileName))
    list_val = []
    list_val = readFile(fileName)
    checkVal(list_val) 
