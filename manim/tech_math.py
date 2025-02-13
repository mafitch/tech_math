from manim import *

class graph_parabola(Scene):
    def construct(self):
        title = Text("Sketching Graphs")
        title.to_edge(UP)
        self.add(title)

        # Construct axes for graph
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=5,
            tips=False,
            axis_config={"include_numbers": True},
        )
        ax.shift(3*RIGHT)
        # Construct table of points
        t0 = IntegerTable(
            [[-2,4],
            [-1,1],
            [0,0],
            [1,1],
            [2,4]],
            col_labels=[
                MathTex("x"),
                MathTex("x^2")],
            h_buff=1)
        t0.shift(3*LEFT)
        t0.scale(0.7)
        self.add(t0)
        self.add(ax)

        origin = ax.c2p(0,0)
        dots = [Dot(origin,radius=0.05,color=GREEN),
            Dot(origin,radius=0.05,color=GREEN),
            Dot(origin,radius=0.05,color=GREEN),
            Dot(origin,radius=0.05,color=GREEN),
            Dot(origin,radius=0.05,color=GREEN)]
        for i in range(5):
            coords = ax.c2p(i-2,(i-2)**2)
            self.add(dots[i])
            hl1=t0.get_highlighted_cell((i+2,1), color=GREEN)
            t0.add_to_back(hl1)
            self.play(ApplyMethod(dots[i].move_to,[coords[0],origin[1],0]))
            self.wait(1)
            hl2=t0.get_highlighted_cell((i+2,2), color=GREEN)
            t0.add_to_back(hl2)
            self.play(ApplyMethod(dots[i].move_to,[coords[0],coords[1],0]))
            self.wait(1)
            t0.remove(*hl1)
            t0.remove(*hl2)

        graph = ax.plot(lambda x: x**2, x_range=[-2,2],color=GREEN)
        self.play(Create(graph))
        self.wait(5)

class period_wavelength(Scene):
    def construct(self):
        def timer_display(mobject,dt):
            mobject.set_value(mobject.get_value()+dt)

        title = Text("Period vs. Wavelength")
        title.to_edge(UP)
        self.add(title)

        # Timer for reading the period
        time = DecimalNumber()
        time.add_updater(timer_display)
        self.add(time)

        # Construct axes for the waves
        axis1 = Axes(
            x_range=[0, 2, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 14},
        )
        axis1.shift(4*LEFT+1.2*UP)
        axis2 = Axes(
            x_range=[0, 2, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 14},
        )
        axis2.shift(4*RIGHT+1.2*UP)
        axis3 = Axes(
            x_range=[0, 2, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 14},
        )
        axis3.shift(4*LEFT+1.7*DOWN)
        axis4 = Axes(
            x_range=[0, 2, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 14},
        )
        axis4.shift(4*RIGHT+1.7*DOWN)

        # add labels
        text1 = Text("Period 1, Wavelength 2",font_size=16).next_to(axis1,DOWN)
        text2 = Text("Period 2, Wavelength 2",font_size=16).next_to(axis2,DOWN)
        text3 = Text("Period 1, Wavelength 1",font_size=16).next_to(axis3,DOWN)
        text4 = Text("Period 2, Wavelength 1",font_size=16).next_to(axis4,DOWN)
        self.add(axis1,axis2,axis3,axis4,text1,text2,text3,text4)

        # create four waves with different periods and wavelengths
        graph1 = axis1.plot(lambda x: np.sin(PI*x), x_range=[0,2],color=GREEN)
        graph2 = axis2.plot(lambda x: np.sin(PI*x), x_range=[0,2],color=GREEN)
        graph3 = axis3.plot(lambda x: np.sin(2*PI*x), x_range=[0,2],color=GREEN)
        graph4 = axis4.plot(lambda x: np.sin(2*PI*x), x_range=[0,2],color=GREEN)
        self.play(Create(graph1,run_time=1),Create(graph2,run_time=2),Create(graph3,run_time=2),Create(graph4,run_time=4))

        self.wait(0.07)
        time.remove_updater(timer_display)

        self.wait(2)
