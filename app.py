from flask import Flask

app = Flask(__name__)

def checkDNA(functie):
    def wrapper(dna):
        for nuc in range (0,len(dna)):
            if dna[nuc].lower() != "a" or dna[nuc].lower != "t" or dna[nuc].lower != "g" or dna[nuc].lower != "c":
                print("sequentie is geen DNA")
                return
        else:
            functie(dna)
    return wrapper

@app.route('/')

@checkDNA
def dnaToRna(dna):
    return dna.replace('t','u').replace('T','U')


if __name__ == '__main__':
    app.run()
