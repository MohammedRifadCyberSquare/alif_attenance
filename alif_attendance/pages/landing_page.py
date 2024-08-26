from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.dialog import MDDialog



class LandingPage(Screen):
    def update_time(self, *args):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.ids.time_label.text = f'Time: {current_time}'
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.ids.date_label.text = f'Date: {current_date}'

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.8, 0.2),
            auto_dismiss=True,
        )
        dialog.open()
    def on_enter(self):
        # Schedule the update_time function to be called every second
        Clock.schedule_interval(self.update_time, 1)

    def login(self):
        print(self.ids.username.text)
        if self.ids.username.text == "Rifad" and self.ids.password.text == "123":
            self.manager.current = 'admin_dashboard'
            print('success')

        else:
             MDSnackbar(
    MDSnackbarText(
        text="Single-line snackbar",
    ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()