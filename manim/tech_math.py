from manim import *

class SimilarTriangles(Scene):
    def construct(self):
        title = Text("Identifying Similar Triangles")
        title.to_edge(UP)
        self.add(title)

        # Label the vertices
        vertices1_labels = ["A", "B", "C"]
        vertices2_labels = ["D", "E", "F"]

        # Define the vertices of the triangle
        triangle1_vertices = [
            [0,0,0],
            [0.8992052389, 0.8096480336, 0],
            [1,0,0]
        ]
        triangle2_vertices = triangle1_vertices

        # construct the first triangle
        triangle1 = Polygon(*triangle1_vertices, color=BLUE)
        triangle1.rotate(PI/3,about_point=([1/2,2/5,0]))
        triangle1.scale(3)
        triangle1_vertices = triangle1.get_vertices()
        vertex_labels1 = VGroup()
        for i, vertex in enumerate(triangle1_vertices):
            label = Tex(vertices1_labels[i]).next_to(vertex,triangle1_vertices[i]/3)
            vertex_labels1.add(label)
        triangle1.move_to([-4,0,0])
        vertex_labels1.move_to([-4,0,0])
        triangle1_vertices = triangle1.get_vertices()

        # Construct the second triangle (scaled up version of 1st)
        triangle2 = Polygon(*triangle2_vertices, color=GREEN)
        triangle2.rotate(-3*PI/8,about_point=([3/4,3/5,0]))
        triangle2.scale(3.9)
        triangle2_vertices = triangle2.get_vertices()
        vertex_labels2 = VGroup()
        for i, vertex in enumerate(triangle2_vertices):
            label = Tex(vertices2_labels[i]).next_to(vertex, triangle2_vertices[i]/3.9 )
            vertex_labels2.add(label)
        triangle2_vertices = triangle2.get_vertices()
        triangle2.move_to([4,0,0])
        vertex_labels2.move_to([4,0,0])
        triangle2_vertices = triangle2.get_vertices()

        # Display the triangles
        self.add(triangle1,triangle2,vertex_labels1,vertex_labels2)

        # Label the angles
        angle_labels1 = VGroup()
        angle_labels2 = VGroup()

        angles1 = [
            Angle.from_three_points(triangle1_vertices[2], triangle1_vertices[0], triangle1_vertices[1], radius=0.5, color=RED),
            Angle.from_three_points(triangle1_vertices[0], triangle1_vertices[1], triangle1_vertices[2], radius=0.5, color=RED),
            Angle.from_three_points(triangle1_vertices[1], triangle1_vertices[2], triangle1_vertices[0], radius=0.5, color=RED)
        ]

        angles2 = [
            Angle.from_three_points(triangle2_vertices[2], triangle2_vertices[0], triangle2_vertices[1], radius=0.5, color=RED),
            Angle.from_three_points(triangle2_vertices[0], triangle2_vertices[1], triangle2_vertices[2], radius=0.5, color=RED),
            Angle.from_three_points(triangle2_vertices[1], triangle2_vertices[2], triangle2_vertices[0], radius=0.5, color=RED)
        ]

        angle_labels1_tex = ["$42^\circ$", "$55^\circ$", "$83^\circ$"]
        angle_labels2_tex = angle_labels1_tex

        for i, angle in enumerate(angles1):
            pt0 = np.array(triangle1_vertices[i])
            pt1 = np.array(angle.point_from_proportion(0.5))
            pt2 = pt0+(pt1-pt0)*1.4
            label = Tex(angle_labels1_tex[i],font_size=32).move_to(pt2)
            angle_labels1.add(label)

        for i, angle in enumerate(angles2):
            pt0 = np.array(triangle2_vertices[i])
            pt1 = np.array(angle.point_from_proportion(0.5))
            pt2 = pt0+(pt1-pt0)*1.4
            label = Tex(angle_labels2_tex[i],font_size=32).move_to(pt2)
            angle_labels2.add(label)

        self.add(VGroup(*angles1),VGroup(*angles2),angle_labels1,angle_labels2)

        # construct sides for highlight and label the side lengths
        side_labels1 = VGroup()
        side_labels2 = VGroup()

        side_labels1_tex = ["82", "100", "121"]
        side_labels2_tex = ["106", "130", "157"]

        sides1 = [
            Line(triangle1_vertices[1],triangle1_vertices[2],stroke_color="WHITE",stroke_width="6"),
            Line(triangle1_vertices[2],triangle1_vertices[0],stroke_color="WHITE",stroke_width="6"),
            Line(triangle1_vertices[0],triangle1_vertices[1],stroke_color="WHITE",stroke_width="6")
        ]
        sides2 = [
            Line(triangle2_vertices[1],triangle2_vertices[2],stroke_color="WHITE",stroke_width="6"),
            Line(triangle2_vertices[2],triangle2_vertices[0],stroke_color="WHITE",stroke_width="6"),
            Line(triangle2_vertices[0],triangle2_vertices[1],stroke_color="WHITE",stroke_width="6")
        ]
        for i, seg in enumerate(sides1):
            pt0 = np.array(seg.point_from_proportion(0.5))
            mt = sides1[i].get_slope()
            mv = -1/mt
            sgn1 = -(triangle1_vertices[i][1]-triangle1_vertices[(i+1)%3][1])+mt*(triangle1_vertices[i][0]-triangle1_vertices[(i+1)%3][0])
            sgn1 = sgn1/abs(sgn1)
            pt2 = pt0+np.array([1,mv,0])/(np.sqrt(1+mv**2)*4)
            sgn2 = -(pt2[1]-triangle1_vertices[(i+1)%3][1])+mt*(pt2[0]-triangle1_vertices[(i+1)%3][0])
            sgn2 = sgn2/abs(sgn2)
            if sgn1 == sgn2:
                pt2 = pt0-np.array([1,mv,0])/(np.sqrt(1+mv**2)*4)
            alpha = sides1[i].get_angle()
            if alpha > PI/2:
                alpha = alpha - PI
            elif alpha < -PI/2:
                alpha = alpha + PI
            lable = Tex(side_labels1_tex[i],font_size=32).move_to(pt2).rotate(alpha,about_point=pt2)
            side_labels1.add(lable)

        for i, seg in enumerate(sides2):
            pt0 = np.array(seg.point_from_proportion(0.5))
            mt = sides2[i].get_slope()
            mv = -1/mt
            sgn1 = -(triangle2_vertices[i][1]-triangle2_vertices[(i+1)%3][1])+mt*(triangle2_vertices[i][0]-triangle2_vertices[(i+1)%3][0])
            sgn1 = sgn1/abs(sgn1)
            pt2 = pt0+np.array([1,mv,0])/(np.sqrt(1+mv**2)*4)
            sgn2 = -(pt2[1]-triangle2_vertices[(i+1)%3][1])+mt*(pt2[0]-triangle2_vertices[(i+1)%3][0])
            sgn2 = sgn2/abs(sgn2)
            if sgn1 == sgn2:
                pt2 = pt0-np.array([1,mv,0])/(np.sqrt(1+mv**2)*4)
            alpha = sides2[i].get_angle()
            if alpha > PI/2:
                alpha = alpha - PI
            elif alpha < -PI/2:
                alpha = alpha + PI
            lable = Tex(side_labels2_tex[i],font_size=32).move_to(pt2).rotate(alpha,about_point=pt2)
            side_labels2.add(lable)

        self.add(side_labels1,side_labels2)
        text0 = Tex("Consider these triangles.")
        text0.to_edge(DOWN)
        self.play(FadeIn(text0))
        self.wait(4)
        self.play(FadeOut(text0))
#        self.remove(text0)

        # Highlight first corresponding pair
        text1 = Tex("Both triangles have an angle of $42^\\circ$")
        text1.to_edge(DOWN)
        self.play(FadeIn(text1))
        self.wait(2)
        self.remove(text1)
        text1b = Tex("These are across from sides of length 82 and 106")
        text1b.to_edge(DOWN)
        self.play(FadeIn(text1b))
        self.add(sides1[0],sides2[0])
        self.wait(1)
        ratio_txt1 = MathTex("{106","\\over","82}","\\approx 1.3")
        ratio_txt1.move_to([0,1,0])
        self.play(FadeIn(ratio_txt1))
        self.wait(2)
        self.play(FadeOut(text1b))
        # Highlight second corresponding pair
        text1 = Tex("Both triangles have an angle of $55^\\circ$")
        text1.to_edge(DOWN)
        self.play(FadeIn(text1))
        self.wait(2)
        self.remove(text1)
        text1b = Tex("These are across from sides of length 100 and 130")
        text1b.to_edge(DOWN)
        self.play(FadeIn(text1b))
        self.add(sides1[0],sides2[0])
        self.wait(1)
        ratio_txt2 = MathTex("{130","\\over","100}","\\approx 1.3")
        ratio_txt2.next_to(ratio_txt1,DOWN)
        self.play(FadeIn(ratio_txt2))
        self.wait(2)
        self.play(FadeOut(text1b))
        # Highlight third corresponding pair
        text1 = Tex("Both triangles have an angle of $83^\\circ$")
        text1.to_edge(DOWN)
        self.play(FadeIn(text1))
        self.wait(2)
        self.remove(text1)
        text1b = Tex("These are across from sides of length 121 and 157")
        text1b.to_edge(DOWN)
        self.play(FadeIn(text1b))
        self.add(sides1[0],sides2[0])
        self.wait(1)
        ratio_txt3 = MathTex("{157","\\over","121}","\\approx 1.3")
        ratio_txt3.next_to(ratio_txt2,DOWN)
        self.play(FadeIn(ratio_txt3))
        self.wait(2)
        self.play(FadeOut(text1b))
        # Conclusion
        textc = Tex("Because all angles have the same measure the triangles are similar.")
        textc.to_edge(DOWN)
        self.play(FadeIn(textc))
        self.wait(2)
        self.play(FadeOut(textc))
        textcb = Tex("Also the ratio of corresponding sides are the same.")
        textcb.to_edge(DOWN)
        self.play(FadeIn(textcb))

        self.wait(5)

class sigfig_multi(Scene):
    def construct(self):
        title = Text("Sigfig Arithmetic")
        title.to_edge(UP)
        self.add(title)

        eq1 = MathTex(r'\left(','{57-46', r'\over','{46}}',r'\right)','(','54.3-48.2',')')
        eq2 = MathTex(r'\left(','{11 ',r'\over',' 46}',r'\right)','(','54.3-48.2',')')
        eq3 = MathTex(r'\left(','{11 ',r'\over',' 46}',r'\right)','(','6.1',')')
        eq4 = MathTex('(','0.23','9130',')','(','6.1',')')
        eq5 = MathTex('1.4','586930')
        eq6 = MathTex('1.5')
        self.add(eq1)
        self.wait(2)
        text1 = Text("Both are precise to units, subtraction maintains that precision.",font_size=20).to_edge(DOWN)
        self.play(FadeIn(text1),
            ReplacementTransform(eq1, eq2)
        )
        self.wait(2)
        self.play(FadeOut(text1))
        text2 = Text("Both are precise to tenths, subtraction maintains that precision.",font_size=20).to_edge(DOWN)
        self.play(FadeIn(text2),
            ReplacementTransform(eq2, eq3)
        )
        self.wait(2)
        self.play(FadeOut(text2))
        text3 = Text("Both have 2 sigfigs, division maintains 2 sigfigs.",font_size=20).to_edge(DOWN)
        eq4[2].set_color(GRAY)
        self.play(FadeIn(text3),
            ReplacementTransform(eq3, eq4)
        )
        self.wait(2)
        self.play(FadeOut(text3))
        text4 = Text("Both have 2 sigfigs, product maintains 2 sigfigs.",font_size=20).to_edge(DOWN)
        eq5[1].set_color(GRAY)
        self.play(FadeIn(text4),
            ReplacementTransform(eq4, eq5)
        )
        self.wait(2)
        self.play(FadeOut(text4))
        text5 = Text("Round last significant digit.",font_size=20).to_edge(DOWN)
        self.play(FadeIn(text5),
            ReplacementTransform(eq5, eq6)
        )

        self.wait(5)

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
