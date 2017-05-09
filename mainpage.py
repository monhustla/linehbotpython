from flask import Flask, request
import json
import requests
app = Flask(__name__)
@app.route(‘/’)
def index ():
return “Hello World!”

@app.route(‘/callback’, methods=[‘POST’])
def callback ():
json_line = request.get_json ()
json_line = json.dumps(json_line)
decoded = json.loads(json_line)
user = decoded[“events”] [0] [‘replyToken’]
print (“ผู้ใช้：”, user)
sendText(user,’สวัสดี’)
return ‘’,200
def sendText(user, text):
LINE_API = ‘https://api.line.me/v2/bot/message/reply'
Authorization = ‘Bearer ENTER_ACCESS_TOKEN’ 
# ใส่ ENTER_ACCESS_TOKEN เข้าไป
headers = {
‘Content-Type’: ‘application/json; charset=UTF-8’,
‘Authorization’:Authorization
}
data = json.dumps({
“replyToken”:user,
“messages”: [{
“type”:”text”,
“text”:text
}]
})

r = requests.post (LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == ‘__main__’:
app.run(debug=True)
