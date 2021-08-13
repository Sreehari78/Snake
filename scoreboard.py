from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


def read_high_score():
    with open("high_score.txt", mode="r") as file_read:
        high_score = file_read.read()
        file_read.close()
        return int(high_score)


def write_high_score(score):
    with open("high_score.txt", mode="w") as file_write:
        file_write.write(str(score))
        file_write.close()


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = -1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} High Score: {read_high_score()}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(read_high_score()):
            write_high_score(self.score)
        self.score = -1
        self.update_score()
