import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QRadioButton, QFormLayout

# Create a PyQt application
app = QApplication(sys.argv)

# Create a QWidget (main window)
widget = QWidget()

# Create a vertical layout for the main window
layout = QVBoxLayout(widget)

# Create a QPushButton
button = QPushButton("Click me!")

# Create a QLabel
label = QLabel("Hello, PyQt5!")

# Create a QLineEdit
line_edit = QLineEdit("Type here...")

# Create a QTextEdit
text_edit = QTextEdit("Multi-line input...")

# Create a QComboBox and add items
combo_box = QComboBox()
combo_box.addItems(["Option 1", "Option 2", "Option 3"])

# Create two QRadioButtons with labels
radio_button1 = QRadioButton("Radio 1")
radio_button2 = QRadioButton("Radio 2")

# Add the widgets to the layout
layout.addWidget(button)
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(text_edit)
layout.addWidget(combo_box)
layout.addWidget(radio_button1)
layout.addWidget(radio_button2)

# Add a QFormLayout with three label-input pairs
form_layout = QFormLayout()
form_layout.addRow("Name:", QLineEdit())
form_layout.addRow("Age:", QLineEdit())
form_layout.addRow("City:", QLineEdit())

# Add the QFormLayout to the existing layout
layout.addLayout(form_layout)

# Show the main window
widget.show()

# Start the application event loop
sys.exit(app.exec_())
