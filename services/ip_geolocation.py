import ipinfo
import folium
from dotenv import get_key

class IpGeolocation:

    def get_details(self, ip_address):
        """Get IP geolocation."""
        try:
            access_token = get_key('.env', 'IPINFO_TOKEN')
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip_address)
            return details.all
        except Exception as e:
            return False

    def draw_map(self, latitude, longitude, location):
        """Draw map."""
        filename = 'map.html'
        map = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker([latitude, longitude], popup=location).add_to(map)
        map.save('static/' + filename)
        return filename

    def map_ip_info(self, details):
        return {
            'Hostname': details.get('hostname'),
            'Organization': details.get('org'),
            'Country': f"{details.get('country_name')} ({details.get('country')})",
            'Region': details.get('region'),
            'City': details.get('city'),
            'Latitude': details.get('latitude'),
            'Longitude': details.get('longitude')
        }
