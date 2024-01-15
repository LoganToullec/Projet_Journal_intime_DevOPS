import sys
import argparse
import IMCInterpretor

def calculer_imc(poids, taille):
    try:
        imc = poids / (taille/100)**2
        return round(imc,1)
    except ZeroDivisionError:
        return None

def main():
    parser = argparse.ArgumentParser(description="Calculer l'IMC à partir du poids et de la taille.")
    parser.add_argument("poids", type=float, help="Poids en kilogrammes")
    parser.add_argument("taille", type=float, help="Taille en centimètres")
    args = parser.parse_args()

    imc = calculer_imc(args.poids, args.taille)
    print(imc)
    if imc is not None:
        interpretation = IMCInterpretor.interpreter_imc(imc)
        print(f"Pour un IMC de {imc:.2f}, la catégorie est: {interpretation}")
    else:
        print("Erreur lors du calcul de l'IMC.")
        sys.exit(1)

if __name__ == "__main__":
    main()