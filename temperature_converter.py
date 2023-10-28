# This program is to help you to convert temperature

# Importing modules
import tkinter
import tkinter.messagebox as box 

# Defining Class
class FahrenConverterGUI:
    # Defining function
    def __init__(self):
      # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #Create widgets for the bottom frame
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        
        #Pack the bottom frame's widgets
        self.quit_button.pack(side='left')
      
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        
temp_converter = FahrenConverterGUI()