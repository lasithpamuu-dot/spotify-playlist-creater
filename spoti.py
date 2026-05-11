import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os



load_dotenv()
class weather:
    def location(self,city):
        API_KEY= "a557b3fc5b3c4730ad165208260305"
        url= f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        response=requests.get(url)
        data=response.json()
        return data["current"]["condition"]["text"]
class qumood:
    def moodclassifier(self,weather,energy,mood):
        return {"weather" : weather,
                "energy"  : energy,
                "mood"    : mood}
class finalreport:
    def quearyready(self,weather,moods):
        condition=weather
        feeling=moods['mood'].lower()
        energy=moods['energy'].lower()
        

        if "cloud" in condition and energy =="low" and feeling=="stressed":
            return "chill"
        elif "sunny" in condition or "cloud" in condition and energy =="high":
            return "energetic"
        elif feeling=="stressed":
            return "focus"
        elif feeling=="sad":
            return "melanchcholic"
        else:
            return "neutral"
class querysender:
    def query(self,final,weather):
        if "cloud" in weather and final=="chill":
            return "lofi chill rain ambient soft beats"
        elif "sunny" in weather and final=="energetic":
            return "upbeat pop energetic dance summer vibes"
        elif final=="stressed":
            return "focus study music instrumental concentration soft electronic"
        else:
            return "soft chill pop relaxed everyday listening"
class spotifycls:
    
    def __init__(self):

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret= os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri="http://127.0.0.1:8888/callback",
                scope="user-read-private"
            )
        )

    def search_tracks(self, query):

        results = self.sp.search(
            q=query,
            type="track",
            limit=5
        )

        songs = []

        for item in results["tracks"]["items"]:
            

            song_data = {
                "\nname": item["name"],
                "\nartist": item["artists"][0]["name"],
                "\nlink"  : item["external_urls"]["spotify"],
                
            }

            songs.append(song_data)

        return songs

        


        


weath=weather()
query_final=querysender()
qm=qumood()
final=finalreport()
spotify=spotifycls()
city=input("enter your city : ")
weather_condition=weath.location(city)
print(weather_condition)
weather_reaction=input("how do you feel about the weather now(like/dislike/nuetral) : ")
eneragy_input=input("whats your energy level right now(low/medium/high) : ")
print("1. HAPPY\n2.SAD\n3.STRESSED\n4.CALM\n5.BORED")
mood_input=input("which is best to describe your mood right now : ")
qm_data=qm.moodclassifier(weather_reaction,eneragy_input,mood_input)
final_report_for_query=final.quearyready(weather_condition,qm_data)
final_sender=query_final.query(final_report_for_query,weather_condition)
print(final_sender)
songs = spotify.search_tracks(final_sender)

print(songs)






