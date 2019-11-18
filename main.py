from flask import Flask , request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

s_text=''

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>

    <body>
    <form method="POST">
      Rotate by <input type="text" name="rot"/ value="0"> <br>
      <textarea name="text" value=''> {0} </textarea> <br> 
      <input type=submit value="Submit Query"/>
    </form>
    </body>

</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
   
    text_rot=int(request.form["rot"])
    
    text_move=request.form["text"]
    s_text=rotate_string(text_move,text_rot)
    return form.format(s_text)


@app.route("/")
def index():
    return form.format(' ')

app.run()