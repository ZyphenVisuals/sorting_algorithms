from manim import *

class ArrayItem:
    def __init__(self, value):
        self.value = value
        self.square = Square(side_length=1)
        self.text = Integer(value)
        
class Thumbnail(Scene):
    def construct(self):

        title = Title("Sorting algorithms 1:")
        subtitle = Text("Insertion sort", font_size=90)

        self.add(title)
        self.add(subtitle)

class Intro(Scene):
    def construct(self):

        title = Text("Insertion sort")

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
        for step in range(1, len(dArray)):
            aux = dArray[step].value
            auxEl = gArray[step].copy()
            self.add(auxEl)
            self.play(auxEl.animate(run_time=0.3).shift(DOWN*1))
            # Loop through all previous items
            j = step - 1
            self.play(auxEl.animate(run_time=0.3).shift(LEFT*1))
            # Compare aux with each element on the left of it until an element smaller than it is found
            while j >= 0 and aux < dArray[j].value:
                newInteger = VGroup().add_to_back(Square(side_length=1)).add(Integer(dArray[j].value))
                self.play(Transform(gArray[j + 1], newInteger.match_x(gArray[j+1]), run_time=0.3))
                dArray[j + 1].value = dArray[j].value
                self.play(auxEl.animate(run_time=0.3).shift(LEFT*1))
                j = j - 1
            # Place key at after the element just smaller than it.
            self.play(auxEl.animate(run_time=0.3).shift(RIGHT*1))
            self.play(Unwrite(gArray[j+1], run_time=0.3))
            gArray[j+1] = auxEl
            self.play(gArray[j+1].animate(run_time=0.3).shift(UP*1))
            dArray[j + 1].value = aux
        
        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1, reverse=False))

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
        for step in range(1, len(dArray)):
            aux = dArray[step].value
            auxEl = gArray[step].copy()
            self.add(auxEl)
            self.play(auxEl.animate(run_time=0.3).shift(DOWN*1))
            # Loop through all previous items
            j = step - 1
            self.play(auxEl.animate(run_time=0.3).shift(LEFT*1))
            # Compare aux with each element on the left of it until an element smaller than it is found
            while j >= 0 and aux < dArray[j].value:
                newInteger = VGroup().add_to_back(Square(side_length=1)).add(Integer(dArray[j].value))
                self.play(Transform(gArray[j + 1], newInteger.match_x(gArray[j+1]), run_time=0.3))
                dArray[j + 1].value = dArray[j].value
                self.play(auxEl.animate(run_time=0.3).shift(LEFT*1))
                j = j - 1
            # Place key at after the element just smaller than it.
            self.play(auxEl.animate(run_time=0.3).shift(RIGHT*1))
            self.play(Unwrite(gArray[j+1], run_time=0.3))
            gArray[j+1] = auxEl
            self.play(gArray[j+1].animate(run_time=0.3).shift(UP*1))
            dArray[j + 1].value = aux
        
        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1, reverse=False))

class DrawCode(Scene):
    def construct(self):
        listing = Code(
            "code/insertion_sort.py",
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