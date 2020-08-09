# WAT-course-parser-nltk
This is a helper lib for the project [watCoursePlanner](https://github.com/thaqib0437/watCoursePlanner). This help in parsing the course prerequsites based on a specified grammar. All the data to course details and prerequsites in the [db](db/) folder.

 All the python requirements are in [requirements.txt](requirements.txt)  


#### Example grammar:
```python 
grammar = nltk.CFG.fromstring("""
    S -> C I C | P C C
    
    C -> "math145"|"math147"|"cs135"
    I -> "or"|"and"
    P -> "one-of"|"all of"
""")
```
### Terminology
- S &#8594; The sentence
- C &#8594; Names of all courses in lowercase and without spaces
- I &#8594; Infix operator. *Ex: or, and* 
- P &#8594; Prefix operator. *Ex: one-of, all-of*

### Sample output
![ex1](img/ex1.png?raw=true "") 
```python
          S            
   _______|_______     
  P       C       C    
  |       |       |    
one-of math145 math147 
return value: [Tree('S', [Tree('P', ['one-of']), Tree('C', ['math145']), Tree('C', ['math147'])])]   
```
![ex2](img/ex2.png?raw=true "")
```python
         S
    _____|____
   C     I    C
   |     |    |
math145  or cs135

return value: [Tree('S', [Tree('C', ['math145']), Tree('I', ['or']), Tree('C', ['cs135'])])]
``` 
![ex3](img/ex3.png?raw=true "") 
```python

         S
    _____|_____
   C     I     C
   |     |     |
math145 and math147
return value: [Tree('S', [Tree('C', ['math145']), Tree('I', ['and']), Tree('C', ['math147'])])]

```

*note: this project is under construction*