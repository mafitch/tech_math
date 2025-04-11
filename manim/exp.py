from manim import *

class exp_rate(MovingCameraScene):
    def construct(self):

        def always_redraw_axes(axes_maker_func):
            mob = axes_maker_func

            def become_axes(m):
                old_axes = mob
                new_axes = make_axes()
                old_axes.become(new_axes)
                old_axes.x_axis.x_range = new_axes.x_axis.x_range
                old_axes.x_axis.scaling = new_axes.x_axis.scaling
                old_axes.y_axis.x_range = new_axes.y_axis.x_range
                old_axes.y_axis.scaling = new_axes.y_axis.scaling
            mob.add_updater(become_axes)
            return mob
        def make_axes():
            temp = Axes( 
                x_range = (0,xmax1.get_value(),6), 
                y_range = (0,ymax1.get_value(),243), 
                tips = False,
                x_axis_config={
                    "font_size": 24,
                    "include_numbers": False,
                    "numbers_to_include": [i for i in range(0,5+1)]
                },
                y_axis_config={
                    "font_size": 24,
                    "include_numbers": False,
                    "numbers_to_include": [(3**i)/2 for i in range(0,5+1)],
                    'decimal_number_config': {
                        "num_decimal_places": 1
                    }
                }
            )
            temp.add_coordinates()
            return temp

        # old code attempting to use one updater for all segments, worked on 1st 2 only
        def seg_updater(mob):
            tmob = VGroup()
            c1 = axes.point_to_coords(mob[0].start)
            c2 = axes.point_to_coords(mob[0].end)
            tll = Line(axes.c2p(c1[0],c1[1]),axes.c2p(c2[0],c2[1]),color=GREEN,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex(mob[1].tex_strings[0], mob[1].tex_strings[1], font_size=24).next_to(tll,UP+RIGHT) ) )
            mob = tmob

        def func(x):
            return (3**x)/2

        # Title screen
        title1 = Text("Exponential Growth")
        self.add(title1)
        self.wait(2)
        self.remove(title1)

        # Title screen
        title2a = Text("Exponential Growth")
        title2b = Text("Measured by Ratio").next_to(title2a,DOWN)
        title2 = VGroup(title2a,title2b)
        self.add(title2)
        self.wait(3)
        self.remove(title2)

        # Define axes including code to scale them
        xmax1 = ValueTracker(1)
        ymax1 = ValueTracker(2)
        axes = always_redraw_axes(make_axes())
        self.add(axes)

        func_text = MathTex("{1 \\over 2}","3^x",font_size=32)
        func_text.to_edge(UP)
        self.add(func_text)
        self.wait(2)

        # Draw segment 0
        def seg_updater_p0(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(0,0),axes.c2p(0,func(0)),color=GREEN,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{1", "\\over 2}",font_size=24).next_to( lines0 ,UP+RIGHT) ) )
            mob = tmob
        
        lines0 = Line(axes.c2p(0,0),axes.c2p(0,func(0)),color=GREEN,stroke_width=6)
        segments0 = VGroup(lines0, MathTex("{1", "\\over 2}",font_size=24).next_to( lines0 ,UP+RIGHT) )
        segments0.add_updater(seg_updater_p0)
        self.play( Create(lines0) )
        self.add( segments0 )

        # Draw segment 1
        desc1 = Text("This segment is tripled.").next_to(func_text,DOWN)
        self.play(Write(desc1))
        rotate_line0 = Line(axes.c2p(0,0),axes.c2p(0,func(0)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(1,func(0)/2) ) )
        self.play( Indicate(func_text[1],scale_factor=1.5) )
        rotate_line1 = Line(axes.c2p(1,0),axes.c2p(1,func(0)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(1,func(0)) ) )
        rotate_line2 = Line(axes.c2p(1,func(0)),axes.c2p(1,func(0)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(1,func(0)*2) ) )

        def seg_updater_p1(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(1,0),axes.c2p(1,func(1)), color=GREEN, stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{3", "\\over 2}",font_size=24).next_to( lines1 ,UP+RIGHT) ) )
            mob = tmob

        lines1 = Line(axes.c2p(1,0),axes.c2p(1,func(1)), color=GREEN, stroke_width=6) 
        segments1 = VGroup(lines1, MathTex("{3", "\\over 2}",font_size=24).next_to( lines1 ,UP+RIGHT) )
        segments1.add_updater(seg_updater_p1)
        self.add(segments1)

        self.remove(rotate_line0,rotate_line1,rotate_line2,desc1)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(2), ymax1.animate.set_value(np.ceil(func(2))))

        # Draw segment 2
        self.play(Write(desc1))
        rotate_line0 = Line(axes.c2p(1,0),axes.c2p(1,func(1)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(2,func(1)/2) ) )
        self.play( Indicate(func_text[1],scale_factor=1.5) )
        rotate_line1 = Line(axes.c2p(2,0),axes.c2p(2,func(1)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(2,func(1)) ) )
        rotate_line2 = Line(axes.c2p(2,func(1)),axes.c2p(2,func(1)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(2,func(1)*2) ) )

        def seg_updater_p2(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(2,0),axes.c2p(2,func(2)), color=GREEN, stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{9", "\\over 2}",font_size=24).next_to( lines2 ,UP+RIGHT) ) )
            mob = tmob

        lines2 = Line(axes.c2p(2,0),axes.c2p(2,func(2)), color=GREEN, stroke_width=6)
        segments2 = VGroup(lines2, MathTex("{9", "\\over 2}",font_size=24).next_to( lines2 ,UP+RIGHT) )
        segments2.add_updater(seg_updater_p2)
        self.add(segments2)

        self.remove(rotate_line0,rotate_line1,rotate_line2,desc1)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(3), ymax1.animate.set_value(np.ceil(func(3))))

        # Draw segment 3
        self.play(Write(desc1))
        rotate_line0 = Line(axes.c2p(2,0),axes.c2p(2,func(2)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(3,func(2)/2) ) )
        self.play( Indicate(func_text[1],scale_factor=1.5) )
        rotate_line1 = Line(axes.c2p(3,0),axes.c2p(3,func(2)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(3,func(2)) ) )
        rotate_line2 = Line(axes.c2p(3,func(2)),axes.c2p(3,func(2)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(3,func(2)*2) ) )

        def seg_updater_p3(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(3,0),axes.c2p(3,func(3)), color=GREEN, stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{27", "\\over 2}",font_size=24).next_to( lines3 ,UP+RIGHT) ) )
            mob = tmob

        lines3 = Line(axes.c2p(3,0),axes.c2p(3,func(3)), color=GREEN, stroke_width=6)
        segments3 = VGroup(lines3, MathTex("{27", "\\over 2}",font_size=24).next_to( lines3 ,UP+RIGHT) )
        segments3.add_updater(seg_updater_p3)
        self.add(segments3)
        self.play( Indicate(segments3[1],scale_factor=1.5) )

        self.remove(rotate_line0,rotate_line1,rotate_line2,desc1)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(4), ymax1.animate.set_value(np.ceil(func(4))))

        # Draw segment 4
        self.play(Write(desc1))
        rotate_line0 = Line(axes.c2p(3,0),axes.c2p(3,func(3)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(4,func(3)/2) ) )
        self.play( Indicate(func_text[1],scale_factor=1.5) )
        rotate_line1 = Line(axes.c2p(4,0),axes.c2p(4,func(3)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(4,func(3)) ) )
        rotate_line2 = Line(axes.c2p(4,func(3)),axes.c2p(4,func(3)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(4,func(3)*2) ) )

        def seg_updater_p4(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(4,0),axes.c2p(4,func(4)), color=GREEN, stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{81", "\\over 2}",font_size=24).next_to( lines4 ,UP+RIGHT) ) )
            mob = tmob

        lines4 = Line(axes.c2p(4,0),axes.c2p(4,func(4)), color=GREEN, stroke_width=6)
        segments4 = VGroup(lines4, MathTex("{81", "\\over 2}",font_size=24).next_to( lines4 ,UP+RIGHT) )
        segments4.add_updater(seg_updater_p4)
        self.add(segments4)

        self.remove(rotate_line0,rotate_line1,rotate_line2,desc1)
        self.wait(4)

        # Subtraction illustation title screen
        title3a = Text("Exponential Growth")
        title3b = Text("Measured by Differences").next_to(title3a,DOWN)
        title3 = VGroup(title3a,title3b)
        self.add(title3)
        self.wait(3)
        self.remove(title3)

        # subtract first 2 segments
        self.play(xmax1.animate.set_value(1), ymax1.animate.set_value(np.ceil(func(1))))

        def seg_updater_p0b(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(0,func(0)),axes.c2p(0,func(1)),color=RED,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{2 \\over 2}","=2 \cdot", "{1 \\over 2}",font_size=24).next_to( lines0c ,UP+RIGHT) ) )
            tmob[1][0:2].set_color(BLACK)
            mob = tmob

        desc2 = Text("Subtract these two segments.").next_to(func_text,DOWN)
        self.play(Write(desc2))
        lines0b = Line(axes.c2p(1,0),axes.c2p(1,func(1)),color=GREEN,stroke_width=6)
        lines0c = Line(axes.c2p(0,func(0)),axes.c2p(0,func(1)),color=RED,stroke_width=6)
        segments0b = VGroup( lines0c, MathTex("{2 \\over 2}", "=2 \cdot", "{1 \\over 2}",font_size=24).next_to( lines0c ,UP+RIGHT) )
        segments0b[1][1:3].set_color(BLACK)
        self.add(lines0b)
        self.play( ApplyMethod( lines0b.move_to, axes.c2p(0,func(1)/2) ) )
        self.play( FadeOut(lines0b), FadeIn(lines0c) )
        self.add(segments0b)
        self.wait(1)
        segments0b[1][1:3].set_color(WHITE)
        segments0.remove_updater(seg_updater_p0)
        self.play(Indicate(segments0b[1][2],scale_factor=1.5),Indicate(segments0[1],scale_factor=1.5))
        segments0b[1][0:2].set_color(BLACK)
        segments0.add_updater(seg_updater_p0)
        segments0b.add_updater(seg_updater_p0b)
        self.remove(desc2)
        self.wait(2)

        # subtract second 2 segments
        self.play(xmax1.animate.set_value(2), ymax1.animate.set_value(np.ceil(func(2))))

        def seg_updater_p1b(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(1,func(1)),axes.c2p(1,func(2)),color=RED,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{6 \\over 2}","=2 \cdot", "{3 \\over 2}",font_size=24).next_to( lines1c ,UP+RIGHT) ) )
            tmob[1][0:2].set_color(BLACK)
            mob = tmob

        desc3 = Text("Subtract the rightmost two segments.").next_to(func_text,DOWN)
        self.play(Write(desc3))
        lines1b = Line(axes.c2p(2,0),axes.c2p(2,func(2)),color=GREEN,stroke_width=6)
        lines1c = Line(axes.c2p(1,func(1)),axes.c2p(1,func(2)),color=RED,stroke_width=6)
        segments1b = VGroup( lines1c, MathTex("{6 \\over 2}","=2 \cdot", "{3 \\over 2}",font_size=24).next_to( lines1c ,UP+RIGHT) )
        segments1b[1][1:3].set_color(BLACK)
        self.add(lines1b)
        self.play( ApplyMethod( lines1b.move_to, axes.c2p(1,func(2)/2) ) )
        self.play( FadeOut(lines1b), FadeIn(lines1c) )
        self.add(segments1b)
        self.wait(1)
        segments1b[1][1:3].set_color(WHITE)
        segments1.remove_updater(seg_updater_p1)
        self.play(Indicate(segments1b[1][2],scale_factor=1.5),Indicate(segments1[1],scale_factor=1.5))
        segments1b[1][0:2].set_color(BLACK)
        segments1.add_updater(seg_updater_p1)
        segments1b.add_updater(seg_updater_p1b)
        self.remove(desc3)
        self.wait(2)

        # subtract third 2 segments
        self.play(xmax1.animate.set_value(3), ymax1.animate.set_value(np.ceil(func(3))))

        def seg_updater_p2b(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(2,func(2)),axes.c2p(2,func(3)),color=RED,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{18 \\over 2}","= 2 \cdot", "{9 \\over 2}",font_size=24).next_to( lines2c ,UP+RIGHT) ) )
            tmob[1][0:2].set_color(BLACK)
            mob = tmob

        self.play(Write(desc3))
        lines2b = Line(axes.c2p(3,0),axes.c2p(3,func(3)),color=GREEN,stroke_width=6)
        lines2c = Line(axes.c2p(2,func(2)),axes.c2p(2,func(3)),color=RED,stroke_width=6)
        segments2b = VGroup( lines2c, MathTex("{18 \\over 2}","= 2 \cdot", "{9 \\over 2}",font_size=24).next_to( lines2c ,UP+RIGHT) )
        segments2b[1][1:3].set_color(BLACK)
        self.add(lines2b)
        self.play( ApplyMethod( lines2b.move_to, axes.c2p(2,func(3)/2) ) )
        self.play( FadeOut(lines2b), FadeIn(lines2c) )
        self.add(segments2b)
        self.wait(1)
        segments2b[1][1:3].set_color(WHITE)
        segments2.remove_updater(seg_updater_p2)
        self.play(Indicate(segments2b[1][2],scale_factor=1.5),Indicate(segments2[1],scale_factor=1.5))
        segments2b[1][0:2].set_color(BLACK)
        segments2.add_updater(seg_updater_p2)
        segments2b.add_updater(seg_updater_p2b)
        self.remove(desc3)
        self.wait(2)

        # subtract fourth 2 segments
        self.play(xmax1.animate.set_value(4), ymax1.animate.set_value(np.ceil(func(4))))

        def seg_updater_p3b(mob):
            tmob = VGroup()
            tll = Line(axes.c2p(3,func(3)),axes.c2p(3,func(4)),color=RED,stroke_width=6)
            tmob.add(mob[0].become( tll ))
            tmob.add(mob[1].become( MathTex("{54 \\over 2}", "=2 \cdot", "{27 \\over 2}",font_size=24).next_to( lines3c ,UP+RIGHT) ) )
            tmob[1][0:2].set_color(BLACK)
            mob = tmob

        self.play(Write(desc3))
        lines3b = Line(axes.c2p(4,0),axes.c2p(4,func(4)),color=GREEN,stroke_width=6)
        lines3c = Line(axes.c2p(3,func(3)),axes.c2p(3,func(4)),color=RED,stroke_width=6)
        segments3b = VGroup( lines3c, MathTex("{54 \\over 2}", "=2 \cdot", "{27 \\over 2}",font_size=24).next_to( lines3c ,UP+RIGHT) )
        segments3b[1][1:3].set_color(BLACK)
        self.add(lines3b)
        self.play( ApplyMethod( lines3b.move_to, axes.c2p(3,func(4)/2) ) )
        self.play( FadeOut(lines3b), FadeIn(lines3c) )
        self.add(segments3b)
        self.wait(1)
        segments3b[1][1:3].set_color(WHITE)
        segments3.remove_updater(seg_updater_p3)
        self.play(Indicate(segments3b[1][2],scale_factor=1.5),Indicate(segments3[1],scale_factor=1.5))
        segments3b[1][0:2].set_color(BLACK)
        segments3.add_updater(seg_updater_p3)
        segments3b.add_updater(seg_updater_p3b)
        self.remove(desc3)
        self.wait(2)

        self.wait(5)
