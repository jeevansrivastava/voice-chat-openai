import gradio as gr
import random
import time

import os
import openai
from gtts import gTTS

openai.api_key=""

#   Global variable to hold the chat history, initialise with system role
conversation = [
        {"role": "system", "content": "Create a person named Alice who is a English Tutor, country of origin as India and act as this person. Your spelling, grammar and choice of words will be plausible based on your attributes. Your goal is to converse in english. Consider me as a 5 year old boy and I am here for general conversation. Make sure that your introduction should not exceed 50 words.","name":"David"}
        ]

def respond(audio, chat_history):
        
        #   Whisper API

        audio_file = open(audio, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)["text"]


        print(transcript)

    #   ChatGPT API

    #   append user's inut to conversation
        conversation.append({"role": "user", "content": transcript})
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
        )
        
        print(response)

    #   system_message is the response from ChatGPT API
        system_message = response["choices"][0]["message"]["content"]

    #   append ChatGPT response (assistant role) back to conversation
        conversation.append({"role": "assistant", "content": system_message})


    #   Text to speech
        tts = gTTS(text=system_message, lang='en')
        tts.save("response.mp3")
        os.rename(audio, audio + '.wav')
        chat_history.append(((audio+ '.wav',), ('response.mp3',)))

        return chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    mic = gr.Audio(source="microphone", type="filepath")
    mic.change(respond, [mic,chatbot], chatbot)
    
demo.launch()

