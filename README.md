# GUI_for_createdSampling_schedule
This is a Graphical user interphase allowing user to create test and inspect random sampling schedule based on random distribution chosen by the user as well as other desired indexing convention to be used in undersampling signal reconstruction. It is built using PYQT5 on python 3.5

Prerequisites:

install python3.5
install numpy
install scipy
install pyqt5-developer

Compiling and running:

To edit the UI:
	open pyqt5 designer (aliased on this machine to qt5-designer)

	to compile the ui : 
 		From the src folder run:
		pyuic5 ../ui/Main.ui -o MainWindow.py 

To Run the application:
	from the src folder run:
		python3.5 Program.py
