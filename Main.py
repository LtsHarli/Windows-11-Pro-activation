import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QListWidget, QDialog
from PyQt5.QtCore import QTimer
import subprocess
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print("Exception occurred while checking admin privileges:", e)
        return False

class SelectWindowsVersionWindow(QDialog):
    def __init__(self, windows_versions):
        super().__init__()

        self.setWindowTitle("Select Windows Version")

        self.layout = QVBoxLayout()

        label = QLabel("Select Windows Version:")
        self.layout.addWidget(label)

        self.version_listbox = QListWidget()
        for version in windows_versions.keys():
            self.version_listbox.addItem(version)
        self.layout.addWidget(self.version_listbox)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.on_ok)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

        self.selected_version = ""
        self.selected_product_key = ""

    def on_ok(self):
        selected_items = self.version_listbox.selectedItems()
        if selected_items:
            self.selected_version = selected_items[0].text()
            self.selected_product_key = windows_versions.get(self.selected_version)
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Please select a Windows version.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windows Activation Tool")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        label = QLabel("Windows Activation Tool")
        font = label.font()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        label.setFont(font)
        self.layout.addWidget(label)

        self.run_part_one_button = QPushButton("Part One")
        self.run_part_one_button.clicked.connect(self.run_part_one)
        self.layout.addWidget(self.run_part_one_button)

        self.run_part_two_button = QPushButton("Part Two")
        self.run_part_two_button.clicked.connect(self.run_part_two)
        self.layout.addWidget(self.run_part_two_button)

        self.output_text = QTextEdit()
        self.layout.addWidget(self.output_text)

        self.central_widget.setLayout(self.layout)

    def run_part_one(self):
        select_windows_version_window = SelectWindowsVersionWindow(windows_versions)
        if select_windows_version_window.exec_() == QDialog.Accepted:
            selected_version = select_windows_version_window.selected_version
            selected_product_key = select_windows_version_window.selected_product_key

            if selected_version and selected_product_key:
                self.run_part_one_button.setEnabled(False)
                self.run_part_two_button.setEnabled(False)
                self.output_text.clear()
                self.output_text.append(f"Selected Windows Version: {selected_version}\n")
                self.output_text.append("Running Part One...\n\n")
                for command in commands:
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    self.output_text.append(f"{process.communicate()[0]}\n\n")

                activation_command = f"slmgr /ipk {selected_product_key}"
                process = subprocess.Popen(activation_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                self.output_text.append(f"Activating Windows {selected_version}...\n{process.communicate()[0]}\n\n")

                self.output_text.append("Part one is now finished. Please restart the computer and run Part Two.")
                self.timer = QTimer()
                self.timer.singleShot(15000, self.enable_buttons)
            else:
                QMessageBox.critical(self, "Error", "Please select a Windows version.")

    def run_part_two(self):
        self.output_text.clear()
        self.output_text.append("Running Part Two...\n\n")
        for command in commands_part_two:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            self.output_text.append(f"{process.communicate()[0]}\n\n")
        self.output_text.append("You should now have Windows 11 Pro. I would suggest restarting your PC, but it is not needed.")

    def enable_buttons(self):
        self.run_part_one_button.setEnabled(True)
        self.run_part_two_button.setEnabled(True)

# Windows versions and their product keys
windows_versions = {
    "Windows 11 Home": "YTMG3-N6DKC-DKB77-7M9GH-8HVX7",
    "Windows 11 Pro": "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "Windows 11 Enterprise": "XGVPP-NMH47-7TTHJ-W3FW7-8HV2C"
}

# Commands for Part One
commands = [
    "cscript //nologo %windir%\\system32\\slmgr.vbs /upk",
    "cscript //nologo %windir%\\system32\\slmgr.vbs /cpky",
    "cscript //nologo %windir%\\system32\\slmgr.vbs /ckms",
    "Dism /online /Get-TargetEditions",
    "sc config LicenseManager start= auto & net start LicenseManager",
    "sc config wuauserv start= auto & net start wuauserv",
]

# Commands for Part Two
commands_part_two = [
    "slmgr /skms kms8.msguides.com",
    "slmgr /ato"
]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
