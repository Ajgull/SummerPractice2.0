from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.ax.invert_yaxis()
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        self.ax.spines['left'].set_visible(True)
        self.ax.spines['top'].set_visible(True)

        self.ax.yaxis.set_ticks_position('left')
        self.ax.xaxis.set_ticks_position('top')

        self.ax.xaxis.set_label_position('top')
        self.ax.set_xlabel('V', fontsize=8)
        self.ax.set_ylabel('Z', fontsize=8)

        self.fig.subplots_adjust(left=0.25)
