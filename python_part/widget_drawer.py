from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent: object = None, width: int = 10, height: int = 5, dpi: int = 100) -> None:
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)

        self.ax.invert_yaxis()

        # скрываем нижнюю ось x и правую границу
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # левые и верхние границы видимы
        self.ax.spines['left'].set_visible(True)
        self.ax.spines['top'].set_visible(True)

        self.ax.yaxis.set_ticks_position('left')  # Ось y слева

        # дополнительная ось сверху
        self.ax_top = self.ax.twiny()

        # Настраиваем верхнюю ось
        self.ax_top.spines['top'].set_visible(True)
        self.ax_top.spines['bottom'].set_visible(False)

        # скрываем правую границу верхней оси дополнительной оси
        self.ax_top.spines['right'].set_visible(False)
        self.ax_top.yaxis.set_ticks_position('left')

        self.ax_top.xaxis.set_ticks_position('top')
        self.ax_top.xaxis.set_label_position('top')
        self.ax_top.set_xlabel('V, Ом · м', fontsize=8)

        # Скрываем нижнюю ось x основной оси
        self.ax.xaxis.set_visible(False)

        self.ax.set_ylabel('Z, м', fontsize=8)

        self.fig.subplots_adjust(left=0.25, top=0.89)
