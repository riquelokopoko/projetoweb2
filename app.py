from flask import Flask , render_template

app = Flask("Meu app")

posts =[
    {
        'texto':'texto'
    },
    {
        'texto':'texto'
    }
]

@app.route('/')
def exibir_entradas():
    entrada = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=[])