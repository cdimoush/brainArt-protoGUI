from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Rectangle, Ellipse, Color, Triangle
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

import math
import time


class XMotor(Widget):
    pos = 400, 50
    r = 50
    c = pos[0] + r, pos[1] + r
    theta = 0
    l_pts = [c[0], c[1], c[0] + r, c[1]]
    l = Line()

    def __init__(self, **kwargs):
        super(XMotor, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 1)
            Ellipse(pos=self.pos, size=(100, 100))
            self.add_widget(Label(pos=(400, 125), text='X Stepper'))
        with self.canvas:
            Color(0, 0, 0)
            self.l = Line(points=self.l_pts, width=2)


class YMotor(Widget):
    pos = 400, 250
    r = 50
    c = pos[0] + r, pos[1] + r
    theta = 0
    l_pts = [c[0], c[1], c[0] + r, c[1]]
    l = Line()

    def __init__(self, **kwargs):
        super(YMotor, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 1)
            Ellipse(pos=self.pos, size=(100, 100))
            self.add_widget(Label(pos=(400, 325), text='Y Stepper'))
        with self.canvas:
            Color(0, 0, 0)
            self.l = Line(points=self.l_pts, width=2)


class Pen(Widget):
    pos = 10, 10
    cursor = Ellipse()
    s = 10

    def __init__(self, **kwargs):
        super(Pen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0, 0)
            self.cursor = Ellipse(pos=self.pos, size=(self.s, self.s))


class ArtWork(Widget):
    def draw(self, x, y):
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(x, y), size=(2.5, 2.5))


class GUIWidget(Widget):

    xm = XMotor()
    ym = YMotor()
    p = Pen()
    a = ArtWork()

    get_xy = True
    steps = 0
    speed = .5
    xy = 0, 0
    d_xy = 0, 0
    rad_x = 0
    rad_y = 0
    draw = False

    step_counter = 0

    def __init__(self, **kwargs):
        super(GUIWidget, self).__init__(**kwargs)
        self.add_widget(self.xm)
        self.add_widget(self.ym)
        self.add_widget(self.p)
        self.add_widget(self.a)
        self.add_widget(Label(pos=(400, 450), text='Brain Art Proto GUI', font_size='24sp'))
        with self.canvas.before:
            Line(rectangle=(50, 50, 250, 500))
            self.p.cursor.pos = (50, 50)

    def move_xy(self):
        if self.d_xy[0] != 0:
            dir_x = (self.d_xy[0]) / math.fabs(self.d_xy[0])
        else:
            dir_x = 0

        x = self.p.cursor.pos[0] + self.d_xy[0]/self.steps
        y = self.p.cursor.pos[1] + self.d_xy[1]/self.steps
        self.xm.theta += self.rad_x/self.steps
        xm_x = self.xm.c[0] + self.xm.r * math.cos(self.xm.theta)
        xm_y = self.xm.c[1] + self.xm.r * math.sin(self.xm.theta)
        self.ym.theta += self.rad_y/self.steps
        ym_x = self.ym.c[0] + self.ym.r * math.cos(self.ym.theta)
        ym_y = self.ym.c[1] + self.ym.r * math.sin(self.ym.theta)

        if self.draw:
            self.a.draw(x, y)
        self.p.cursor.pos = (x, y)
        self.xm.l.points = (self.xm.c[0], self.xm.c[1], xm_x, xm_y)
        self.ym.l.points = (self.ym.c[0], self.ym.c[1], ym_x, ym_y)

    def calc_xy(self, x, y, z):

        # ------ Change in XY -------------------
        # set new coordinates and calc difference
        x += 50
        y += 50
        dx = x - self.p.cursor.pos[0]
        dy = y - self.p.cursor.pos[1]

        self.xy = x, y
        self.d_xy = dx, dy

        # -------- Steps -----------------------
        # need maximum step speed, try .5 dist per step
        if math.fabs(dx) > math.fabs(dy):
            self.steps = math.fabs(dx) / self.speed
        else:
            self.steps = math.fabs(dy) / self.speed

        self.step_counter = self.steps

        # ---------- Rotation ------------------
        # cir = pulley circumference = 2 * pi * r
        # theta = rotation angle = (dx / cir) * (2pi)

        self.rad_x = dx / (2 * math.pi * self.xm.r/12)  # need to get radius of physical pulleys, not GUI ellipses!!!
        self.rad_y = dy / (2 * math.pi * self.ym.r/12)

        # ---------- Draw -----------------------
        # Determine if pen should touch paper, binary z variable
        if z == 1:
            self.draw = True
        else:
            self.draw = False

    def read_xy(self):
        f = open('input.txt', 'r+')
        r = str(f.read())
        if r != '':
            self.get_xy = False  # recieved coordinates, switch to pen movement
            x = int(r[r.find('x')+1: r.find('y')])
            y = int(r[r.find('y')+1: r.find('z')])
            z = int(r[r.find('z') + 1])
            f.close()
            open('input.txt', 'w').close()
            self.calc_xy(x, y, z)
        else:
            f.close()
            open('input.txt', 'w').close()

    def update(self, dt):
        if self.get_xy:
            g = open('request.txt', 'w+')
            g.write('request')
            g.close()
            self.read_xy()
        else:
            if self.step_counter > 0:
                self.move_xy()
                self.step_counter -= 1
            else:
                self.get_xy = True


class GUIApp(App):
    def build(self):
        Window.size = (600, 600)
        w = GUIWidget()
        Clock.schedule_interval(w.update, 1.0/60.0)
        return w

if __name__ == '__main__':
    GUIApp().run()