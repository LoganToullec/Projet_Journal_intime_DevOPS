import sys

def interpreter_imc(imc):
    if imc < 18.5:
        return "Insuffisance pondérale (maigreur)"
    elif 18.5 <= imc < 24.9:
        return "Poids normal"
    elif 24.9 <= imc < 29.9:
        return "Surpoids"
    else:
        return "Obésité"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script2.py [IMC]")
        sys.exit(1)

    imc = float(sys.argv[1])
    interpretation = interpreter_imc(imc)
    print(f"Pour un IMC de {imc:.2f}, la catégorie est: {interpretation}")

if __name__ == "__main__":
    main()