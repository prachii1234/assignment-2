import json

nasa_apod_data = '''
{"copyright":"Gianni Tumino","date":"2024-07-05","explanation":"A glow from the summit of Mount Etna, famous active stratovolcano of planet Earth, stands out along the horizon in this mountain and night skyscape. Bands of diffuse light from congeries of innumerable stars along the Milky Way galaxy stretch across the sky above. In silhouette, the Milky Way's massive dust clouds are clumped along the galactic plane. But also familiar to northern skygazers are bright stars Deneb, Vega, and Altair, the Summer Triangle straddling dark nebulae and luminous star clouds poised over the volcanic peak. The deep combined exposures also reveal the light of active star forming regions along the Milky Way, echoing Etna's ruddy hue in the northern hemisphere summer's night.","hdurl":"https://apod.nasa.gov/apod/image/2407/GianniTumino_Etna&MW_14mm_JPG_LOGO__2048pix.jpg","media_type":"image","service_version":"v1","title":"Mount Etna Milky Way","url":"https://apod.nasa.gov/apod/image/2407/GianniTumino_Etna&MW_14mm_JPG_LOGO__1024pix.jpg"}
'''

data = json.loads(nasa_apod_data)

for key in ["explanation", "title"]:
    print(f"{key.capitalize()}: {data[key]}")