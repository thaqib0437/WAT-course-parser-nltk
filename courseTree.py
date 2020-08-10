import nltk

class parseTree(object):
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
    def get_trees(self):
        parser = nltk.ChartParser(self.grammar)
        TREES = []
        try:
            for tree in parser.parse(self.sentence):
                tree.pretty_print()
                tree.draw()
                TREES.append(tree)
        except ValueError:
            print(ValueError)
            print("Parsing not possible for specified grammar")
        return TREES

## A-> ATOM (Single requirment)
## BG -> Bracket Group
## B -> Bracket
## C -> Course
## I -> Infix operator
## Prefix operator

grammar = nltk.CFG.fromstring("""
    S -> BG | A | BG A | A BG | BG I BG | P BG BG | BG COM BG | A I BG | P A BG    
    BG -> B A B
    B -> "("|")"

    A -> CG I CG | P CG CG | I CG | CG I | P CG I CG | CG

    CG -> C COM N | C COM N COM N | C COM N COM N COM N | C | N
    COM -> ","
    C -> "math145"|"math147"|"cs135"|"pmath345" 
    N -> "135" | "145" | "147" | "101" | "345" | "346" | "347"
    I -> "or"|"and"|"/"
    P -> "one-of"|"all-of"
""")
sentence = input("Sentence: ").split()


# Real EX: (PMATH345 and 346) or 347

grammerString = """
S -> ROOT

ROOT -> BG OR BG | BG AND BG | OR BG BG | AND BG BG

BG -> B P B | P

B -> "("|")"

P -> CL AND CL | CL OR CL | OR CL CL| AND CL CL

AND -> "and"|"all-of"
OR -> "or"|"one-of"|"/"

CL -> C N | C N COM N | C N COM N COM N | C N COM N COM N COM N | C N COM N COM N COM N COM N  

COM -> ","
N -> "145"|"135"|"147"|"137"
C -> "math"|"cs" 
"""

grammar2 = nltk.CFG.fromstring(grammerString)

p = parseTree(grammar, sentence)
print(sentence)
T = p.get_trees()
print(T)
