from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, Mahlon!'

def hi():
  return "How are you, my brother"
  
app.run(host='0.0.0.0', port=8080)
