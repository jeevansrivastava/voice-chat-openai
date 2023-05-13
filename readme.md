# OpenAiChatbot

This Python project contains a chatbot that simulates an interaction with OpenAI's GPT-3 language model. The user can speak to the bot via their microphone, and the bot will convert the audio to text using the Text-to-Speech (gTTS) library. The bot then uses GPT-3 to generate a response to the user's message and converts it to speech using Google's Text-to-Speech (gTTS) library. Finally, the bot plays the audio response using the gradio library.

## Dependencies

The following Python libraries are required to run this project:

- openai
- datetime
- gtts
- gradio
- playsound

The project also requires an OpenAI API key.

## Running the Chatbot

To run the chatbot, simply run the python bot function from the command line. The chatbot will prompt the user to ask a question or provide a command, and will respond with an appropriate answer or action. To stop the chatbot, the user can say "stop" or simply close the command line.
