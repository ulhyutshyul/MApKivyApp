from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.garden.mapview import MapView
import geocoder

class MapApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Создаем виджет карты
        self.mapview = MapView(zoom=2, lat=0, lon=0)
        self.layout.add_widget(self.mapview)

        # Создаем кнопку для отображения текущего местоположения
        self.location_button = Button(text="Показать местоположение", size_hint=(1, 0.1))
        self.location_button.bind(on_press=self.show_location)
        self.layout.add_widget(self.location_button)

        return self.layout

    def get_location(self):
        location = geocoder.ip('me')
        return location.latlng if location else None

    def on_location(self):
        location = self.get_location()
        if location:
            lat, lon = location
            # Центрируем карту на текущем местоположении
            self.mapview.center_on(lat, lon)

    def show_location(self, instance):
        # Обновляем местоположение и центрируем карту
        self.on_location()


if __name__ == '__main__':
    MapApp().run()
