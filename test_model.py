# retreive model from tfhub
from google import genai
from film_simulation import *
client = genai.Client(api_key="AIzaSyB48j08Xi5rLdjix8NwV6CSe8ae6m0Vp58")

myfile = client.files.upload(file="./hq720.jpg")

response = client.models.generate_content(
    model="models/gemini-2.5-flash-preview-04-17",
    contents=[ myfile,  "You’re a colorist with task  to collect color from reference  image  and ."\
                   "clone  the color setting for using with other image"\
                   "Your task is to analyze the look of the image and create a concise, thoughtful  and complete  guide to reacreate the look."\
                   "Make sure to make the color curve at accurate as possible."\
                   
                   "Perform analysis based on the content of the image"\
                   "Focus more on skin tone if the image  genre are potrait"\
                   "Focus more sky, ground and color balance if image is landscape"\
                   "Get a little grain and chromatic abrration if the image in the style have grain and imperfection, grain size must be interger, inrange [0,2]"\
                   "Create a JSON LUT file for this image, with example below "\
                   "Create the JSON file and add the file to the response JUST OUTPUT THE JSON FILE "
                #    "Create a SIMPLE GUIDE TO CREATE THE COLOR IN LIGHTROOM "
                   "Example:"
                    '"Kodak Portra 400": {"'
                    '  "color_curves": {'
                    '   "R": {"x": [0, 0.25, 0.5, 0.75, 1], "y": [0, 0.27, 0.53, 0.77, 1]},'
                    '    "G": {"x": [0, 0.25, 0.5, 0.75, 1], "y": [0, 0.25, 0.5, 0.75, 1]},'
                    '    "B": {"x": [0, 0.25, 0.5, 0.75, 1], "y": [0, 0.23, 0.47, 0.73, 1]}'
                    '  },'
                    '  "contrast": 1.1,'
                    '  "saturation": 0.9,'
                    '  "chromatic_aberration": 0.2,'
                    '  "blur": 0.1,'
                    '  "base_color": [255, 250, 245],'
                    '  "grain_amount": 0.03,'
                    '  "grain_size": 1'
                    '}'])


print(response.text.replace("```json", "").replace("```", ""))

json_data = response.text.replace("```json", "").replace("```", "")
with open("temp_profile.json", "w+") as f:
    f.write(response.text.replace("```json", "").replace("```", ""))


process_args = []
film_profiles = load_film_profiles_from_json("./test.json")
for name, profile in film_profiles.items():
    process_image_func("./test_img.jpg",profile, 6500, False, "./output_temp.jpg")
# process_image(arg)
# inputs