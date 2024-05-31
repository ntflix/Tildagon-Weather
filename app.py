import app

from .weather import FetchWeather
from events.input import Buttons, BUTTON_TYPES


class WeatherApp(app.App):
    text: str

    def __init__(self):
        self.button_states = Buttons(self)

        self.weather()

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.weather()
        elif self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()

    def draw(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.rgb(0, 1, 0).move_to(-95, 0).text(self.text)

    def try_connect(self):
        self.text = "Connecting to wifi"
        try:
            import wifi

            wifi.connect()
            self.text = "Connected to wifi"
        except ImportError as e:
            self.text = "Wifi failure"
            raise e

    def weather(self):
        self.text = "Fetching weather"
        weather = FetchWeather()
        self.text = weather.human_readable()


__app_export__ = WeatherApp
