#In[]
Essen={}
Essen['Schinken']='Ja'
Essen['Eier']='Nein'
Essen['Pommes']='Jau'
Essen['HF']='72106'
Essen['Eier']
Essen['Pommes']
print (Essen)
print(Essen['Pommes'])
# %%
print (Essen['HF'])


en_de={'red':'rot', 'green':'grün', 'blue':'blau','Yellow':'gelb'}
print(en_de)
print(en_de['blue'])
de_fr={'rot':'rouge', 'grau':'greey', 'grün':'vert', 'blau':'bleu', 'gelb':'jaune'}
print(de_fr)
print(de_fr['blau'])
print ('Englisch-Franz')
print('von_dem ersten diktionary ins zweite geschaut')
print(de_fr[en_de['green']])
x='blue'
z=en_de['blue']
y=de_fr[en_de['blue']]
print('auf Englisch:{}, auf französisch{}'.format(z,y))