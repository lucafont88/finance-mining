
class PlotModel:

    title: str
    x_label: str
    y_label: str
    x1: list
    y1: list
    label1: str
    x2: list
    y2: list
    label2: str

    def __init__(self, title: str, x_label: str, y_label: str, x1: list, y1: list, label1: str, x2: list, y2: list, label2: str):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x1 = x1
        self.y1 = y1
        self.label1 = label1
        self.x2 = x2
        self.y2 = y2
        self.label2 = label2