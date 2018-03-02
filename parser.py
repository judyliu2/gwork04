from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    commands = []
    f = open(fname,"rw+")
    with open (fname) as command:
        commands = [line.strip() for line in command]

    x = 0;
    while (x < length(commmands)):
        
        if (commands[x] == "line"):
            coordinates = commands[x+1].split()
            add_edge(point, int(commands[0]), int(commands[1]),int(commands[2]),int(commands[3]),int(commands[4]),int(commands[5]))
            x += 2
            
        if (commands[x] == "ident"):
            ident(transform)
            x++
            
        if (commands[x] == "scale"):
            scale = commands[x+1].split()
            make_scale(scale[0], scale[1], scale[2])
            x+=2
            
        if (commands[x] == "move"):
            move = commands[x+1].split()
            make_translate(move[0], move[1], move[2])
            x+=2
            
        if (commands[x] == "rotate"):
            rotation = commands[x+1].split()
            if (rotation[0] == "x"):
                 make_rotx(rotation[1])
            if (rotation[1] == "y"):
                make_roty(rotation[1])
            if (rotation[2] == "z"):
                make_rotz(rotation[1])
            x+=2
            
        if (commands[x] == "apply"):
            matrix_multiply(transform, points)
            x++
            
        if (commands[x] == "display"):
            display(screen)
            x++
            
        if (commands[x] == "save"):
            save_extension(screen, fname)
            x++
            
        if (commands[x] == "quit"):
            break
