import sys
from Licitacoes import Licitacoes

def main():
    licitacoes = Licitacoes()
    params = []

    for param in sys.argv:
        params.append(param)

    if params[1] == "1":
        licitacoes.load_licitacoes()
    elif params[1] == "2":
        licitacoes.plot_graphic()
    elif params[1] == "3":
        licitacoes.delete_data()   
    else:
        print("bad option")

if __name__ == "__main__":
  main()
