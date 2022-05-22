import copy as cp

def prove_TD(kb,G):
    print(G)
    if not G:
        return 'yes.'
    else:
        a = G.pop(0)
        
        if a in kb['askables']:
            if ask(a):
                kb['rules'][a] = [[]]
                kb['askables'].remove(a)

        if a in kb['rules']:
            bodies = kb['rules'][a]

            for body in bodies:
                if prove_TD(kb,body + G) == 'yes.':
                    return 'yes.' 
        return f'Could not prove for {a}'

def prove_BU(kb):

    nkb = cp.deepcopy(kb)

    for askable in kb['askables']:
        if ask(askable):
            nkb['rules'][askable] = [[]]
    c = []
    added_atom = True

    while added_atom:
        added_atom = False

        for h in nkb['rules']:
            if h not in c:
                bodies = nkb['rules'][h]
                for body in bodies:
                    if set(body).issubset(set(c)):
                        c.append(h)
                        added_atom = True
                        break
    return c            

def ask(askable):
    ans = input(f'Is {askable} true?')
    return True if ans in ['sim','yes','y','s'] else False

def explain(observations, kb, explanation = set()):
    if observations:
        a = observations[0]

        if a in kb['assumables']:
            return explain(observations[1:],kb,explanation|{a})
        else:
            bodies = kb['rules'][a]
            explanations = []

            for body in bodies:
                explanations += explain(body + observations[1:],kb,explanation)

            return explanations
    return [explanation]

if __name__ == "__main__":
    
    kb = {  'rules':{   'a':[['b','c']],
                        'b':[['d'],['c']],
                        'e':[[]],
                        'd':[['h']],
                        'g':[['a','b','c']],
                        'f':[['h','b']]},
            'askables':['c','e'],
            'assumables':[] }

    kb = {  'rules':{   'bronchitis':[['influenza'],['smokes']],
                        'coughing':[['bronchitis']],
                        'wheezing':[['bronchitis']],
                        'fever':[['influenza'],['infection']],
                        'sore_throat':[['influenza']],
                        'False':[['smokes','non-smoker']]
                        },
            'askables':[],
            'assumables':['smokes','influenza','infection'] }


    print(explain(['False'],kb))