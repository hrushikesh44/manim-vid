from manim import *

class HelloWorld(Scene):
    def construct(self):
        # First text
        welcome_text = Text("Welcome to the video", font_size=64)
        self.play(Write(welcome_text))
        self.wait(2)
        self.play(FadeOut(welcome_text))

        # Second text
        topic_text = Text("Today we learn about Binary Search", font_size=60)
        self.play(Write(topic_text))
        self.wait(3)
        self.play(FadeOut(topic_text))

        topic_exp = Text("Binary Search in the simple manner" , font_size=50)
        self.play(Write(topic_exp))
        self.wait(3)
        self.play(FadeOut(topic_exp))
        
        # array = Text("[1,2,3,4,5,6,7,8,9]", font_size=60)
        # self.play(Write(array))
        # self.wait(3)

        # arrow = Arrow(
        #     start=char_a.get_center(),
        #     end=char_b.get_center(),
        #     buff=0.1,
        #     color=BLUE
        # )
        # self.play(GrowArrow(arrow))
        # self.wait(2)
        # self.play(FadeOut(array))
        # self.play(FadeOut(arrow))



class BinarySearchIntro(Scene):
    def construct(self):
        # Title
        title = Text("Binary Search", font_size=60).to_edge(UP)
        self.play(Write(title))

        # Array elements
        numbers = [1, 3, 5, 7, 9, 11, 13]
        boxes = VGroup(*[
            Square(side_length=1.2).set_fill(GREY, 0.1) for _ in numbers
        ])
        boxes.arrange(RIGHT, buff=0.2).shift(DOWN)

        texts = VGroup(*[
            Text(str(num), font_size=36).move_to(boxes[i].get_center())
            for i, num in enumerate(numbers)
        ])

        self.play(Create(boxes), Write(texts))

        # search for 9
        target = 9
        low, high = 0, len(numbers) - 1

        # what am i searching for
        search_text = Text(f"Searching for: {target}", font_size=36).next_to(boxes, DOWN, buff=1)
        self.play(Write(search_text))
        self.wait(1)

        while low <= high:
            mid = (low + high) // 2

            #  current low, mid, high
            low_box = boxes[low].copy().set_stroke(color=BLUE, width=6)
            mid_box = boxes[mid].copy().set_stroke(color=YELLOW, width=6)
            high_box = boxes[high].copy().set_stroke(color=RED, width=6)

            self.play(Create(low_box), Create(mid_box), Create(high_box))
            self.wait(1)

            mid_value = numbers[mid]
            if mid_value == target:
                found_text = Text(f"Found {target} at index {mid}!", font_size=36, color=GREEN).next_to(search_text, DOWN)
                self.play(Write(found_text))
                self.wait(2)
                break
            else:
                self.play(FadeOut(low_box), FadeOut(mid_box), FadeOut(high_box))
                if mid_value < target:
                    low = mid + 1
                else:
                    high = mid - 1

        self.wait(1)


class BinarySearchWithArrows(Scene):
    def construct(self):
       
        title = Text("Binary Search", font_size=60).to_edge(UP)
        self.play(Write(title))

        #array
        numbers = [1, 3, 5, 7, 9, 11, 13]
        boxes = VGroup(*[Square(1.2).set_fill(GREY, 0.1) for _ in numbers])
        boxes.arrange(RIGHT, buff=0.2).shift(DOWN * 0.5)

        elements = VGroup(*[
            Text(str(num), font_size=36).move_to(boxes[i].get_center())
            for i, num in enumerate(numbers)
        ])

        self.play(Create(boxes), Write(elements))

        # searching 
        target = 9
        search_text = Text(f"Searching for: {target}", font_size=36)
        search_text.next_to(boxes, DOWN, buff=1)
        self.play(Write(search_text))
        self.wait(1)

        # binary Search logic
        low, high = 0, len(numbers) - 1
        low_arrow = None
        mid_arrow = None
        high_arrow = None

        while low <= high:
            mid = (low + high) // 2

            #arrows pointing to low, mid, high
            def get_arrow(index, label, color):
                arrow = Arrow(
                    start=boxes[index].get_top() + UP * 0.3,
                    end=boxes[index].get_top(),
                    buff=0.05,
                    stroke_width=6,
                    color=color
                )
                tag = Text(label, font_size=24, color=color).next_to(arrow, UP, buff=0.1)
                return VGroup(arrow, tag)

            # delete old arrows
            if low_arrow: self.play(FadeOut(low_arrow))
            if mid_arrow: self.play(FadeOut(mid_arrow))
            if high_arrow: self.play(FadeOut(high_arrow))

            #  updated arrows
            low_arrow = get_arrow(low, "low", BLUE)
            mid_arrow = get_arrow(mid, "mid", YELLOW)
            high_arrow = get_arrow(high, "high", RED)

            self.play(GrowArrow(low_arrow[0]), Write(low_arrow[1]),
                      GrowArrow(mid_arrow[0]), Write(mid_arrow[1]),
                      GrowArrow(high_arrow[0]), Write(high_arrow[1]))
            self.wait(1)

            # check if found
            if numbers[mid] == target:
                success = Text(f"Found {target} at index {mid}!", font_size=36, color=GREEN)
                success.next_to(search_text, DOWN)
                self.play(Write(success))
                self.wait(2)
                break
            elif numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        self.wait(1)