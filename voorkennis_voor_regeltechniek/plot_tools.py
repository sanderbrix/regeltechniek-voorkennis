import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import math
from fractions import Fraction

rcParams["axes.unicode_minus"] = False


def set_ax_formatter(ax, x={}, y={}):

    if "j" in y:
        if y["j"]:
            ax.yaxis.set_major_locator(plt.MultipleLocator(y["j"]))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(format_j))

    if "int" in x:
        if x["int"]:
            ax.xaxis.set_major_locator(plt.MultipleLocator(x["int"]))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_int))

    if "T" in x:
        if x["T"]:
            ax.xaxis.set_major_locator(plt.MultipleLocator(x["T"] / 2))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_T_factory(x["T"])))

    if "pi" in x:
        if x["pi"]:
            ax.xaxis.set_major_locator(plt.MultipleLocator(x["pi"] * np.pi))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_2pi))

    if "frac" in x:
        # if x["pi"]:
        #     ax.xaxis.set_major_locator(plt.MultipleLocator(x["pi"] * np.pi))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_frac))

    return ax


def format_2pi(value, tick_number):
    # find number of multiples of pi/2
    if value == 0:
        return "$0$"
    if value == np.pi:
        return "$\\pi $"

    # N = format_int(value / np.pi, tick_number)
    number = format_frac(value / np.pi, tick_number, no_dollars=True)
    return f"${number} \\pi $"


def format_frac(value, tick_number, no_dollars=False):
    if value == 0:
        return "0"

    whole_number = format_int(value // 1, tick_number)
    frac = Fraction(value - whole_number).limit_denominator()

    whole_number = str(whole_number) if whole_number > 0 else ""
    frac = (
        f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
        if frac.numerator > 0
        else ""
    )
    if no_dollars:
        return f"{whole_number}{frac}"
    else:
        return f"${whole_number}{frac}$"


def format_T_factory(T):
    def format_T(value, tick_number):
        # find number of multiples of pi/2
        if value == 0:
            return "$0$"

        N = format_int(value / T, tick_number)
        return f"${N}T$"

    return format_T


def format_j(value, tick_number):
    value = format_int(value, tick_number)

    if value == 0:
        return "0"
    else:
        return f"${value}j$"


def format_int(value, tick_number):

    if not (value % 1):
        return int(value)

    else:
        return value


# class Complex_Number_list:

#     def __init__(self, number_list):
#         self.numbers = []
#         for number in number_list:
#             self.numbers.append()


# class Complex_Number:
#     def __init__(self, z, label, ax=None, plot_angle_arc=False):
#         self.z = z
#         self.label = label
#         self.plot_angle_arc = plot_angle_ard
#         self.ensure_ax(ax)

#     def ensure_ax(self, ax):
#         if not ax:
#             self.fig, self.ax = create_complex_plane()
#         else:
#             self.fig, self.ax = (ax.get_figure(), ax)

#     def plot(self):
#         self.ax.scatter(self.z.real, self.z.imag, marker="x", zorder=10, label=f"${self.label}$")
#         self.ax.legend()


def center_spines(ax, yaxis=True):

    # ax.spines["bottom"].set_position(("data", 0))
    if yaxis:
        # ax.spines["left"].set_position(("data", 0))
        ax.spines["right"].set_linewidth(1.5)
        ax.xaxis.set_tick_params(
            which="both", top=True, bottom=False, labeltop=False, labelbottom=True
        )
    else:
        ax.spines["left"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.xaxis.set_tick_params(
            which="both", top=True, bottom=False, labeltop=True, labelbottom=False
        )
    # ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("axes", 0))
    # ax.xaxis.set_tick_params(bottom='on', top='on')
    # ax.xaxis.set_tick_params(pad=-11)

    ax.spines["right"].set_position(("data", 0))
    ax.spines["bottom"].set_linewidth(0)
    ax.spines["top"].set_linewidth(1.5)
    ax.yaxis.set_tick_params(pad=20)
    ax.yaxis.set_tick_params(
        which="both", left=False, labelleft=True, right="on", pad=0
    )
    ax.spines["left"].set_position(("axes", 0))
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_position(("data", 0))

    return ax


def create_number_line_and_complex():
    fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(9, 5), dpi=300)
    fig0, ax0 = create_number_line(ax=axs[0])
    fig1, ax1 = create_complex_plane(ax=axs[1])
    return fig, axs


def create_complex_plane(ax=None):
    if not ax:
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    else:
        fig = ax.get_figure()

    circle1 = plt.Circle((0, 0), 1, zorder=5, ec="k", lw=0.4, fc="none")
    ax.add_patch(circle1)
    ax.grid(True, which="both", lw=0.25, zorder=-10)
    # ax.minorticks_on()

    ax.set_aspect("equal", adjustable="box")

    print(ax.get_xticks())
    print(ax.get_yticks())

    ax.tick_params(length=4, width=1.5)
    ax.tick_params(which="minor", length=2.5, width=0.6)

    ax = set_ax_formatter(ax, x={"int": 0}, y={"j": 0})
    ax = center_spines(ax)

    return fig, ax


def create_number_line(ax=None):
    if not ax:
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    else:
        fig = ax.get_figure()
    # ax.grid(True, which="both", lw=0.25, zorder=-10)
    ax.minorticks_on()

    ax.set_yticks([])
    ax.tick_params(length=4, width=1.5)
    ax.tick_params(which="minor", length=2.5, width=0.6)
    ax = center_spines(ax, yaxis=False)

    return fig, ax


def create_time_plot(ax=None, x_format={}):
    if not ax:
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    else:
        fig = ax.get_figure()

    if x_format:
        ax = set_ax_formatter(ax, x=x_format)

    return fig, ax


def plot_complex(
    z,
    z_label,
    ax=None,
    fig=None,
    plot_arc=False,
    xkcd=False,
    xtick_sep=None,
    ytick_sep=None,
):
    if not ax:
        fig, ax = create_complex_plane()

    if xkcd:
        with plt.xkcd():
            point = ax.scatter(
                z.real, z.imag, marker="x", zorder=10, label=f"${z_label}$"
            )
    else:
        point = ax.scatter(z.real, z.imag, marker="x", zorder=10, label=f"${z_label}$")
        fc = point.get_facecolor()

    if plot_arc:
        xtick = 2 if z.imag > 0 else 3
        ytick = 0 if z.real < 0 else 1
        dashx = ax.scatter(z.real, 0, marker=xtick, fc=fc, zorder=10, label=None)

        dashy = ax.scatter(0, z.imag, marker=ytick, fc=fc, zorder=10, label=None)
        if np.angle(z) > 0:
            angles = np.arange(0, np.angle(z), np.pi / 50)
        else:
            angles = np.arange(np.angle(z), 0, np.pi / 50)
        r = np.abs(z) / 5
        xs, ys = (r * np.cos(angles), r * np.sin(angles))
        ax.plot(xs, ys, "-", color=fc[0], lw=0.4)

    if plot_arc:
        ax.plot([z.real, z.real], [0, z.imag], "k:", lw=0.5, color=fc[0])
        ax.plot([0, z.real], [z.imag, z.imag], "k:", lw=0.5, color=fc[0])
        ax.plot([0, z.real], [0, z.imag], "k:", lw=0.5)

    ax.legend()

    return fig, ax, point

class TimePlot:
    def __init__(self, t, y, label=None):
        self.t, self.y, self.label = (t, y, label)


    def plot(self, ax=None, x_format={}, **kwargs):

        # if not ax:
        #     fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        # else:
        #     fig = ax.get_figure()
        if not ax: 
            fig, ax = create_time_plot(x_format=x_format)

        if not "color" in kwargs:
            kwargs["color"] = next(ax._get_lines.prop_cycler)["color"]

        ax = center_spines(ax)
        label_tex = f"${self.label} \\ $" if self.label else None
        line = ax.plot(self.t, self.y, label=label_tex, **kwargs)

        ax.grid(True)
        ax.set_xlabel("$t$")

        return fig, ax, line



# def time_plot(t, y, ax=None, label=None, **kwargs):
#     if not ax:
#         fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
#     else:
#         fig = ax.get_figure()

#     if not "color" in kwargs:
#         kwargs["color"] = next(ax._get_lines.prop_cycler)["color"]

#     ax = center_spines(ax)
#     label_tex = f"${label} \\ $" if label else None
#     line = ax.plot(t, y, label=label_tex, **kwargs)

#     ax.grid(True)
#     ax.set_xlabel("$t$")

#     return fig, ax, line


if __name__ == "__main__":
    # z = 5 + 2j

    modes = ["time", "complex"]

    # plot_complex(z, "z")
    # plt.show()
    if "complex" in modes:
        fig, axs = create_number_line_and_complex()

        axs[0].scatter(-1, 0, marker="x", label="a=-1")
        axs[0].scatter(2, 0, marker="x", label="b=2")
        axs[0].legend()
        z = 1 + 1j
        plot_complex(z, f"z_1", ax=axs[1], plot_arc=True)

        z = -1 + 0.5j
        plot_complex(z, f"z_2", ax=axs[1], plot_arc=True, xtick_sep=2, ytick_sep=3)
        plot_complex(
            z.conjugate(),
            f"\\bar{{z}}_2",
            ax=axs[1],
            plot_arc=True,
            xtick_sep=1,
            ytick_sep=1.5,
        )

    if "time" in modes:
        N_periods = 1
        t = np.arange(0, N_periods * 2 * np.pi, 0.01)
        a = -0.2
        omega = 1
        phase_diff = -np.pi / omega


        yexp = np.exp(a * t)
        ycos = np.cos(omega * t)
        ycosd = np.cos(omega * t - phase_diff)
        ysin = np.sin(omega * t)

        fig, ax, line = TimePlot(t, yexp, f"y_0(t) = \\exp({a} t) \\cdot cos({omega}t) ").plot(x_format={"pi": 0.25})
        fig, ax, line = TimePlot(t, yexp * ycos).plot(ax)
        fig, ax, line = TimePlot(t, yexp * ysin).plot(ax)
        fig, ax, line = TimePlot(t, yexp * ycosd).plot(ax)


        fig, ax = create_time_plot(x_format={"pi": 0.25})

        # fig, ax, line = time_plot(
        #     t,
        #     yexp * ycos,
        #     label=f"y_0(t) = \\exp({a} t) \\cdot cos({omega}t) ",
        #     ax=ax,
        #     ls="-",
        # )
        # fig, ax, line = time_plot(
        #     t,
        #     yexp * ysin,
        #     label=f"y_1(t) = \\exp({a} t) \\cdot sin({omega}t) ",
        #     ls="--",
        #     ax=ax,
        # )
        # fig, ax, line = time_plot(
        #     t,
        #     yexp * ycosd,
        #     label=f"y_2(t) = \\exp({a} t) \\cdot sin({omega}t - {phase_diff/np.pi} \\pi) ",
        #     ls="--",
        #     ax=ax,
        # )
        # fig, ax, line = time_plot(t, yexp, ls=":", color="k", ax=ax)
        # fig, ax, line = time_plot(t, -yexp, ls=":", color="k", ax=ax)
        fig.legend()

    plt.show()
