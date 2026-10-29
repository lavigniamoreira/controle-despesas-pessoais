from flask import Flask

class FRC:
  #F: flask R: rota C: conteudo
    def create_app(self):
    app = Flask(__name__)
    self.app = app  
      self.rota()
    return app
  
  def conteudo():
    return("Despesas pessoais")

  def rota():
    conteudo()
    self.app.add_url_rule(
            "/",
            view_func=self.conteudo
        )
