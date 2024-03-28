import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QRadioButton
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windows Activation Tool")
        self.setGeometry(100, 100, 400, 200)

        self.setStyleSheet("background-color: #000000; color: #ffffff;")

        self.layout = QVBoxLayout()

        self.label = QLabel("Welcome to Windows Activation Tool")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.buttons_group = QGroupBox()
        self.buttons_group.setStyleSheet("QGroupBox { border: none; }")
        self.buttons_layout = QHBoxLayout()

        self.install_button = QPushButton("Install Key (Run First)")
        self.install_button.clicked.connect(self.run_part1)
        self.install_button.setStyleSheet(
            "QPushButton {"
            "background-color: #4CAF50;"
            "border: none;"
            "color: #ffffff;"
            "padding: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: #45a049;"
            "}"
            "QPushButton:pressed {"
            "background-color: #367d39;"
            "}"
        )
        self.buttons_layout.addWidget(self.install_button)

        self.activate_button = QPushButton("Activate Key")
        self.activate_button.clicked.connect(self.run_part2)
        self.activate_button.setStyleSheet(
            "QPushButton {"
            "background-color: #4CAF50;"
            "border: none;"
            "color: #ffffff;"
            "padding: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: #45a049;"
            "}"
            "QPushButton:pressed {"
            "background-color: #367d39;"
            "}"
        )
        self.buttons_layout.addWidget(self.activate_button)

        self.buttons_group.setLayout(self.buttons_layout)
        self.layout.addWidget(self.buttons_group)

        self.theme_toggle_button = QPushButton()
        self.theme_toggle_button.setFixedSize(20, 20)
        self.theme_toggle_button.setCheckable(True)
        self.theme_toggle_button.setChecked(True)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)
        self.theme_toggle_button.setStyleSheet(
            "QPushButton {"
            "background-color: #eeeeee;"
            "border: none;"
            "}"
            "QPushButton:checked {"
            "background-color: #222222;"
            "}"
            "QPushButton:hover {"
            "background-color: #dddddd;"
            "}"
        )

        self.layout.addWidget(self.theme_toggle_button, alignment=Qt.AlignRight | Qt.AlignTop)

        self.setLayout(self.layout)

    def run_part1(self):
        self.label.setText("Running Part One...")

        commands = [
            "cscript //nologo %windir%\\system32\\slmgr.vbs /upk",
            "cscript //nologo %windir%\\system32\\slmgr.vbs /cpky",
            "cscript //nologo %windir%\\system32\\slmgr.vbs /ckms",
            "Dism /online /Get-TargetEditions",
            "sc config LicenseManager start= auto",
            "net start LicenseManager",
            "sc config wuauserv start= auto",
            "net start wuauserv",
            "changepk.exe /productkey VK7JG-NPHTM-C97JM-9MPGT-3V66T"
        ]

        for cmd in commands:
            subprocess.run(cmd, shell=True)

        self.label.setText("Part One finished. Please restart the computer and run part two.")

    def run_part2(self):
        self.label.setText("Running Part Two...")

        commands = [
            "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX",
            "slmgr /skms kms8.msguides.com",
            "slmgr /ato"
        ]

        for cmd in commands:
            subprocess.run(cmd, shell=True)

        self.label.setText("Part Two finished. You should now have Windows 11 Pro.")

    def toggle_theme(self):
        if self.theme_toggle_button.isChecked():
            self.setStyleSheet("")
            self.activate_button.setStyleSheet("")
            self.install_button.setStyleSheet("")
        else:
            self.setStyleSheet(
                "background-color: #2b2b2b; color: #ffffff"
            )
            self.activate_button.setStyleSheet(
                "background-color: #4CAF50; color: #ffffff"
            )
            self.install_button.setStyleSheet(
                "background-color: #4CAF50; color: #ffffff"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
