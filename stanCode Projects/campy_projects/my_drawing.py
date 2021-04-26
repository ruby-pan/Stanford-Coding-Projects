"""
File: My_drawing.py
Name: Ruby
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GArc, GRect, GLabel, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    This program creates an image of Chicago Bulls.
    """
    window = GWindow(width=800, height=600, title='CHICAGO BULLS STICKER')

    back = GRect(800, 600)        # background
    back.filled = True
    back.fill_color = 'darkorange'
    back.color = 'darkorange'
    window.add(back)

    cast = GPolygon()       #shine
    cast.add_vertex((0, 00))
    cast.add_vertex((0,170))
    cast.add_vertex((400,300))
    cast.filled = True
    cast.fill_color = 'orange'
    cast.color = 'orange'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((80, 0))
    cast.add_vertex((150,0))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'orange'
    cast.color = 'orange'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((0, 200))
    cast.add_vertex((0,270))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'orange'
    cast.color = 'orange'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((0, 200))
    cast.add_vertex((0,230))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((0, 100))
    cast.add_vertex((0,120))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)

    cast = GPolygon()           # shine
    cast.add_vertex((600, 600))
    cast.add_vertex((800, 600))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'orange'
    cast.color = 'orange'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((800, 400))
    cast.add_vertex((800,550))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'orange'
    cast.color = 'orange'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((580, 600))
    cast.add_vertex((500, 600))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((800, 580))
    cast.add_vertex((800, 600))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((800, 450))
    cast.add_vertex((800, 500))
    cast.add_vertex((400, 300))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)

    # palm
    back1 = GOval(150, 150, x=370, y=500)
    back1.filled = True
    back1.fill_color = 'chocolate'
    window.add(back1)

    #other fingers
    cast = GPolygon()
    cast.add_vertex((270, 520))
    cast.add_vertex((350,605))
    cast.add_vertex((275,600))
    cast.filled = True
    cast.fill_color = 'peru'
    cast.color = 'peru'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((270, 520))
    cast.add_vertex((380,470))
    cast.add_vertex((275,600))
    cast.filled = True
    cast.fill_color = 'peru'
    cast.color = 'peru'
    window.add(cast)
    back1 = GOval(70, 70, x=320, y=538)
    back1.filled = True
    back1.fill_color = 'peru'
    back1.color = 'peru'
    window.add(back1)
    back1 = GOval(35, 50, x=345, y=550)
    back1.filled = True
    back1.fill_color = 'peachpuff'
    back1.color = 'peachpuff'
    window.add(back1)
    back1 = GOval(35, 50, x=340, y=550)
    back1.filled = True
    back1.fill_color = 'darksalmon'
    back1.color = 'darksalmon'
    window.add(back1)

    cast = GPolygon()
    cast.add_vertex((290, 470))
    cast.add_vertex((350,470))
    cast.add_vertex((280,570))
    cast.filled = True
    cast.fill_color = 'sandybrown'
    cast.color = 'sandybrown'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((350, 575))
    cast.add_vertex((350,470))
    cast.add_vertex((280,570))
    cast.filled = True
    cast.fill_color = 'sandybrown'
    cast.color = 'sandybrown'
    window.add(cast)
    back1 = GOval(70, 70, x=330, y=508)
    back1.filled = True
    back1.fill_color = 'sandybrown'
    back1.color =  'sandybrown'
    window.add(back1)
    back1 = GOval(35, 40, x=355, y=533)
    back1.filled = True
    back1.fill_color = 'peachpuff'
    back1.color = 'peachpuff'
    window.add(back1)
    back1 = GOval(35, 40, x=350, y=533)
    back1.filled = True
    back1.fill_color = 'darksalmon'
    back1.color = 'darksalmon'
    window.add(back1)

    cast = GPolygon()
    cast.add_vertex((330, 400))
    cast.add_vertex((390,550))
    cast.add_vertex((300,530))
    cast.filled = True
    cast.fill_color = 'darksalmon'
    cast.color = 'darksalmon'
    window.add(cast)
    back1 = GOval(70, 70, x=360, y=480)
    back1.filled = True
    back1.fill_color = 'darksalmon'
    back1.color = 'darksalmon'
    window.add(back1)
    back1 = GOval(35, 40, x=382, y=502)
    back1.filled = True
    back1.fill_color = 'peachpuff'
    back1.color = 'peachpuff'
    window.add(back1)
    back1 = GOval(35, 40, x=377, y=502)
    back1.filled = True
    back1.fill_color = 'lightcoral'
    back1.color = 'lightcoral'
    window.add(back1)

    back = GRect(340, 80, x=235, y=50)        # backshadows
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    back = GRect(300, 150, x=245, y=110)
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    back1 = GOval(80, 80, x=200, y=50)
    back1.filled = True
    back1.fill_color = 'black'
    window.add(back1)
    back2 = GOval(80, 80, x=530, y=50)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back = GRect(40, 110, x=220, y=110)
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    back = GRect(40, 110, x=530, y=110)
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    cast4 = GPolygon()
    cast4.add_vertex((220, 100))
    cast4.add_vertex((220, 180))
    cast4.add_vertex((205, 180))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast4 = GPolygon()
    cast4.add_vertex((200, 255))
    cast4.add_vertex((220, 180))
    cast4.add_vertex((205, 180))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast4 = GPolygon()
    cast4.add_vertex((200, 255))
    cast4.add_vertex((220, 180))
    cast4.add_vertex((245, 260))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast4 = GPolygon()
    cast4.add_vertex((570, 100))
    cast4.add_vertex((570,180))
    cast4.add_vertex((585,180))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast4 = GPolygon()
    cast4.add_vertex((590, 255))
    cast4.add_vertex((570, 180))
    cast4.add_vertex((585, 180))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast4 = GPolygon()
    cast4.add_vertex((590, 255))
    cast4.add_vertex((570, 180))
    cast4.add_vertex((545, 260))
    cast4.filled = True
    cast4.fill_color = 'black'
    cast4.color = 'black'
    window.add(cast4)
    cast = GPolygon()           # backshadows
    cast.add_vertex((205, 230))
    cast.add_vertex((390,490))
    cast.add_vertex((575,230))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    back1 = GOval(160, 130, x=310, y=350)
    back1.filled = True
    back1.fill_color = 'black'
    window.add(back1)
    cast = GPolygon()           # ear shadows
    cast.add_vertex((250, 250))
    cast.add_vertex((390,350))
    cast.add_vertex((210,280))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((530, 250))
    cast.add_vertex((390,350))
    cast.add_vertex((580,280))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)

    word3 = GLabel('CHICAGO')        # words
    word3.font = 'Courier-70-bold'
    word3.color = 'white'
    window.add(word3, 205, 145)
    word4 = GLabel('BULLS')
    word4.font = 'Courier-70-bold'
    word4.color = 'white'
    window.add(word4, 260, 210)

    horn = GRect(120, 45, x=240, y=210)       # horns
    horn.filled = True
    horn.fill_color = 'white'
    horn.color = 'white'
    window.add(horn)
    horn = GRect(120, 45, x=430, y=210)
    horn.filled = True
    horn.fill_color = 'white'
    horn.color = 'white'
    window.add(horn)
    cast = GPolygon()
    cast.add_vertex((540, 210))        #right horn
    cast.add_vertex((560,180))
    cast.add_vertex((580,250))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)
    cast3 = GPolygon()
    cast3.add_vertex((580, 250))
    cast3.add_vertex((560,180))
    cast3.add_vertex((575,180))
    cast3.filled = True
    cast3.fill_color = 'white'
    cast3.color = 'white'
    window.add(cast3)
    cast3 = GPolygon()
    cast3.add_vertex((540, 210))
    cast3.add_vertex((580,250))
    cast3.add_vertex((550,255))
    cast3.filled = True
    cast3.fill_color = 'white'
    cast3.color = 'white'
    window.add(cast3)
    cast = GPolygon()
    cast4 = GPolygon()
    cast4.add_vertex((560, 130))
    cast4.add_vertex((560,180))
    cast4.add_vertex((575,180))
    cast4.filled = True
    cast4.fill_color = 'firebrick'
    cast4.color = 'black'
    window.add(cast4)
    cast.add_vertex((250, 210))        # left horn
    cast.add_vertex((230,180))
    cast.add_vertex((210,250))
    cast.filled = True
    cast.fill_color = 'white'
    cast.color = 'white'
    window.add(cast)
    cast3 = GPolygon()
    cast3.add_vertex((210, 250))
    cast3.add_vertex((230,180))
    cast3.add_vertex((215,180))
    cast3.filled = True
    cast3.fill_color = 'white'
    cast3.color = 'white'
    window.add(cast3)
    cast3 = GPolygon()
    cast3.add_vertex((250, 210))
    cast3.add_vertex((210,250))
    cast3.add_vertex((240,255))
    cast3.filled = True
    cast3.fill_color = 'white'
    cast3.color = 'white'
    window.add(cast3)
    cast4 = GPolygon()
    cast4.add_vertex((230, 130))
    cast4.add_vertex((230, 180))
    cast4.add_vertex((215, 180))
    cast4.filled = True
    cast4.fill_color = 'firebrick'
    cast4.color = 'black'
    window.add(cast4)

    face2 = GRect(155, 90, x=315, y=210)       # bullheads
    face2.filled = True
    face2.fill_color = 'firebrick'
    face2.color = 'firebrick'
    window.add(face2)
    cast = GPolygon()
    cast.add_vertex((280, 270))
    cast.add_vertex((390,470))
    cast.add_vertex((500,270))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    back1 = GOval(140, 80, x=320, y=380)
    back1.filled = True
    back1.fill_color = 'black'
    window.add(back1)
    back1 = GOval(140, 80, x=320, y=383)
    back1.filled = True
    back1.fill_color = 'firebrick'
    window.add(back1)
    face2 = GRect(95, 55, x=342, y=395)
    face2.filled = True
    face2.fill_color = 'firebrick'
    face2.color = 'firebrick'
    window.add(face2)

    cast = GPolygon()               # forehead
    cast.add_vertex((315, 210))
    cast.add_vertex((340,290))
    cast.add_vertex((300,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((470, 210))
    cast.add_vertex((450,290))
    cast.add_vertex((485,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)

    cast = GPolygon()               # ears
    cast.add_vertex((460, 250))
    cast.add_vertex((480,290))
    cast.add_vertex((550,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((320, 250))
    cast.add_vertex((330,290))
    cast.add_vertex((240,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((280, 280))
    cast.add_vertex((280,295))
    cast.add_vertex((240,280))
    cast.filled = True
    cast.fill_color ='firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((280, 280))
    cast.add_vertex((280,295))
    cast.add_vertex((300,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()               # ears
    cast.add_vertex((510, 280))
    cast.add_vertex((510,295))
    cast.add_vertex((550,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)
    cast = GPolygon()               # ears
    cast.add_vertex((510, 280))
    cast.add_vertex((510,295))
    cast.add_vertex((470,280))
    cast.filled = True
    cast.fill_color = 'firebrick'
    cast.color = 'firebrick'
    window.add(cast)

    cast = GPolygon()
    cast.add_vertex((375, 451))     # chin shadow
    cast.add_vertex((390,475))
    cast.add_vertex((405,451))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)

    line = GLine(315, 210, 305, 258)        #horn lines
    line.color = 'black'
    window.add(line)
    line = GLine(316, 210, 306, 258)
    line.color = 'black'
    window.add(line)
    line = GLine(470, 210, 480, 258)
    line.color = 'black'
    window.add(line)
    line = GLine(469, 210, 479, 258)
    line.color = 'black'
    window.add(line)

    back2 = GOval(35, 30, x=310, y=310)     # left eye bags
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(35, 30, x=310, y=307)
    back2.filled = True
    back2.fill_color = 'firebrick'
    window.add(back2)
    back2 = GOval(45, 30, x=300, y=295)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(45, 30, x=300, y=290)
    back2.filled = True
    back2.fill_color = 'firebrick'
    back2.color = 'firebrick'
    window.add(back2)

    back2 = GOval(30, 30, x=440, y=310)     # right eye bags
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(30, 30, x=440, y=307)
    back2.filled = True
    back2.fill_color = 'firebrick'
    window.add(back2)
    back2 = GOval(40, 30, x=440, y=295)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(40, 30, x=440, y=290)
    back2.filled = True
    back2.fill_color = 'firebrick'
    back2.color = 'firebrick'
    window.add(back2)

    back2 = GOval(40, 40, x=300, y=270)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(35, 35, x=305, y=270)  #left eye
    back2.filled = True
    back2.fill_color = 'white'
    window.add(back2)
    back2 = GOval(25, 25, x=310, y=275)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)

    back2 = GOval(40, 40, x=440, y=270)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(35, 35, x=440, y=270)  #right eye
    back2.filled = True
    back2.fill_color = 'white'
    window.add(back2)
    back2 = GOval(25, 25, x=445, y=275)
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)

    back2 = GOval(40, 40, x=425, y=255)     #eye covers
    back2.filled = True
    back2.fill_color = 'firebrick'
    back2.color = 'firebrick'
    window.add(back2)
    back2 = GOval(40, 40, x=320, y=255)
    back2.filled = True
    back2.fill_color = 'firebrick'
    back2.color = 'firebrick'
    window.add(back2)

    back2 = GOval(80, 100, x=353, y=270)    # nose fold
    back2.filled = True
    back2.fill_color = 'black'
    window.add(back2)
    back2 = GOval(80, 100, x=353, y=265)
    back2.filled = True
    back2.fill_color = 'firebrick'
    back2.color = 'firebrick'
    window.add(back2)
    line = GLine(350, 360, 340, 290)    # left nose line
    line.color = 'black'
    window.add(line)
    line = GLine(350, 360, 341, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 360, 342, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(351, 360, 343, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 360, 340, 390)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 360, 341, 390)
    line.color = 'black'
    window.add(line)
    line = GLine(351, 360, 342, 390)
    line.color = 'black'
    window.add(line)

    line = GLine(435, 360, 445, 290)    # right nose line
    line.color = 'black'
    window.add(line)
    line = GLine(435, 360, 444, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(435, 360, 443, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(434, 360, 442, 290)
    line.color = 'black'
    window.add(line)
    line = GLine(435, 360, 440, 390)
    line.color = 'black'
    window.add(line)
    line = GLine(435, 360, 439, 390)
    line.color = 'black'
    window.add(line)
    line = GLine(435, 360, 438, 390)
    line.color = 'black'
    window.add(line)
    line = GLine(434, 360, 437, 390)
    line.color = 'black'
    window.add(line)

    back = GRect(20, 15, x=300, y=268)    # left brows
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    cast = GPolygon()
    cast.add_vertex((300, 280))
    cast.add_vertex((320,268))
    cast.add_vertex((365,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((395, 280))
    cast.add_vertex((380,312))
    cast.add_vertex((365,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((395, 280))
    cast.add_vertex((355,300))
    cast.add_vertex((365,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((380, 300))
    cast.add_vertex((320,270))
    cast.add_vertex((365,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)

    back = GRect(20, 15, x=460, y=268)    #right brows
    back.filled = True
    back.fill_color = 'black'
    window.add(back)
    cast = GPolygon()
    cast.add_vertex((480, 280))
    cast.add_vertex((460,268))
    cast.add_vertex((420,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((395, 280))
    cast.add_vertex((405,312))
    cast.add_vertex((420,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((395, 280))
    cast.add_vertex((430,300))
    cast.add_vertex((420,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((410, 300))
    cast.add_vertex((460,270))
    cast.add_vertex((420,310))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)

    line = GLine(350, 240, 440, 240)        #forehead expressions
    line.color = 'black'
    window.add(line)
    line = GLine(350, 241, 440, 241)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 255, 440, 255)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 256, 440, 256)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 270, 440, 270)
    line.color = 'black'
    window.add(line)
    line = GLine(350, 271, 440, 271)
    line.color = 'black'
    window.add(line)
    line = GLine(395, 280, 395, 230)
    line.color = 'black'
    window.add(line)
    line = GLine(396, 280, 396, 230)
    line.color = 'black'
    window.add(line)

    back1 = GOval(27, 20, x=358, y=400)          # nose
    back1.filled = True
    back1.fill_color = 'black'
    window.add(back1)
    back1 = GOval(27, 20, x=398, y=400)
    back1.filled = True
    back1.fill_color = 'black'
    window.add(back1)
    cast = GPolygon()
    cast.add_vertex((340, 400))
    cast.add_vertex((340,460))
    cast.add_vertex((350,460))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((440, 400))
    cast.add_vertex((440,460))
    cast.add_vertex((430,460))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)

    cast = GPolygon()    # chin shadows
    cast.add_vertex((440, 395))
    cast.add_vertex((440,460))
    cast.add_vertex((480,400))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((340, 395))
    cast.add_vertex((340,460))
    cast.add_vertex((300,400))
    cast.filled = True
    cast.fill_color = 'black'
    cast.color = 'black'
    window.add(cast)
    rec = GRect(100, 20, x=340, y=450)
    rec.filled = True
    rec.fill_color = 'black'
    window.add(rec)

    back1 = GOval(310, 300, x=460, y=500)          # thumb
    back1.filled = True
    back1.fill_color = 'lightsalmon'
    back1.color = 'lightsalmon'
    window.add(back1)
    cast = GPolygon()
    cast.add_vertex((560, 560))
    cast.add_vertex((670,510))
    cast.add_vertex((520,445))
    cast.filled = True
    cast.fill_color = 'lightsalmon'
    cast.color = 'lightsalmon'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((370, 430))
    cast.add_vertex((520,445))
    cast.add_vertex((360,510))
    cast.filled = True
    cast.fill_color = 'lightsalmon'
    cast.color = 'lightsalmon'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((360, 510))
    cast.add_vertex((520,445))
    cast.add_vertex((560,550))
    cast.filled = True
    cast.fill_color = 'lightsalmon'
    cast.color = 'lightsalmon'
    window.add(cast)
    back1=GOval(80, 85, x=340, y=430)
    back1.filled = True
    back1.fill_color = 'lightsalmon'
    back1.color = 'lightsalmon'
    window.add(back1)
    back1=GOval(50, 50, x=358, y=430)       # nail
    back1.filled = True
    back1.fill_color = 'peachpuff'
    back1.color = 'darksalmon'
    window.add(back1)
    back1=GOval(51, 51, x=366, y=431)
    back1.filled = True
    back1.fill_color = 'lightcoral'
    back1.color = 'darksalmon'
    window.add(back1)
    cast = GPolygon()
    cast.add_vertex((415,485))
    cast.add_vertex((400,432))
    cast.add_vertex((425,435))
    cast.filled = True
    cast.fill_color = 'lightcoral'
    cast.color = 'lightcoral'
    window.add(cast)
    cast = GPolygon()
    cast.add_vertex((415,485))
    cast.add_vertex((400,432))
    cast.add_vertex((390,483))
    cast.filled = True
    cast.fill_color = 'lightcoral'
    cast.color = 'lightcoral'
    window.add(cast)

if __name__ == '__main__':
    main()
