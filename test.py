from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def return_files_tut():
    try:
         f = open("/home/azureuser/S2L/S2L-P3-API/Speak2Learn/log.txt", "r")
         content = f.read()
         f.close()
         return render_template("index.html", content=content, title="Sana")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2022, debug=True)
