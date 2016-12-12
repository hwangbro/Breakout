import tkinter as tk
import breakout_model
import point

class BreakoutApplication:
    def __init__(self):
        self._state = breakout_model.BreakoutState()
        
        self._root_window = tk.Tk()
        
        self._canvas = tk.Canvas(
            master = self._root_window,
            width = 600, height = 600,
            background = 'black')

        self._canvas.grid(
            row = 0, column = 0,
            sticky = tk.N + tk.S + tk.E + tk.W)

        self._started = False

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas.bind('<Left>', self._move_left)
        self._canvas.bind('<Right>', self._move_right)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        self._root_window.after(40, self._next_frame)
        self._root_window.mainloop()

    def _move_left(self, event: tk.Event) -> None:
        print('moving left')

    def _move_right(self, event: tk.Event) -> None:
        print('moving right')

    def _next_frame(self) -> None:
        self._state.advance_frame()


        if self._state.game_over():
            self._draw_game_over_screen()

        else:
            self._draw_screen()
            self._root_window.after(40, self._next_frame)


    def _draw_game_over_screen(self) -> None:
        self._canvas.delete(tk.ALL)

        self._canvas.config(background = 'red')
        


    def _on_canvas_resized(self, event: tk.Event) -> None:
        self._draw_screen()

    def _on_canvas_clicked(self, event: tk.Event) -> None:
        if not self._started:
            self.start()
            self._started = True
        else:
            return

    def _draw_screen(self) -> None:
        self._canvas.delete(tk.ALL)
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        ball_center_x, ball_center_y = self._state.ball().center().frac()
        ball_radius = self._state.ball().radius()

        ball_tl_x = ball_center_x - ball_radius
        ball_tl_y = ball_center_y - ball_radius
        ball_tl = point.from_frac(ball_tl_x, ball_tl_y)
        ball_tl_px, ball_tl_py = ball_tl.pixel(width, height)
        
        ball_br_x = ball_center_x + ball_radius
        ball_br_y = ball_center_y + ball_radius
        ball_br = point.from_frac(ball_br_x, ball_br_y)
        ball_br_px, ball_br_py = ball_br.pixel(width, height)

        self._canvas.create_oval(
            ball_tl_px, ball_tl_py, ball_br_px, ball_br_py,
            fill = 'pink')

        
        

if __name__ == '__main__':
    BreakoutApplication()
