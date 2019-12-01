lMarginIn = input("Enter left margin: ")
rMarginIn = input("Enter right margin: ")

sampleText = open("DAT1.txt", "r")
outputText = open("output.txt", "w+")

margin = '      ' #Number of 12 pt spaces to equal an inch
marginChars = 6
numOfFileChars = 80 - ((marginChars*lMarginIn) + (marginChars*rMarginIn))

#newWords = sampleText.read()
#word = newWords.split()

outputText.write("01234567890123456789012345678901234567890123456789012345678901234567890123456789\n")
while True:
  line = sampleText.readline(numOfFileChars)
  if not line:
    break
  outputText.write(margin*lMarginIn + line + margin*rMarginIn +"\n")
  
sampleText.close()
outputText.close()