from guizero_autogrid.util import Auto, AutogridState, NextRow


class AutogridMixin:
    def __init__(self, master=None, *args, grid=None, spacing=None, **kwargs):
        grid = self._update_autogrid(master, grid, spacing)
        super().__init__(master, *args, grid=grid, **kwargs)

        if hasattr(master, "_autogrid"):
            self._apply_spacing(
                master._autogrid.spacing,
                padx=kwargs.get("padx"),
                pady=kwargs.get("pady"),
            )

    def _apply_spacing(self, spacing, padx=None, pady=None):
        spacing_x = spacing
        spacing_y = spacing
        if isinstance(spacing, (list, tuple)):
            spacing_x, spacing_y = spacing

        # if the widget already has padding, don't re-apply
        if padx is None:
            self.tk.config(padx=spacing_x)

        if pady is None:
            self.tk.config(pady=spacing_y)

    def _update_autogrid(self, parent, grid, spacing):
        if parent.layout == "grid":
            if not hasattr(parent, "_autogrid"):
                parent._autogrid = AutogridState(0, 0, spacing)

            c = parent._autogrid.current_col
            r = parent._autogrid.current_row
            sc = sr = 1
            if isinstance(grid, (tuple, list)):
                c = grid[0]
                r = grid[1]
                sc = grid[2] if len(grid) > 2 else 1
                sr = grid[3] if len(grid) > 3 else 1

            if grid is NextRow:
                c = 0
                r += 1
            elif isinstance(grid, (tuple, list)):
                if r == NextRow:
                    r = parent._autogrid.current_row + 1

                if Auto in grid:
                    c = parent._autogrid.current_col if c is Auto else c
                    r = parent._autogrid.current_row if r is Auto else r

            grid = (c, r, sc, sr)

            parent._autogrid.current_col = grid[0] + sc
            parent._autogrid.current_row = grid[1] + sr - 1

        return grid


class AutogridAppMixin:
    def __init__(self, *args, spacing=None, **kwargs):
        self._autogrid = AutogridState(0, 0, spacing)
        super().__init__(*args, **kwargs)
