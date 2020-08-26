from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apiKey}')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/66e421cd-c4aa-4c8d-8583-85c9b8c14563')

newVal = 0
sumVal = 0
equation = ""
while True:
    newVal = input("Enter a val or enter 0 to sum the values: ")
    if(newVal == '0'):
        break
    sumVal += int(newVal)
    equation += newVal + '+'
    print(equation)

with open('hello_world_ALLISON.ogg', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'The equation you entered was '+equation[:-1]+' and The sum of your values was '+str(sumVal),
            voice='en-US_AllisonVoice',
            accept='audio/ogg'        
        ).get_result().content)