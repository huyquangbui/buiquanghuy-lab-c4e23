from gmail import GMail, Message
import random

gmail = GMail("f.lampard263@gmail.com","tubqut-7nybny-cufzEf")

sickness_list = ["thuong han","tieu chay","kiet li"]

sickness = random.choice(sickness_list)

template = '''
<p>hey boss</p>
<p>kinda {{sick}} today. like a {{symptom}} on my chest.&nbsp;</p>
<p>have a nice day without your fav employee.</p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-wink.gif" alt="wink" /></p>
'''

symptom = "dau rang"
content = template.replace("{{sick}}",sickness).replace("{{symptom}}",symptom)

message = Message("Xin nghi lam", to="qhuydtvt@gmail.com", html=content)
gmail.send(message)