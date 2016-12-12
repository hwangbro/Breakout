import point

class Ball:
    def __init__(self):
        self._center = point.from_frac(0.5, 0.5)
        self._radius = 0.01

        self._xdelta = 0.012
        self._ydelta = -0.006
        self._off_board = False
        
    def center(self) -> point.Point:
        return self._center

    def radius(self) -> float:
        return self._radius

    def move(self) -> None:
        cx, cy = self._center.frac()

        cx += self._xdelta
        cy += self._ydelta


        if cx + self._radius > 1.0 or cx - self._radius < 0.0:
            self._xdelta *= -1

        if cy + self._radius < 0.0:
            self._ydelta *= -1

        if cy - self._radius > 1.0:
            self._off_board = True


        self._center = point.from_frac(cx, cy)

    def off_board(self) -> bool:
        return self._off_board

class Paddle:
    def __init__(self):
        self._center = point.from_frac(0.5, 0.98)
        self._x_radius = 0.05
        self._y_radius = 0.005

        self._xdelta = 0.01

    def center(self) -> point.Point:
        return self._center

    def x_radius(self) -> float:
        return self._x_radius

    def yradius(self) -> float:
        return self._y_radius

    def move_left(self) -> None:
        cx, cy = self._center.frac()
        if self._is_at_edge():
            return
        else:
            cx -= self._xdelta
            self._center = point.from_frac(cx, cy)

    def move_right(self) -> None:
        cx, cy = self._center.frac()
        if self._is_at_edge():
            return
        else:
            cx += self._xdelta
            self._center = point.from_frac(cx, cy)
            
    def _is_at_edge(self) -> bool:
        cx = self._center.frac()[0]
        return (cx + radius == 1) or (cx - radius == 1)
        



class BreakoutState:
    def __init__(self):
        self._ball = Ball()
        self._paddle = Paddle()
        self._move_left = False
        self._move_right = False


    def ball(self) -> Ball:
        return self._ball

    def paddle(self) -> Paddle:
        return self._paddle

    def advance_frame(self) -> None:
        self._ball.move()
        if self._move_left:
            self._paddle.move_left()
        elif self._move_right:
            self._paddle.move_right()
            

    def game_over(self) -> bool:
        return self._ball.off_board()

    
