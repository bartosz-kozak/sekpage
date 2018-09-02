from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name = 'Strona domowa')

@app.route('/get_sek')
def get_sek():
    return render_template('get_sek.html', name = 'Podaj sekwencje')

@app.route('/sek_stat')
def sek_stat():
    seq = request.args.get('seq').upper()
    if '....' in seq:
        return render_template('error.html', name = 'Brak sekwencji')
    nuc_list = ['A', 'C', 'T', 'G']
    if any(x not in nuc_list for x in seq):
        return render_template('error1.html', name = 'Niedozwolone znaki')
    seq_len = len(seq)
    l=0
    for n in seq:
        if n == 'G' or n == 'C':
            l+=1
    cg = round(l/len(seq)*100,2)
    return render_template('sek_stat.html', name = 'Statystyki', seq_len = seq_len, cg = cg)




if __name__=='__main__':
    app.run(debug=True)
