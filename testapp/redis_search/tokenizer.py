import re
import os
current_dir=os.getcwd()+"/"

f=open(current_dir+'stopwords.txt','r')
stopwords=set(f.read().split('\n'))
f.close()

def remove_special_char(text):
	return re.sub(r'[~!@#$%^&*()_+=-\[\]\\|\}\{;\":,/<>?]+',' ',text)

WORDS_RE=re.compile("[a-z]{2,}")
def tokenize(content):
	words=set()
	new_content=remove_special_char(content.lower())
	for match in WORDS_RE.finditer(new_content):
		word=match.group().strip(" ")
		if len(word)>=2:
			words.add(word)
	#return words
	return words-stopwords



'''def Main():
	a="A more negotiable instrument is a document guaranteeing the \
	payment of a specific amount of money, either on demand, or\
	 at a set time, with the payer named on the document More \
	 specifically, it is a document contemplated by or consisting\
	  of a contract, which promises the payment of money without\
	   condition, which may be paid either on demand or at a future \
	     	    date. the term can have different meanings, depending on what\
	     law is being applied and what country it is used in and what\
	      context it is used in.examples of negotiable instruments include promissory notes, \
	      bills of exchange, banknotes, and cheques.Because money is promised to be paid, the instrument \
	      itself can be used by the holder in due course as a store of\
	       value. The instrument may be transferred to a third party; \
	       it is the holder of the instrument who will ultimately get\
	        paid by the payer on the instrument. Transfers can happen \
	        at less than the face value of the instrument and this is known as \
	        discounting; this may happen for example if there is doubt about the \
	        payer's ability to pay.Due to the nature of the negotiable \
	        instrument as a store of value, most countries passed laws \
	        specifically related to negotiable instruments."

	print tokenizer(a)


if __name__=='__main__':
	Main()'''