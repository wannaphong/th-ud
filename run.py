import re
import codecs
def get_data():
	with codecs.open('orchid.pos', 'r',encoding='utf8') as f:
		lines = f.read()
	return re.split("TTTT",lines)
data=get_data()
i=0
data_all=[]
TAG_MAP = {
    #NOUN
    "NOUN":"NOUN",
    "NCMN":"NOUN",
    "NTTL":"NOUN",
    "CNIT":"NOUN",
    "CLTV":"NOUN",
    "CMTR":"NOUN",
    "CFQC":"NOUN",
    "CVBL":"NOUN",
    # VERB
    "VACT":"VERB",
    "VSTA":"VERB",
    #PRON
    "PRON":"PRON",
    "NPRP":"PRON",
    # ADJ
    "ADJ": "ADJ",
    "NONM": "ADJ",
    "VATT": "ADJ",
    "DONM": "ADJ",
    # ADV
    "ADV": "ADV",
    "ADVN": "ADV",
    "ADVI": "ADV",
    "ADVP": "ADV",
    "ADVS": "ADV",
	# INT
    "INT": "INTJ",
    # PRON
    "PROPN":"PROPN",
    "PPRS":"PROPN",
    "PDMN":"PROPN",
    "PNTR":"PROPN",
    # DET
    "DET": "DET",
    "DDAN": "DET",
    "DDAC": "DET",
    "DDBQ": "DET",
    "DDAQ": "DET",
    "DIAC": "DET",
    "DIBQ": "DET",
    "DIAQ": "DET",
    "DCNM": "DET",
    # NUM
    "NUM": "NUM",
    "NCNM": "NUM",
    "NLBL": "NUM",
    "DCNM": "NUM",
	# AUX
    "AUX": "AUX",
    "XVBM": "AUX",
    "XVAM": "AUX",
    "XVMM": "AUX",
    "XVBB": "AUX",
    "XVAE": "AUX",
	# ADP
    "ADP": "ADP",
    "RPRE": "ADP",
    # CCONJ
    "CCONJ":"CCONJ",
    "JCRG":"CCONJ",
	# SCONJ
    "SCONJ":"SCONJ",
    "PREL":"SCONJ",
    "JSBR":"SCONJ",
    "JCMP":"SCONJ",
    # PART
    "PART":"PART",
    "FIXN":"PART",
    "FIXV":"PART",
    "EAFF":"PART",
    "EITT":"PART",
    "AITT":"PART",
    "NEG":"PART",
    # PUNCT
    "PUNCT":"PUNCT",
    "PUNC":"PUNCT"
}
def c(w,tag):
	if w=="การ" or w=="ความ":
		return "NOUN"
	return tag
while i<len(data):
	data_list=[]
	for r in re.split('\n',data[i]):
		t=[x for x in re.split(' ',r) if x!='']
		if t!=[]:
			data_list.append((t[0],c(t[0],TAG_MAP[t[1]])))
	data_all.append(data_list)
	i+=1
train_data=[x for x in data_all if x!=[]]
with open("orchid-ud.pos","w",encoding="utf-8") as f:
	for i in train_data:
		for j in i:
			f.write(str(j[0])+"\t"+str(j[1])+"\n")
		f.write("\n")
