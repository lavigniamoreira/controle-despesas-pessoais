from flask import Flask

class FRC:
  #F: flask R: rota C: conteudo
    def create_app(self):
    app = Flask(__name__)
    self.app = app  
      self.rota()
    return app
  
  def conteudo(self):
    self.cntd = "Despesas pessoais"
    return(self.cntd)

  def rota(self):
    self.rt = self.app.add_url_rule(
            "/",
            view_func=self.conteudo
        )
    
frc_um = FRC()
