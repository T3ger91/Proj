#main structure and also main file with all logic to start game, single games, random gen off rooms, choises in menu and ...
import pygame
import random
import time
import keyboard
import tkinter
import PySimpleGUI as sg
import webbrowser
from slow_print import slow_print

global HP
global money
global money_win
global event
global solution
global R
global budget
from MenuS import Menu
budget = 1000
slow_print(f"1000 this is ur money now\nto escape this asshole place u need to gain 100.000 dinars")

Menu()





