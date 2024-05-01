import pywhatkit as pw

text='''calculator, youtube video downloader, voice assistant, digital clock, email sending, and Instagram bot generator are some of them.
WsCube Tech is here to help you with the learning and practicing as well, which will land you in a good company with a decent salary. After watching these good programming projects, your skills will definitely increase.
You will be more skilled and confident about the advanced Python projects that will give you opportunities to explore more. Watch this Python project full walk-through for beginners to advanced level, practice it at home and get perfect.
You can take the help of timestamps below for switching to any project from the top 20 Python projects within this video.
'''
pw.text_to_handwriting(text, "demo.png",[0,0,138])
print('Its done')