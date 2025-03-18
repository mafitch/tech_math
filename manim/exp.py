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
                    "include_numbers": False,
                    "numbers_to_include": [i for i in range(0,5+1)]
                },
                y_axis_config={
                    "include_numbers": False,
                    "numbers_to_include": [(3**i)/2 for i in range(0,5+1)],
                    'decimal_number_config': {
                        "num_decimal_places": 1
                    }
                }
            )
            temp.add_coordinates()
            return temp

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

        title1 = Text("Exponential Growth")
        self.add(title1)
        self.wait(3)
        self.remove(title1)

        # Define axes including code to scale them
        xmax1 = ValueTracker(1)
        ymax1 = ValueTracker(2)
        axes = always_redraw_axes(make_axes())
        self.add(axes)

        func_text = MathTex("{1 \\over 2}","3^x",font_size=32)
        func_text.to_edge(UP)
        self.add(func_text)
        self.wait(1)
        
        lines0 = Line(axes.c2p(0,0),axes.c2p(0,func(0)),color=GREEN,stroke_width=6)
        segments0 = VGroup(lines0, MathTex("{1", "\\over 2}",font_size=24).next_to( lines0 ,UP+RIGHT) )
        segments0.add_updater(seg_updater)
        self.play( Create(lines0) )
        self.add( segments0 )

        # Draw segment 1
        rotate_line0 = Line(axes.c2p(0,0),axes.c2p(0,func(0)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(1,func(0)/2) ) )
        rotate_line1 = Line(axes.c2p(1,0),axes.c2p(1,func(0)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(1,func(0)) ) )
        rotate_line2 = Line(axes.c2p(1,func(0)),axes.c2p(1,func(0)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(1,func(0)*2) ) )

        lines1 = Line(axes.c2p(1,0),axes.c2p(1,func(1)), color=GREEN, stroke_width=6) 
        segments1 = VGroup(lines1, MathTex("{3", "\\over 2}",font_size=24).next_to( lines1 ,UP+RIGHT) )
        segments1.add_updater(seg_updater)
        self.add(segments1)

        self.remove(rotate_line0,rotate_line1,rotate_line2)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(2), ymax1.animate.set_value(np.ceil(func(2))))

        # Draw segment 2
        rotate_line0 = Line(axes.c2p(1,0),axes.c2p(1,func(1)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(2,func(1)/2) ) )
        rotate_line1 = Line(axes.c2p(2,0),axes.c2p(2,func(1)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(2,func(1)) ) )
        rotate_line2 = Line(axes.c2p(2,func(1)),axes.c2p(2,func(1)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(2,func(1)*2) ) )

        lines2 = Line(axes.c2p(2,0),axes.c2p(2,func(2)), color=GREEN, stroke_width=6)
        segments2 = VGroup(lines2, MathTex("{9", "\\over 2}",font_size=24).next_to( lines2 ,UP+RIGHT) )
        segments2.add_updater(seg_updater)
        self.add(segments2)

        self.remove(rotate_line0,rotate_line1,rotate_line2)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(3), ymax1.animate.set_value(np.ceil(func(3))))

        # Draw segment 3
        rotate_line0 = Line(axes.c2p(2,0),axes.c2p(2,func(2)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(3,func(2)/2) ) )
        rotate_line1 = Line(axes.c2p(3,0),axes.c2p(3,func(2)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(3,func(2)) ) )
        rotate_line2 = Line(axes.c2p(3,func(2)),axes.c2p(3,func(2)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(3,func(2)*2) ) )

        lines3 = Line(axes.c2p(3,0),axes.c2p(3,func(3)), color=GREEN, stroke_width=6)
        segments3 = VGroup(lines3, MathTex("{27", "\\over 2}",font_size=24).next_to( lines3 ,UP+RIGHT) )
        segments3.add_updater(seg_updater)
        self.add(segments3)

        self.remove(rotate_line0,rotate_line1,rotate_line2)
        self.wait(2)

        # adjust view for next element
        self.play(xmax1.animate.set_value(4), ymax1.animate.set_value(np.ceil(func(4))))

        # Draw segment 4
        rotate_line0 = Line(axes.c2p(3,0),axes.c2p(3,func(3)),color=GREEN,stroke_width=6)
        self.add( rotate_line0 )
        self.play( ApplyMethod(rotate_line0.move_to, axes.c2p(4,func(3)/2) ) )
        rotate_line1 = Line(axes.c2p(4,0),axes.c2p(4,func(3)),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line1 , angle=PI, about_point=axes.c2p(4,func(3)) ) )
        rotate_line2 = Line(axes.c2p(4,func(3)),axes.c2p(4,func(3)*2),color=GREEN,stroke_width=6)
        self.add(rotate_line1)
        self.play( Rotate(rotate_line2 , angle=PI, about_point=axes.c2p(4,func(3)*2) ) )

        lines4 = Line(axes.c2p(4,0),axes.c2p(4,func(4)), color=GREEN, stroke_width=6)
        segments4 = VGroup(lines4, MathTex("{81", "\\over 2}",font_size=24).next_to( lines4 ,UP+RIGHT) )
        segments4.add_updater(seg_updater)
        self.add(segments4)

        self.remove(rotate_line0,rotate_line1,rotate_line2)

        self.wait(5)
