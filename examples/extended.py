from guizero_autogrid import App, Auto, NextRow, PushButton

app = App(layout="grid", spacing=25)

b1 = PushButton(app, text="TEST 0.1")
b2 = PushButton(app, text="TEST 0.2")
b3 = PushButton(app, text="TEST 0.3")
b4 = PushButton(app, text="TEST 0.4")

b1 = PushButton(app, text="TEST 1.1", grid=NextRow)
b3 = PushButton(app, text="TEST 1.2")
b4 = PushButton(app, text="TEST 1.3")
b2 = PushButton(app, text="TEST 1.4", grid=[3, 3])

b1 = PushButton(app, text="TEST 2.1", grid=NextRow)
b3 = PushButton(app, text="TEST 2.2", grid=[Auto, Auto])
b4 = PushButton(app, text="TEST 2.3")
b2 = PushButton(app, text="TEST 2.4", grid=[4, 4])

b1 = PushButton(app, text="TEST 3.1", grid=NextRow)
b3 = PushButton(app, text="TEST 3.2")
b4 = PushButton(app, text="TEST 3.3")
b2 = PushButton(app, text="TEST 3.4")

app.display()
