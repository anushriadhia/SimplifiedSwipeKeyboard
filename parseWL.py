import sys

def main():

	wordList = open("wordList.txt",'r');

	newWordList = open("newWL.txt", 'w');

	newWordList.write("var wordList = [");

	for line in wordList:
		newWordList.write('"'+ line.strip()+'", ');


	newWordList.write("];");

	wordList.close();
	newWordList.close();

	print "done"

main()








	
