from flask import Flask, render_template, request
from groq import Groq
from datetime import datetime


app = Flask(__name__)

ai_key = "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"

user = Groq(api_key=ai_key)

def panggil_ai(tahun):
    try:
        pesan = user.chat.completions.create(
             messages=[
                {
                    "role": "user",
                    "content": f"Berikan saya satu fakta menarik seputar teknologi di tahun {tahun} menggunakan bahasa indonesia",
                }
            ],
            model="llama3-8b-8192",
            stream=False,
        )
        output_ai = pesan.choices[0].message.content
        return output_ai
    except Exception:
        return "mohon maaf, ai sekarang sedang sibuk"

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/usia', methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        tahun = request.form['tahun_lahir']
        tahun1 = int(tahun)
        usia = datetime.now().year - tahun1
        output_ai = panggil_ai(tahun)
        return render_template('cek_usia.html', usia=usia, output_ai=output_ai)
    return render_template('cek_usia.html', usia=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)