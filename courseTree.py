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
    S -> BG | A | BG A | A BG
    
    BG -> B A B
    B -> "("|")"

    A -> C I C | P C C | I C | C I

    C -> "math145"|"math147"|"cs135"
    I -> "or"|"and"
    P -> "one-of"|"all-of"
""")
sentence = input("Sentence: ").split()

p = parseTree(grammar, sentence)
print(sentence)
T = p.get_trees()
print(T)