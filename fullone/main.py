import pygame
import random
import time
##import keyboard
import tkinter
##import PySimpleGUI as sg
import webbrowser

global HP
global money
global money_win
global event
global solution
global R

from choisesmain import choisemain
from time import sleep
from slots import slots
from BCC import Poker
from Ruleta import Ruleta
from enemies import enemies
from gamesR import gameR
from RR import russia_roulette

choisemain()
money = 1000
if solution == 1:
    gameR()
elif solution == 2:
     file_path = 'Rules.html'
     webbrowser.open(file_path)


