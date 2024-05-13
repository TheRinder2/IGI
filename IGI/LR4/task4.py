import matplotlib.pyplot as plt
from entities import Figure, IsoscelesRhomb
from input import valid_type
from decorators import try_again_decorator


def input_data():
    '''Inputs and validates trapezoid parameters.'''

    a = valid_type('Enter a: ', 'float')
    r = valid_type('\tr: ', 'float')
    color = input('\tcolor: ')
    name = input('\tname: ')
    return a, r, color, name


class FigureActions:
    def __init__(self, figure: Figure):
        self.figure = figure

    def plot_figure(self, x0=0, y0=0):
        '''Plots polygon using matplotlib.'''

        fig = plt.figure()
        points = self.figure.get_vertexes(x0, y0)

        ax = fig.add_subplot()
        ax.set_xlim(min([point[0] for point in points]) - 1, max([point[0] for point in points]) + 1)
        ax.set_ylim(min([point[1] for point in points]) - 1, max([point[1] for point in points]) + 1)
        ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

        try:
            polygon = plt.Polygon(points,  fill=True, color=self.figure.get_color().color)
        except:
            print("Color not found")
            raise ValueError

        ax.add_patch(polygon)

        return fig

    def show_figure(self, figure):
        '''Show passed figure.'''

        figure.savefig(f'{self.figure.get_name()}.png', dpi=90, bbox_inches='tight')
        plt.title(self.figure.get_name())
        plt.show()


@try_again_decorator
def task4():
    '''Creates trapezoid by given data, plots this figure and saves result in file.'''

    a, r, color, name = input_data()

    rhomb = IsoscelesRhomb(name, color, a, r)

    try:
        worker = FigureActions(rhomb)
        worker.show_figure(worker.plot_figure())
        print(f'Builded rhomb: {rhomb}')
    except ValueError:
        pass


