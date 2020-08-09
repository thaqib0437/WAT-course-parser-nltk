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

grammar = nltk.CFG.fromstring("""
    S -> C I C | P C C
    
    C -> "math145"|"math147"|"cs135"
    I -> "or"|"and"
    P -> "one-of"|"all of"
""")
sentence = input("Sentence: ").split()

p = parseTree(grammar, sentence)
print(sentence)
T = p.get_trees()
print(T)