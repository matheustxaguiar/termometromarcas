class UsuarioObserver():
    def update(self, instancia):
        print("teste")
        if instancia.status=='desativado':
            print("usuario desativado")