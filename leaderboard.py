class Leaderboard:
    def __init__(self):
        self.json = __import__("json")
        self.turtle = __import__("turtle")
        self.FONT = ("Arial", 20, "normal")

    def read_leaderboard(self) -> dict:
        with open("leaderboard.json") as leaderboard:
            return self.json.load(leaderboard)

    def write_to_leaderboard(self, player_name: str, score: int) -> None:
        current_leaderboard = self.read_leaderboard()
        current_leaderboard[player_name] = score
        with open("leaderboard.json", "w") as leaderboard:
            self.json.dump(current_leaderboard, leaderboard)

    def top_five(self) -> dict:
        current_data = self.read_leaderboard()
        sorted_scores = (
            sorted([x for x in current_data.values()])[::-1][:5]
            if len(current_data.values()) >= 5
            else sorted([x for x in current_data.values()])[::-1]
        )
        current_data = {
            x: y
            for x, y in sorted(current_data.items(), key=lambda item: item[1])[::-1]
        }
        return current_data

    def display_leaderboard(self):
        leaderboard_writer = self.turtle.Turtle()
        leaderboard_writer.pencolor("white")
        leaderboard_writer.pu()
        current_scores = self.top_five()
        leaderboard_writer.hideturtle()
        for x in range(len(current_scores)):
            leaderboard_writer.goto(-200, leaderboard_writer.ycor() - 50)
            leaderboard_writer.write(
                f"#{x + 1}: {list(current_scores.keys())[x]}, {list(current_scores.values())[x]}",
                font=self.FONT,
            )
