import os
import sys
import pyautogui
import keyboard
        
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QLabel,QFileDialog
from PyQt5.QtGui import QFont
        
        
class MyWindow(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        self.screenshot_path = None # Declare "self.screenshot_path" with no value at the beginning.
        
        
    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Get_Screen')
        self.setFixedSize(600, 200) # Resize the window.
        
        center_point = QDesktopWidget().availableGeometry().center() # Calculate the center of the screen.
        
        center_window = center_point - self.rect().center()
        self.move(center_window) # Method to center the window at startup.
        
        button = QLabel('Press Alt + F12', self)
        button.setGeometry(225, 50, 200, 60) # Change element position in interface.
        font = QFont()
        font.setPointSize(10) # Change the font size of QLabel.
        button.setFont(font)
        
        folderpath = QPushButton('Select Folder', self)
        folderpath.setGeometry(210, 100, 150, 40)
        folderpath.clicked.connect(self.selectFolder) # Call selectFolder(self) on click.
        
    def selectFolder(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options) # Create variable with the folder location.
        self.screenshot_path = os.path.join(folder_path, "Screenshot.png") # Use "os" library to add name and extension to the file.
        keyboard.add_hotkey('alt+f12', self.getScreenshot) # Create the keyboard shortcut and call getScreenshot(self). This is important, the Shortcut should only be generated after pressing the button.
        
    def getScreenshot(self):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(self.screenshot_path) # Save the file in the selected folder.
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
