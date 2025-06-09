"""
Application de gestion des commandes et paiements
Point d'entrée principal de l'application
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    """Fenêtre principale de l'application."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Commandes")
        self.setGeometry(100, 100, 800, 600)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout vertical
        layout = QVBoxLayout(central_widget)
        
        # Ajouter un label de bienvenue
        welcome_label = QLabel("Bienvenue dans l'application de Gestion des Commandes")
        welcome_label.setStyleSheet("font-size: 18px; margin: 20px;")
        layout.addWidget(welcome_label)

def main():
    """Point d'entrée de l'application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()