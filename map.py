import sys
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout#pip install PyQt5
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import openrouteservice

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QuickRoute')
        self.window_width, self.window_height = 1600, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)
        client =openrouteservice.Client(key="5b3ce3597851110001cf62481c012148def84c72bd979bba50d42b29")
        map = folium.Map(location = [19.004506312976766, 72.90108739421363], zoom_start= 17)
        a = [[19.004855620660692, 72.89477603506968],[19.00519037316952, 72.90016378068037],[19.002992637871028, 72.89833194717272],
            [19.004477203969998, 72.90422768022673],[19.002133912217243, 72.9045201578456],[19.000925866929954, 72.90498196461222]]


        #c = [[72.89477603506968,19.004855620660692],[72.9045201578456,19.002133912217243]]
        folium.Marker(location=a[0],popup="A").add_to(map)
        folium.Marker(location=a[1],popup="B").add_to(map)
        folium.Marker(location=a[2],popup="C").add_to(map)
        folium.Marker(location=a[3],popup="D").add_to(map)
        folium.Marker(location=a[4],popup="E").add_to(map)
        folium.Marker(location=a[5],popup="F").add_to(map)
        
        i = int(input("Starting point \n A = 0 | B = 1 | C = 2 | D = 3 | E = 4 | F = 5 \n User Input  :   "))
        j = int(input("Ending point \n A = 0 | B = 1 | C = 2 | D = 3 | E = 4 | F = 5 \n User Input  :   "))
        c = [a[i][::-1],a[j][::-1]]

        folium.Marker(location=a[i]).add_to(map)
        folium.Marker(location=a[j]).add_to(map)

        route = client.directions(coordinates=c,profile='driving-car',format='geojson')
        folium.GeoJson(route , name = "route").add_to(map)
        # save map data to data object
        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')