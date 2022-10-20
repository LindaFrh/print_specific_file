from doctest import OutputChecker
from zoneinfo import available_timezones
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os, sys
import subprocess
import tempfile
import win32api
import win32con
import win32print
import win32ui

class printFolder(App):
    def build(self):
        #returns a window object with all it's wodgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        #label widget
        self.greeting = Label(
                            text = "Print files in my folder",
                            font_size = 18,
                            color = '#00FFCE'
                                )
        self.window.add_widget(self.greeting)

        #text input widget
        self.user = TextInput(
                    multiline = False,
                    size_hint = (1,0.5),
                    padding_y = (20,20)
                    )
        self.window.add_widget(self.user)
        
        #button widget
        self.button = Button(
                            text = "Print!",
                            size_hint = (1,0.5),
                            bold = True,
                            background_color = '#00FFCE',
                                )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self,instance):
        file1 = self.user.text
        try:
            printer_name = win32print.GetDefaultPrinter ()
            print(printer_name)
            hPrinter = win32print.OpenPrinter (printer_name)
            hDC = win32ui.CreateDC ()
            hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
            hDC.StartDoc (file1)
            hDC.StartPage ()
            hDC.SetMapMode (win32con.MM_TWIPS)
            hDC.DrawText ("TEST", (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
            hDC.EndPage ()
            hDC.EndDoc ()
            #os.startfile(file1, 'open')
            win32api.ShellExecute (
                    0,
                    "printto",
                    file1,
                    'AnyDesk Printer'
                    ".",
                    0
                )
        except:
            print(f"file {file1} cannot be printed")
        
if __name__ == "__main__":
    printFolder().run()

