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
        commands = [line.rstrip('\n') for line in command]
    x = 0;
    while (x < len(commands)):
        
        if (commands[x] == "line"):
            coordinates = commands[x+1].split(" ")
            add_edge(points, int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3]),int(coordinates[4]),int(coordinates[5]))
            x += 2
          
            
        elif (commands[x] == "ident"):
            ident(transform)
            x+=1
           
            
        elif (commands[x] == "scale"):
            scale = commands[x+1].split(" ")
            change = make_scale(float(scale[0]), float(scale[1]), float(scale[2]))
            matrix_mult(change,transform)
            x+=2
        
        
        elif (commands[x] == "move"):
            move = commands[x+1].split(" ")
            moves =make_translate(move[0], move[1], move[2])
            matrix_mult(moves,transform)
            x+=2
           
            
        elif (commands[x] == "rotate"):
            rotation = commands[x+1].split(" ")
            if (rotation[0] == "x"):
                degree = make_rotX(int(rotation[1]))
            elif (rotation[0] == "y"):
                degree = make_rotY(int(rotation[1]))
            else:
                degree = make_rotZ(int(rotation[1]))
            matrix_mult(degree,transform)
            x+=2
           
        elif (commands[x] == "apply"):
            matrix_mult(transform, points)
            x+=1
    
        elif (commands[x] == "display"):
            for r in range(len(points)):
                for c in range(4):
                    points[r][c] = int(points[r][c])
            clear_screen(screen)
            draw_lines(points,screen,color)
          
            x+=1
            
            
        elif (commands[x] == "save"):
            coordinates = commands[x+1].split(" ")
            save_extension(screen, coordinates[0])
            x+=1
            
            
        elif (commands[x] == "end"):
            break
    
        else:
            x+=1
            

    print "done"
