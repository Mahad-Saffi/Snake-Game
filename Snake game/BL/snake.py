from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
WIDTH = 800
HEIGHT = 800


def add_segment():
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    return new_segment


class Snake:
    def __init__(self, length_of_snake):
        self.length_of_snake = length_of_snake
        self.next_snake_segment_X_cord = 0
        self.snake_segment_X_cord_len = 20
        self.starting_positions_of_snake_segments = []
        self.snake_segments = []

        self.create_snake(length_of_snake)
        self.snake_head = self.snake_segments[0]

    def create_snake(self, length_of_snake):
        for snake_index in range(length_of_snake):
            new_snake_segment = add_segment()
            starting_position = (self.next_snake_segment_X_cord, 0)
            new_snake_segment.goto(starting_position)
            self.starting_positions_of_snake_segments.append(starting_position)
            self.next_snake_segment_X_cord -= self.snake_segment_X_cord_len
            self.snake_segments.append(new_snake_segment)

    def increase_segment(self):
        new_segment = add_segment()
        new_segment.goto(self.snake_segments[len(self.snake_segments) - 1].xcor(),
                         self.snake_segments[len(self.snake_segments) - 1].ycor())
        self.snake_segments.append(new_segment)

    def move(self):
        # To move snake from one side of the screen towards the other
        if self.snake_head.xcor() >= WIDTH / 2:
            self.snake_head.goto(-WIDTH/2, self.snake_head.ycor())
        elif self.snake_head.xcor() <= -(WIDTH / 2):
            self.snake_head.goto(WIDTH/2, self.snake_head.ycor())
        elif self.snake_head.ycor() >= HEIGHT / 2:
            self.snake_head.goto(self.snake_head.xcor(), -(HEIGHT/2))
        elif self.snake_head.ycor() <= -(HEIGHT / 2):
            self.snake_head.goto(self.snake_head.xcor(), HEIGHT/2)

        # To move all the segments of snake with respect to head
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x_cord = self.snake_segments[seg_num - 1].xcor()
            new_y_cord = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x_cord, new_y_cord)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
