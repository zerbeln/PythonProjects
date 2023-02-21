from canvases.canvas import Canvas
import threading


class AxesCanvas(Canvas):
    def construct_function_plot(self):
        scribe_threads = [threading.Thread(target=self.make_plots, args=(sc,)) for sc in self.scribes]
        [t.start() for t in scribe_threads]
        [t.join() for t in scribe_threads]

    def make_plots(self, scribe):
        for x in range(self._x):
            pos = scribe.plot_function(x, self)
            scribe.draw(pos, self)

    def format_axis_number(self, num):
        if num % 5 != 0:
            return '  '
        if num < 10:
            return ' ' + str(num)
        return str(num)

    def print(self):
        self.clear()
        for y in range(self._y):
            print(self.format_axis_number(y) + ' '.join([col[y] for col in self._canvas]))

        print(' '.join([self.format_axis_number(x) for x in range(self._x)]))
