from gmail import GMail, Message
import datetime
import random

now = datetime.datetime.now().strftime("%R")

gmail = GMail("f.lampard263@gmail.com","tubqut-7nybny-cufzEf")

sickness_list = ["sick","tired","exhausted"]

sickness = random.choice(sickness_list)

template = '''
<p>hey boss</p>
<p>kinda {{sick}} today. like a {{symptom}} on my chest.&nbsp;</p>
<p>have a nice day without your fav employee.</p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-wink.gif" alt="wink" /></p>
'''

symptom = "hammer"
content = template.replace("{{sick}}",sickness).replace("{{symptom}}",symptom)

message = Message("Xin nghi lam", to="qhuydtvt@gmail.com", html=content)

while True:
    if  now == "07:00":  # at 7AM 
        gmail.send(message)