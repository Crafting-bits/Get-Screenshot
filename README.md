# Get-Screenshot
Simple desktop app, which creates a screenshot using Alt + F12.
Necessary libraries: (os, sys, pyautogui, keyboard, pathlib, PyQt5.QtWidgets, PyQt5.QtGui)

Description:
The Desktop Screenshot Tool is a Python-based desktop application that facilitates in selecting a folder and capturing screenshots using a simple graphical interface. The application is built utilizing Python's libraries to enable folder selection and screenshot capture.

Functionality Overview:

Folder Selection: The application allows users to navigate their file system and select a folder of their choice. This functionality is achieved through the integration of QFileDialog from PyQt5, enabling an folder selection process.

Screenshot Capture: Upon selecting a folder, users have the capability to capture screenshots using the application. This functionality uses the pyautogui library, providing a straightforward method to capture screenshots.

Libraries Used:

os: This standard library in Python provides functionality to interact with the operating system, facilitating tasks such as directory operations.

sys: Another core library in Python that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

pyautogui: A cross-platform GUI automation library used to take screenshots and perform various GUI interactions.

keyboard: A library used for interacting with and controlling the keyboard input events.

pathlib: This library provides classes representing filesystem paths with semantics appropriate for different operating systems.

PyQt5: A comprehensive set of Python bindings for Qt v5 used for creating desktop applications with graphical user interfaces (GUIs).

Code Structure Overview:

Main Script (Get_Screen.pyw): Contains all code of the application, including the GUI setup using PyQt5, folder selection functionality, and integration with pyautogui for capturing screenshots.

Function Definitions: The application may contain several function definitions responsible for handling events, capturing screenshots, managing folders, and interacting with the GUI elements.

GUI Implementation (QMainWindow, QPushButton, QLabel): Utilizes PyQt5's classes and methods to create a user-friendly graphical interface with buttons, labels, and other elements, providing a seamless user experience.

Usage Instructions:

Installation: To use the application, ensure all required libraries (os, sys, pyautogui, keyboard, pathlib, PyQt5) are installed in your Python environment.

Execution: Run the Get_Screen.pyw script, which initializes the application and presents the graphical interface. Follow on-screen instructions to select a folder and capture screenshots as needed.

Conclusion:

The Desktop Screenshot Tool offers an intuitive and efficient solution for users to select folders and capture screenshots within a user-friendly graphical environment. Leveraging powerful libraries in Python, the application provides a seamless experience for users requiring such functionality.

