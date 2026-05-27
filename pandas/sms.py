# SMS
from twilio.rest import Client

account_sid = 'AC54b3d9cb566fa40c2866addc51d0b179'
auth_token = '15a0420c5eb0368dd4b781213cd75f83'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16592712764',
  body='Emergency! Help Please!',
  to='+917470983452'
)

print(message.sid)

# Sound
# import winsound
# winsound.Beep(2000, 1500)

# import folium

# world = folium.Map(location=[33.5969, 73.0528], zoom_start=2)

# # Add markers, popups, or other features to your map

# world.save("map.html")
