import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QTextEdit, QVBoxLayout, QWidget, QFileDialog)

class FileViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ralf's PyQt File Viewer")
        self.resize(800, 600)

        # Zentrales Widget und Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # UI Komponenten
        self.btn_open = QPushButton("Datei auswählen...")
        self.btn_open.clicked.connect(self.open_file_dialog)
        
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)

        layout.addWidget(self.btn_open)
        layout.addWidget(self.text_display)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Datei öffnen", "", "Textdateien (*.txt);;Alle Dateien (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_display.setPlainText(content)
            except Exception as e:
                self.text_display.setPlainText(f"Fehler beim Lesen der Datei: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileViewer()
    window.show()
    sys.exit(app.exec())