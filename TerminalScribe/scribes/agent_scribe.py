from scribes.terminal_scribe import TerminalScribe


class AgentScribe(TerminalScribe):
    def __init__(self, start_pos):
        super().__init__(start_pos)
        # This class extension may have unique properties to be established after the parent constructor

    def up(self, distance=1):
        """
        Agent receives an action to move up by a given distance.
        """
        self.get_moves([0, distance])

    def down(self, distance=1):
        """
        Agent receives an action to down up by a given distance.
        """
        self.get_moves([180, distance])

    def right(self, distance=1):
        """
        Agent receives an action to move right by a given distance.
        """
        self.get_moves([90, distance])

    def left(self, distance=1):
        """
        Agent receives an action to move left by a given distance.
        """
        self.get_moves([270, distance])

    def draw_square(self, size):
        """
        The scribe gets a set of moves that will trace a square
        """
        self.right(distance=size)
        self.down(distance=size)
        self.left(distance=size)
        self.up(distance=size)

    def forward_bounce(self, canvas, distance):
        """
        The scribe moves forward by a given distance along its current heading. It will bounce off of walls.
        """
        for d in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]

            wall_impact = canvas.hits_wall(pos)

            if not wall_impact[0] and not wall_impact[1]:
                pass
            elif wall_impact[0] and wall_impact[1]:
                self.bounce([-1, -1])
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            elif wall_impact[0]:
                self.bounce([-1, 1])
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            elif wall_impact[1]:
                self.bounce([1, -1])
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]

            self.draw(pos, canvas)
