from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib import pyplot as plt
import sys
import cv2
import os

import time
from io import StringIO

# Custom modules
import classes.core_mods as core
import classes.file as file
import classes.jpeg as jpeg

# Configuration files
import config.app

class WorkerSignals(QObject):
    ''' Defines the signals available from a running worker thread.
    class Worker(QRunnable):
    
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    update_console = pyqtSignal()

class ConsoleUpdater(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(ConsoleUpdater, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        print('Thread Initialized')
        while(1):
            time.sleep(config.app.CONSOLE_UPDATE_DELAY)
            self.signals.update_console.emit()
        # self.fn(*self.args, **self.kwargs)