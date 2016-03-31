__author__ = 'Veronica'

class View():
    def start(self):
        print 'EXPERIMENTO ELISA SIMULACAO\n\n'
        return self.menu()

    def menu(self):
        print "1 - Iniciar Simulacao"
        print "2 - Parar Simulacao"
        print "3 - Sair"

        return int(raw_input("\nDigite a opcao: "))

    def finalizar(self):
        print "Programa finalizado!"
