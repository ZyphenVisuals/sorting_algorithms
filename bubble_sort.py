from manim import *

class ArrayItem:
    def __init__(self, value):
        self.value = value
        self.square = Square(side_length=1)
        self.text = Integer(value)
        
class Thumbnail(Scene):
    def construct(self):

        title = Title("Sorting algorithms 3:")
        subtitle = Text("Bubble sort", font_size=90)

        self.add(title)
        self.add(subtitle)

class Intro(Scene):
    def construct(self):

        title = Text("Bubble sort")

        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title, reverse=False))

class Sort(Scene):
    def construct(self):
        # initialize the array
        data = [2,3,1,4,7,6,5,9,8]

        # transform the array into ArrayItems
        dArray = []
        for el in data:
            dArray.append(ArrayItem(el))

        # create the VGroup for Manim rendering
        gArray = VGroup()
        # add the squares
        for el in dArray:
            gArray.add(VGroup().add_to_back(el.square).add(el.text))
        # arrange them
        gArray.arrange(buff=0)
        # add the texts
        #for el in range(len(dArray)):
            #gArray.add(dArray[el].text.align_to(dArray[el].square))

        self.play(Write(gArray, lag_ratio=0.1))
        self.wait(1)

        # sort
        for i in range(len(dArray)):
            if i != 0:
                self.play(AnimationGroup(dArray[len(dArray)-i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3),
                                         dArray[len(dArray)-i-1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0)))
            for j in range(0, len(dArray) - i - 1):
                if j != 0:
                    self.play(AnimationGroup(dArray[j-1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0),
                                        dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3),
                                        dArray[j+1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3)))
                else:
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3)))
                if dArray[j].value > dArray[j + 1].value:
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(RED, opacity=0.3),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(RED, opacity=0.3)))
                    auxJ = gArray[j].copy()
                    auxJ2 = gArray[j+1].copy()
                    self.play(AnimationGroup(Transform(gArray[j], auxJ2.match_x(gArray[j]), run_time=0.3),
                                             Transform(gArray[j+1], auxJ.match_x(gArray[j+1]), run_time=0.3)))
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(RED, opacity=0),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(RED, opacity=0)))
                    dArray[j].value, dArray[j+1].value = dArray[j+1].value, dArray[j].value

        self.play(dArray[0].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1))

class SortWithDuplicates(Scene):
    def construct(self):
        # initialize the array
        data = [4,1,3,2,4]

        # transform the array into ArrayItems
        dArray = []
        for el in data:
            dArray.append(ArrayItem(el))

        # create the VGroup for Manim rendering
        gArray = VGroup()
        # add the squares
        for el in dArray:
            gArray.add(VGroup().add_to_back(el.square).add(el.text))
        # arrange them
        gArray.arrange(buff=0)
        # add the texts
        #for el in range(len(dArray)):
            #gArray.add(dArray[el].text.align_to(dArray[el].square))

        self.play(Write(gArray, lag_ratio=0.1))
        self.wait(1)

        # sort
        for i in range(len(dArray)):
            if i != 0:
                self.play(AnimationGroup(dArray[len(dArray)-i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3),
                                         dArray[len(dArray)-i-1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0)))
            for j in range(0, len(dArray) - i - 1):
                if j != 0:
                    self.play(AnimationGroup(dArray[j-1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0),
                                        dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3),
                                        dArray[j+1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3)))
                else:
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3)))
                if dArray[j].value > dArray[j + 1].value:
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(RED, opacity=0.3),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(RED, opacity=0.3)))
                    auxJ = gArray[j].copy()
                    auxJ2 = gArray[j+1].copy()
                    self.play(AnimationGroup(Transform(gArray[j], auxJ2.match_x(gArray[j]), run_time=0.3),
                                             Transform(gArray[j+1], auxJ.match_x(gArray[j+1]), run_time=0.3)))
                    self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(RED, opacity=0),
                                         dArray[j+1].square.animate(run_time=0.3).set_fill(RED, opacity=0)))
                    dArray[j].value, dArray[j+1].value = dArray[j+1].value, dArray[j].value

        self.play(dArray[0].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1))

class DrawCode(Scene):
    def construct(self):
        listing = Code(
            "code/bubble_sort.py",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style="github-dark",
            background="window",
            language="py",
            font_size=24,
        )

        self.play(Write(listing))
        self.wait(1)