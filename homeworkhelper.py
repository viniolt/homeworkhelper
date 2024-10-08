import base64
import openai

openai.api_key = ""#YOUR OPENAI API KEY HERE
MODEL = "chatgpt-4o-latest" #SET THE GPT MODEL HERE

IMAGE_PATH = ("")#IMAGE PATH HERE (YOUR HOMEWORK, OR WHATEVER YOU WANT GPT TO READ)
def encode_image(image_path): #Decoding image
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(IMAGE_PATH)

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my homework!"}, #GPT's role
        {"role": "user", "content": [
            {"type": "text", "text": "Insert your prompt here. Example: Find the area of the triangle"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
             }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
