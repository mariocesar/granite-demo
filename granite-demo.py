from gi.repository import Gtk, Gio
from gi.repository import Granite

class LLabel (Gtk.Label):
    def __init__(self, label):
        self.label = label
        self.halign = Gtk.Align.START


class GraniteDemo(Granite.Application):

    def do_activate(self):
        self.window = Gtk.Window()
        self.window.set_title('Granite Demo')
        self.window.set_position(Gtk.WindowPosition.CENTER)

        self.add_window(self.window)

        self.window.set_default_size(800, 550)
        self.window.show_all()
        self.show_light_window()

    def show_light_window(self):

        # TODO: New method is possible not the correct API conventional use
        light_window = Granite.WidgetsLightWindow.new("Light Window")
        light_window_notebook = Granite.WidgetsStaticNotebook.new("Notebook")

        entry = Gtk.Entry()
        open_drop = Gtk.ComboBoxText()
        open_label = LLabel("Alwas Open Mpeg Video Files with Audience")

        grid = Gtk.Grid()
        grid.attach (entry, 1, 0, 1, 1)
        grid.attach (LLabel ("1.13 GB, Mpeg Video File"), 1, 1, 1, 1)
        grid.attach (light_window_notebook, 0, 2, 2, 1)

        general = Gtk.Grid ()
        
        general.attach(LLabel("<b>Info:</b>"), 0, 0, 2, 1)
        general.attach(LLabel("Created:"), 0, 1, 1, 1)
        general.attach(LLabel("Modified:"), 0, 2, 1, 1)
        general.attach(LLabel("Opened:"), 0, 3, 1, 1)
        general.attach(LLabel("Mimetype:"), 0, 4, 1, 1)
        general.attach(LLabel("Location:"), 0, 5, 1, 1)

        general.attach(LLabel("Tobday at 9:50 PM"), 1, 1, 1, 1)
        general.attach(LLabel("Today at 9:50 PM"), 1, 2, 1, 1)
        general.attach(LLabel("Today at 10:00 PM"), 1, 3, 1, 1)
        general.attach(LLabel("video/mpeg"), 1, 4, 1, 1)
        general.attach(LLabel("/home/daniel/Downloads"), 1, 5, 1, 1)
        
        general.attach(LLabel("<b>Open with:</b>"), 0, 6, 2, 1)
        general.attach(open_drop, 0, 7, 2, 1)
        general.attach(open_label, 0, 8, 2, 1)

        light_window_notebook.append_page(general, Gtk.Label("General"))
        light_window_notebook.append_page(Gtk.Label("More"), Gtk.Label("More"))
        light_window_notebook.append_page(Gtk.Label("Sharing"), Gtk.Label("Sharing"))
        
        light_window.add(grid)
        light_window.show_all()


if __name__ == '__main__':
    application = GraniteDemo()
    application.run("granite-demo", Gio.ApplicationFlags.FLAGS_NONE)