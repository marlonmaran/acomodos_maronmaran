import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='Ir a la segunda ventana', on_release=self.switch_to_second)
        button2 = Button(text='Ir a la tercera ventana', on_release=self.switch_to_third)
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def switch_to_second(self, *args):
        self.manager.current = 'second'

    def switch_to_third(self, *args):
        self.manager.current = 'third'


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        wm = WindowManager()
        wm.add_widget(MainWindow(name='main'))
        wm.add_widget(SecondWindow(name='second'))
        wm.add_widget(ThirdWindow(name='third'))
        return wm


if __name__ == '__main__':
    MyApp().run()