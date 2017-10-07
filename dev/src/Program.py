
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from matplotlib.ticker import NullFormatter
from numpy import *
from PyQt5 import QtCore, QtGui, QtWidgets
import random as ran
from scipy.integrate import quad
import sys

from MainView import Ui_MainWindow


class SimulationThread(QtCore.QThread):
  finished = QtCore.pyqtSignal()
  error = QtCore.pyqtSignal(str)

  def __init__(self, mainWindow):
    QtCore.QThread.__init__(self)
    self.mainWindow = mainWindow

  def __del__(self):
    self.wait()

  def run(self):
    timeRange = self.textToList(self.mainWindow.timeRangeInput.toPlainText())
    decay = self.textToList(self.mainWindow.decayInput.toPlainText())
    samplingPortionT = self.mainWindow.samplingInput.toPlainText()
    expDecayEvalInput = self.mainWindow.expDecayEvalInput.toPlainText()
    sim = Simulation(expDecayEvalInput.strip())

    try:
      samplingPortion = float(samplingPortionT.strip())
    except Exception as e:
      self.error.emit("Sampling Portion must be a float")
      return

    if not len(timeRange):
      self.error.emit("Invalid time range, must be a comma seperated list of integerrs (i.e. 100, 100, 100)")
      return

    if not len(decay):
      self.error.emit("Invalid decay, must be a comma seperated list of integers (i.e. -3, -6, -3)")
      return

    if len(timeRange) != len(decay):
      self.error.emit("Time Range and Decay must be the same length")
      return

    if samplingPortion < 0:
      self.error.emit("The sampling portion must be greater than 0")
      return

    if samplingPortion > 100:
      self.error.emit("The sampling portion must be less than 100")
      return


    try:
      grid, self.mainWindow.VClists = self.runSimulation(timeRange, decay, samplingPortion, sim)
      self.mainWindow.grid = copy(grid)
    except Exception as e:
      self.error.emit("Something went wrong: " + str(e))
      
    self.mainWindow.timeRange = timeRange
    self.finished.emit()

  def runSimulation(self, timeRange, decay, samplingPortion, sim):
    grid, VClists = sim.baisRandomList(timeRange, decay, samplingPortion, self.getNormalisationMethod())
    return grid, VClists

  def textToList(self, text):
    textList = text.split(',')
    result = []
    for s in textList:
      try:
        temp = int(s.strip())
      except:
        return []

      result.append(temp)
    return result
 
  def getNormalisationMethod(self):
    if self.mainWindow.normalisationMethod_1.isChecked():
      return 1

    elif self.mainWindow.normalisationMethod_2.isChecked():
      return 2

    return 0


class MainWindowView(Ui_MainWindow):

  def __init__(self, mainWindow):
    Ui_MainWindow.__init__(self)
    self.setupUi(mainWindow)

# a figure instance to plot on
    self.dimensionsLbl.hide()
    self.figure = plt.figure()
    self.canvas = FigureCanvas(self.figure)
    self.toolbar = NavigationToolbar(self.canvas, self.graphWidget)
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(self.toolbar)
    layout.addWidget(self.canvas)
    self.graphWidget.setLayout(layout)

    #Set up laoding spinner
    self.movie = QtGui.QMovie('loading.gif', QtCore.QByteArray())
    self.movie.setCacheMode(QtGui.QMovie.CacheAll)
    self.movie.setSpeed(100)
    self.loadingSpinnerLbl.setMovie(self.movie)
    self.movie.stop()
    self.loadingSpinnerLbl.hide()
    self.loadingLbl.hide()

    self.VClists = []
    self.timeRange = 0
    self.grid = []

    self.runSimulationBtn.clicked.connect(self.handleRunClicked)
    self.saveOutputBtn.clicked.connect(self.saveOutput)

  def showControls(self):
    self.timeRangeInput.show()
    self.decayInput.show()
    self.samplingInput.show()
    self.expDecayEvalInput.show()
    self.timeRangeLbl.show()
    self.decayLbl.show()
    self.samplingLbl.show()
    self.expDecayEvalLbl.show()
    self.normalisationLbl.show()
    self.runSimulationBtn.show()
    self.saveOutputBtn.show()       
    self.graphWidget.show()
    self.normalisationBox.show()
    self.printOptionsGroup.show()
    self.startFromGroup.show()
    self.vclistSizeLbl.show()
    self.vclistSizeValueLbl.show()
    self.timeVolumeLbl.show()
    self.timeVolumeValueLbl.show()

    self.loadingSpinnerLbl.hide()
    self.loadingLbl.hide()
    self.movie.stop()

  def hideControls(self):
    self.timeRangeInput.hide()
    self.decayInput.hide()
    self.samplingInput.hide()
    self.expDecayEvalInput.hide()
    self.timeRangeLbl.hide()
    self.decayLbl.hide()
    self.samplingLbl.hide()
    self.expDecayEvalLbl.hide()
    self.normalisationLbl.hide()
    self.runSimulationBtn.hide()
    self.saveOutputBtn.hide()    
    self.graphWidget.hide()
    self.normalisationBox.hide()
    self.printOptionsGroup.hide()
    self.startFromGroup.hide()
    self.vclistSizeLbl.hide()
    self.vclistSizeValueLbl.hide()
    self.timeVolumeLbl.hide()
    self.timeVolumeValueLbl.hide()
    self.dimensionsLbl.hide()

    self.movie.start()
    self.loadingSpinnerLbl.show()
    self.loadingLbl.show()

  def saveOutput(self):
    fileDialog = QtWidgets.QFileDialog()
    fileDialog.setLabelText(QtWidgets.QFileDialog.Accept, "Save")
    fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
    if fileDialog.exec_():
      filenames = fileDialog.selectedFiles()
      name = filenames[0]

      try:
        if (name):
          file = open(name, 'w')
          body = self.formatVCList()
          file.write(body)
          file.close()
      except Exception as e:
        launchErrorDialog("Could not print: " + e)    

  def formatVCList(self):
    if self.printMethodSingleBtn.isChecked():
      return self.printSingleLine()

    elif self.printMethodMultiBtn.isChecked():
      return self.printMultiLine()

    return self.printRaw()

  def printSingleLine(self):
    startingValue = self.getStartingValue()
    offset = 0
    if startingValue == 0:
      offset = 1

    temp = ""

    for j in range(0, len(self.VClists[0])):
      for i in range(0, len(self.VClists)):
        temp = temp + str(self.VClists[i][j] - offset) + "\n"

    return temp

  def printMultiLine(self):
    startingValue = self.getStartingValue()
    offset = 0
    if startingValue == 0:
      offset = 1

    temp = ""

    for j in range(0, len(self.VClists[0])):
      for i in range(0, len(self.VClists)):
        temp = temp + str(self.VClists[i][j] - offset) + self.getSpacer(str(self.VClists[i][j] - offset))
      temp = temp + "\n"

    return temp

  def printRaw(self):
    startingValue = self.getStartingValue()
    if startingValue == 0:
      temp = deepcopy(self.VClists)

      for i in range(0, len(temp)):
        for j in range(0, len(temp[i])):
          temp[i][j] -= 1

      return str(temp)

    return str(self.VClists)


  def getSpacer(self, value):
    spaces = 5 - len(value)
    tmp = ""

    if spaces < 1:
      return " "

    for i in range(0, spaces):
      tmp = tmp + " "

    return tmp

  def getStartingValue(self):
    if self.startFrom0.isChecked():
      return 0

    return 1

  def handleRunClicked(self):
    self.hideControls()
    self.get_thread = SimulationThread(self)
    self.get_thread.finished.connect(self.handleSimCompletion)
    self.get_thread.error.connect(self.launchErrorDialog)
    self.get_thread.start()

  def handleSimCompletion(self):
    self.showControls()
    self.drawGraph(self.timeRange)

    self.printSizeOfVCList()
    self.printTimeVolume()

  def printSizeOfVCList(self):
    result = len(self.VClists[0])

    self.vclistSizeValueLbl.setText(str(result))

  def printTimeVolume(self):
    result = 1

    for lst in self.timeRange:
      result *= lst

    result = int(result * (float(self.samplingInput.toPlainText())/100))

    self.timeVolumeValueLbl.setText(str(result))

  def drawGraph(self, timeRange):
    #clear any old graphs
    self.figure.clf()
    self.dimensionsLbl.hide()

    if len(timeRange) == 3:
      self.create3DGraph(timeRange)
    elif len(timeRange) == 2:
      self.create2DGraph(timeRange)
    elif len(timeRange) == 1:
      self.create1DGraph(timeRange)
    else:
      self.dimensionsLbl.show()
      self.graphWidget.hide()

  def create1DGraph(self, timeRange):
    subplot(2,1,1)
    ax = self.figure.add_subplot(211)
    t = arange(timeRange[0])
    ax.scatter(t, self.grid)
    bx = self.figure.add_subplot(212)
    Y = fft.fft(self.grid)
    Y1,Y2 = hsplit(Y, 2)
    Y = hstack((Y2, Y1))
    f = arange(len(Y))
    bx.plot(f, abs(Y), 'r')
    bx.set_xlabel('Freq (Hz)')
    bx.set_ylabel('|Y(freq)|')
    self.canvas.draw()

  def create2DGraph(self, timeRange):
    x = self.VClists[0]
    y = self.VClists[1]

    nullfmt = NullFormatter()  # no labels

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    figure(2, figsize=(8, 8))

    axScatter = self.figure.add_axes(rect_scatter)
    axScatter.hold(False)
    axHistx = self.figure.add_axes(rect_histx)
    axHistx.hold(False)
    axHisty = self.figure.add_axes(rect_histy)
    axHisty.hold(False)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 10
    xymax = max([max(np.fabs(x)), max(np.fabs(y))])
    lim = (int(xymax / binwidth)) * binwidth

    axScatter.set_xlim((1, lim))
    axScatter.set_ylim((1, lim))

    bins = arange(1, lim + binwidth, binwidth)
    axHistx.hist(x, bins=bins)
    axHisty.hist(y, bins=bins, orientation='horizontal')

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())

    self.canvas.draw()

  def create3DGraph(self, timeRange):
    ax = self.figure.add_subplot(111, projection='3d')
    ax.hold(False)
    xs = self.VClists[0]
    ys = self.VClists[1]
    zs = self.VClists[2]
    ax.scatter(xs, ys, zs, c = 'r', marker = '.')
    ax.set_xlim3d(0, timeRange[0])
    ax.set_ylim3d(0, timeRange[1])
    ax.set_zlim3d(0, timeRange[2])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    self.canvas.draw()

  def launchErrorDialog(self, message):
    QtWidgets.QMessageBox.information(None, "OK", message)
    self.showControls()



class Simulation:

  def __init__(self, expDecay=""):
    self.expDecayEval = expDecay

  def __createGrid(self, input):
    tmp = []
    grid = 0
    for elem in input[::-1]: #iterate over the list in reverse
      for i in range(0, elem):
        tmp.append(grid)
      grid = tmp
      tmp = []

    return grid

  def __expDecay(self, t, b):
    if self.expDecayEval != "" and self.expDecayEval is not None:
      y = eval(self.expDecayEval)
    else:
      y = exp(float(b)*float(t))

    #y = (sin(float(t)*pi)*-1)+1+(float(b)/100)   #eval
    #y = t
    return y

  def __applyTimeRange(self, grid, timeRange, position=0):
    if (position == len(timeRange) - 1 ):
      grid[timeRange[position] - 1] = 1
      return grid
    else:
      grid[timeRange[position] - 1] = self.__applyTimeRange(grid[timeRange[position] - 1], timeRange, position + 1)
      return grid

  def __setInitialValueTo1(self, grid, timeRange, position=0):
    if (position == len(timeRange) - 1 ):
      grid[0] = 1
      return grid
    else:
      grid[0] = self.__setInitialValueTo1(grid[0], timeRange, position + 1)
      return grid

  def normMethod1(self, timeRange):
    return timeRange

  def normMethod2(self, timeRange):
    timeRange[0] = 200
    return timeRange

  def baisRandomList (self, timeRange, decay, samplingPortion, normalisationMethod):
    #Use this block to normalise the data, it can be moved into the correct place

    if normalisationMethod == 1:
      timeRange = self.normMethod1(timeRange)      

    elif normalisationMethod == 2:
      timeRange = self.normMethod2(timeRange)      

    VClists = []
    grid = asarray(self.__createGrid(timeRange))
    grid = self.__applyTimeRange(grid, timeRange)
    grid = self.__setInitialValueTo1(grid, timeRange)

    for i in timeRange:
      VClists.append([])

    counter = 0
    for VClist in VClists:
      VClist.append(1)
      VClist.append(timeRange[counter])
      counter = counter + 1

    dimensionalIntegrals = []
    for dec in decay:
      dimensionalIntegrals.append(quad(self.__expDecay,0,1, args=(dec,))[0])

    decayVolume = 0
    counter = 0
    for integral in dimensionalIntegrals:
      if counter == 0:
          decayVolume = integral
      else:
          decayVolume *= integral

      counter = counter + 1

    Condition = (samplingPortion/100.)/decayVolume  # comparing demand with expectation

    it=nditer(grid,flags=['multi_index'], op_flags=['writeonly'])

    shrink = 1     # if demand is low, shrink possible points
    enlarge = 1    # if demand is high, enlarge P function with error (under-enlarge)

    if Condition <1:
      shrink = Condition  #shrink by demand/volume supply
    else:
      enlarge = Condition * (1 + ((samplingPortion / 100.) * len(timeRange)))  #enlarge by demand/volume supply


    while not it.finished:
      if ran.random()< shrink:
        ticks = []
        ind = 0
        for ti in timeRange:
          ticks.append(float(it.multi_index[ind] / float(ti)))
          ind = ind + 1

        y = 0
        for i in range(0, len(timeRange)):
          if i == 0:
              y = self.__expDecay(ticks[i], decay[i])
          else:
              y *= self.__expDecay(ticks[i], decay[i])

        y *= enlarge

        ran1 = ran.random()
        if ran1 < y:
          if it[0] == 0:
            it[0] = 1
            for i in range(0, len(VClists)):
              VClists[i].append(it.multi_index[i] + 1)

      it.iternext()


    sumTimeRange = 0
    counter = 0
    for ti in timeRange:
      if counter == 0:
        sumTimeRange = ti
      else:
        sumTimeRange *= ti

      counter += 1

    #grid is from original scan, we truncate VClist only for over sampling
    while len(VClists[0])> samplingPortion * sumTimeRange / 100.:
      temp = ran.randint(1,len(VClists[0])-1)
      for VClist in VClists:
        del VClist[temp]

    return grid, VClists


def main(args):
  application = QtWidgets.QApplication(args)
  mainWindow = QtWidgets.QMainWindow()
  program = MainWindowView(mainWindow)

  mainWindow.show()

  sys.exit(application.exec_())


if __name__ == '__main__':
  main(sys.argv)

