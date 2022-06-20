import guizero

from guizero_autogrid.mixins import AutogridAppMixin, AutogridMixin


class App(AutogridAppMixin, guizero.App):
    pass


class Box(AutogridMixin, guizero.Box):
    pass


class ButtonGroup(AutogridMixin, guizero.ButtonGroup):
    pass


class CheckBox(AutogridMixin, guizero.CheckBox):
    pass


class Combo(AutogridMixin, guizero.Combo):
    pass


class Drawing(AutogridMixin, guizero.Drawing):
    pass


class ListBox(AutogridMixin, guizero.ListBox):
    pass


class MenuBar(AutogridMixin, guizero.MenuBar):
    pass


class Picture(AutogridMixin, guizero.Picture):
    pass


class PushButton(AutogridMixin, guizero.PushButton):
    pass


class RadioButton(AutogridMixin, guizero.RadioButton):
    pass


class Slider(AutogridMixin, guizero.Slider):
    pass


class Text(AutogridMixin, guizero.Text):
    pass


class TextBox(AutogridMixin, guizero.TextBox):
    pass


class TitleBox(AutogridMixin, guizero.TitleBox):
    pass


class Waffle(AutogridMixin, guizero.Waffle):
    pass


class Window(AutogridMixin, guizero.Window):
    pass
