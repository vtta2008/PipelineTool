# -*- coding: utf-8 -*-
"""

Script Name: Task.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

from bin.data.damg                       import DAMGLIST, DAMGTHREADPOOL, DAMGTIMER, DAMGTHREAD
from utils                               import get_ram_useage, get_cpu_useage, create_signal_slot

signal_cpu, slot_cpu = create_signal_slot(argType=str, name='CPU')
signal_ram, slot_ram = create_signal_slot(argType=str, name='RAM')

class BackgroundService(DAMGTHREAD):

    key = 'FooterWorker'
    cpu = signal_cpu
    ram = signal_ram

    slotCpu = slot_cpu
    slotRam = slot_ram

    def __init__(self, name='CPU useage', *args, **kwargs):
        super(BackgroundService, self).__init__(self)

        self.args = args
        self.kwargs = kwargs
        self._name = name

    def run(self):
        while True:
            cpu = str(get_cpu_useage())
            ram = str(get_ram_useage())
            self.cpu.emit(cpu)
            self.ram.emit(ram)

class Counting(DAMGTIMER):

    key = 'Counting'
    printCounter = False
    _isCounting = False
    _counter = 0

    def __init__(self, countLimited=0, interval=10000):
        super(Counting, self).__init__()

        self._interval = interval
        self._countLimited = countLimited
        self.setInterval(self._interval)

    def begin(self):
        if self.printCounter:
            print("Start counting")
        # self.timeout.connect(self.start_thread)
        self.timeout.connect(self.counting)
        self.start(1000)
        self._isCounting = True

    def counting(self):
        if self._counter == 0:
            self._counter += 1
        elif self._counter == self._countLimited:
            self.finish()
        else:
            self._counter += 1

        if self.printCounter:
            print(self._counter)

    def finish(self):
        if self.printCounter:
            print("Stop counting")
        self.stop()
        self._isCounting = False

    def setStartCounter(self, val):
        self._counter = val
        return self._counter

    def setCountLimited(self, val):
        if not self._countLimited == val:
            if self.printCounter:
                print('countLimited is set to: {0}'.format(val))
            self._countLimited = val

        return self._countLimited

    def setPrintCounter(self, bool):
        if bool:
            if not self.printCounter:
                self.printCounter = bool
        else:
            if self.printCounter:
                print('printCounter is set to: {0}'.format(bool))
                self.printCounter = bool
            else:
                print('printCounter is set to: {0}'.format(bool))

        return self.printCounter

    @property
    def counter(self):
        return self._counter

    @property
    def countLimited(self):
        return self._countLimited

    @property
    def isCounting(self):
        return self._isCounting

    @counter.setter
    def counter(self, val):
        self._counter = val

    @countLimited.setter
    def countLimited(self, val):
        self._countLimited = val

    @isCounting.setter
    def isCounting(self, val):
        self._isCounting = val

class ThreadManager(DAMGTHREADPOOL):

    tasks = DAMGLIST()

    def __init__(self):
        super(ThreadManager, self).__init__()

        self.counter                = Counting()

    def startCounting(self):
        self.counter.begin()

    def stopCounting(self):
        self.counter.finish()

    def serviceThread(self):
        thread = BackgroundService()
        self.threads.append(thread)
        return thread

    def setCountLimited(self, val):
        return self.counter.setCountLimited(val)

    def setPrintCounter(self, bool):
        return self.counter.setPrintCounter(bool)

    def isCounting(self):
        return self.counter.isCounting

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 20/10/2019 - 6:23 PM
# © 2017 - 2018 DAMGteam. All rights reserved