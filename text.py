import gradio as gr
from gtts import gTTS

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    filename = "hello_mp3.mp3"
    tts.save(filename)
    return filename

demo = gr.Interface(
    fn=text_to_speech,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Audio(type="filepath"),
    title="Text to Speech"
)

demo.launch(share=True)