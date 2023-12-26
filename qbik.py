import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class DiceSimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.kol = 0
        self.br = 0
        self.data = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_kol = QLabel("Сколько кубиков?")
        layout.addWidget(self.label_kol)

        self.input_kol = QLineEdit()
        layout.addWidget(self.input_kol)

        self.label_br = QLabel("Сколько бросков?")
        layout.addWidget(self.label_br)

        self.input_br = QLineEdit()
        layout.addWidget(self.input_br)

        self.submit_button = QPushButton("Запустить симуляцию")
        self.submit_button.clicked.connect(self.run_simulation)
        layout.addWidget(self.submit_button)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle("Симулятор кубиков")

    def run_simulation(self):
        self.kol = int(self.input_kol.text())
        self.br = int(self.input_br.text())
        self.data = []

        for l in range(self.br):
            count = 0
            for i in range(self.kol):
                a = randint(1, 6)
                count += a
            self.data.append(count)
            if l % 1000 == 0:
                self.result_text.append(f'{l} из {self.br // 1000}')

        self.data.sort()
        self.result_text.append(str(self.data))

        for h in range(self.kol, (self.kol * 6) + 1):
            gg = self.data.count(h)
            self.result_text.append(f'Вероятность выпадения {h}: {gg / self.br * 100}%')

def run_dice_simulator():
    app = QApplication(sys.argv)
    simulator = DiceSimulator()
    simulator.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_dice_simulator()