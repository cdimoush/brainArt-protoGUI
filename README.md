# brainArt-protoGUI

The protoGUI is an attempt to simmulate the Brain Art Drawing Machine and preview the art generated.
The code the repository can be broken into two sections. A) GUIs B) Art Generators / Dependencies


---------------------------------------------------------------------------------------------------------

GUIs:

  -main.py: a kivy program that simmulates pen carriage movement and stepper motor rotation. Since Kivy only works on python 3.4 it probably won't be used by anyone. IMPORTANT: The calc_coordinates function can be used for the arduino code.
  
  -art_preview.py: a tkinter program that displays the art. Tkinter > Kivy.
  
  Both programs load numpy arrays that act as gcode. The format of the arrays is ([[x1, y1, z1], [x2, y2, z2], ...])
  

----------------------------------------------------------------------------------------------------------


Art Generator:

  -art_generator.py: spit out one huge numpy array for the drawing machine use. How is it going to do it I don't know yet. Lots of imported functions
  
  
  
