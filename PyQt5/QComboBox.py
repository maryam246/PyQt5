import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

# Create a PyQt application
app = QApplication(sys.argv)

# Create a QWidget (main window)
widget = QWidget()

# Create a QGridLayout
grid_layout = QGridLayout(widget)

# Add widgets to the layout
grid_layout.addWidget(QPushButton("Button 1"), 0, 0)
grid_layout.addWidget(QPushButton("Button 2"), 0, 1)
grid_layout.addWidget(QPushButton("Button 4"), 1, 0, 1, 2)  # Spanning two columns
# Show the main window
widget.show()

# Start the application event loop
sys.exit(app.exec_())
