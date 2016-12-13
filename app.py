import web
from web import form
from dataCliente import clientes
from dataPelicula import peliculas

render = web.template.render('views', base='base')

urls=(
    '/(.*)','index'
    )

db = web.database(dbn='mysql',db='peliculas',user='root',pw='1234')

clientes = clientes()
clientes.readCliente()
peliculas = peliculas()
peliculas.readPeliculas()

myformClientes= form.Form(
    form.Dropdown('Cliente', clientes.getCliente()),
    form.Dropdown('Pelicula', peliculas.getPelicula()),
    form.Dropdown('Formato',["Blueray","DVD"]),
    form.Dropdown('Tiempo',["1","2","3","4","5","6","7",",8","9"])
)

class index:
    def GET(self,results):
        form = myformClientes()
        results = db.select('renta')
        return render.index(form, results)

    def POST(self, results):
        form = myformClientes()
        if not form.validates():
            return render.index(form)
        else:
            costo=0
            if form.d.Formato=="Blueray":
                costo=20
            elif form.d.Formato=="DVD":
                costo=10
            total=int(form.d.Tiempo)*costo
            db.insert('renta',pelicula=form.d.Pelicula, formato=form.d.Formato,cliente=form.d.Cliente, tiempo=form.d.Tiempo,total=total)

            
            results=db.select('renta')
            return render.index(form,results)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()