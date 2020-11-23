from time import sleep
import matplotlib.pyplot as plt

FILE_NAME_1 = "word1.txt"  # Default File Name 1
FILE_NAME_2 = "word2.txt"  # Default File Name 2
PRINT_LIMIT = 20  # Default Print Limit
STOPWORDS = ["i", "its", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his",
             "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
             "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did",
             "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
             "between", "into", "through", "during", "before", "after", "above", "below", "from", "up", "down", "in", "out", "on", "off", "over",
             "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
             "most", "to", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
             "don", "should", "now", "to", "nt", "th", "m", "int", "re"]  # List of the Stopwords retrieved from NLTK library and some additions of my own
PUNCTUATION = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "?", "\'", "\"", "{", "}", "[", "]", "<", ">", "~",
               "`", ":", ";", "|", "\\""/", ".", ",", "°F", "°C", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]  # Punctuation list


def readFile(answer):
    if answer == "1":  # In the case of reading single default file
        try:
            FILE_NAME_1 = "word1.txt"
            file = open(FILE_NAME_1, "r")  # Open the txt file as read
            Text1 = file.read()  # Read the contents of the file
            file.close()  # Close the file
            # Clean the punctuation and make the text lowercase
            Text1 = cleanPunctuation(Text1).lower()
            Text1list = Text1.split()  # Split string file into individual words in a list
            # Remove the stopwords from the text list and calculate the frequency of the words and store them in a list called result
            result = evaluateTextList(removeStopWords(Text1list))

            printSingleFileResult(result)  # Print the resulting list

        except IOError:  # In case of the file not being readable or non existent
            print("File non existent or inaccessible")
            sleep(3)
            SystemExit(0)  # Exit

    elif answer == "3":  # In the case of the user wanting to enter their own file
        # Replace the default file name with the one user entered
        FILE_NAME_1 = input(
            "Please enter the name of the file you would like to evaluate with the full extension (The file must be in the path of the .py file): ").strip()

        try:
            file = open(FILE_NAME_1, "r")
            Text1 = file.read()
            file.close()
            Text1 = cleanPunctuation(Text1).lower()
            Text1list = Text1.split()
            result = evaluateTextList(removeStopWords(Text1list))

            printSingleFileResult(result)

        except IOError:
            print("File non existent or inaccessible")
            sleep(3)
            SystemExit(0)

    elif answer == "2":  # In the case of reading two default files
        try:
            FILE_NAME_1 = "word1.txt"
            file1 = open(FILE_NAME_1, "r")
            Text1 = file1.read()
            file1.close()
            if(len(Text1.strip()) != 0):
                Text1 = cleanPunctuation(Text1).lower()
                Text1list = Text1.split()
                result1 = evaluateTextList(removeStopWords(Text1list))

                FILE_NAME_2 = "word2.txt"
                file2 = open(FILE_NAME_2, "r")
                Text2 = file2.read()
                file2.close()
                if(len(Text2.strip()) != 0):
                    Text2 = cleanPunctuation(Text2).lower()
                    Text2list = Text2.split()
                    result2 = evaluateTextList(removeStopWords(Text2list))

                    # Print the result for two files
                    printDoubleFileResult(result1, result2)
                else:
                    print("FILE_2 has incorrect content")
            else:
                print("FILE_1 has incorrect content")

        except IOError():
            print("File non existent or inaccessible")
            sleep(3)
            SystemExit(0)

    elif answer == "4":  # In the case of user wanting to use their own two files
        FILE_NAME_1 = input(
            "Please enter the name of the first file you would like to evaluate with the full extension (The file must be in the path of the .py file): ").strip()
        FILE_NAME_2 = input(
            "Please enter the name of the second file you would like to evaluate with the full extension (The file must be in the path of the .py file): ").strip()

        try:
            file1 = open(FILE_NAME_1, "r")
            Text1 = file1.read()
            file1.close()
            if(len(Text1.strip()) != 0):
                Text1 = cleanPunctuation(Text1).lower()
                Text1list = Text1.split()
                result1 = evaluateTextList(removeStopWords(Text1list))

                file2 = open(FILE_NAME_2, "r")
                Text2 = file2.read()
                file2.close()
                if(len(Text2.strip()) != 0):
                    Text2 = cleanPunctuation(Text2).lower()
                    Text2list = Text2.split()
                    result2 = evaluateTextList(removeStopWords(Text2list))

                    printDoubleFileResult(result1, result2)
                else:
                    print("FILE_2 has incorrect content")
            else:
                print("FILE_1 has incorrect content")

        except IOError():
            print("File non existent or inaccessible")
            sleep(3)
            SystemExit(0)


# Takes the recently read string as the argument
def cleanPunctuation(incomingString):
    newstring = incomingString
    for char in PUNCTUATION:  # For every element in Punctuation list replace the element with a " "
        newstring = newstring.replace(char, " ")

    return newstring


# Takes the text as list after the seperation of words in the original text string
def removeStopWords(textList):
    # For every element in Stopwords list remove them from the list of words
    for i in range(0, len(STOPWORDS), 1):
        for j in range(0, len(textList), 1):
            if(textList[j] == STOPWORDS[i]):
                textList.remove(STOPWORDS[i])
            if(j >= len(textList)-1):
                break
    textList.sort()

    return textList


def evaluateTextList(textList):  # Takes the cleaned and sorted word list
    words = []
    wordcount = []

    num = 0
    words.append(textList[0])
    wordcount.append(0)

    # Count each word and store them in their corresponding lists
    for i in range(len(textList)):
        if textList[i] == words[num]:
            wordcount[num] += 1
        else:
            num += 1
            words.append(textList[i])
            wordcount.append(1)

    result = zip(wordcount, words)  # joining two lists together
    # sorting the joined list according to the word count
    result = sorted(result)

    return result


# Takes the result list that has been produced by the evaluateTextList() function
def printSingleFileResult(result):
    words = []
    wordcount = []
    # "Unzipping" the result list in descending order
    for i in range(len(result)-1, len(result)-PRINT_LIMIT-1, -1):
        words.append(result[i][1])
        wordcount.append(result[i][0])

    plt.barh(words, wordcount)  # Create the bar chart in the Y axis2
    plt.show()
    # In case the computer executing the code doesn't have matplotlib installed I left the default way of displaying the data in a comment
    """ 
    counter = 1
    print("NO   WORD    FREQ")
    for i in range(len(result)-1,len(result)-PRINT_LIMIT-1,-1):
        print(counter," ",result[i][1],"  ",result[i][0])
        counter+=1
    """


# Takes two result lists that have been produced by the evaluateTextList() function
def printDoubleFileResult(result1, result2):
    word = []
    freq1 = []
    freq2 = []
    totalfreq = []
    # "Unzipping" the result lists in descending order, finding the same words in the two lists while doing so
    for i in range(len(result1)-1, len(result1)-PRINT_LIMIT-1, -1):
        for j in range(len(result2)):
            if(result1[i][1] == result2[j][1]):
                word.append(result1[i][1])
                freq1.append(result1[i][0])
                freq2.append(result2[j][0])
                totalfreq.append(result1[i][0]+result2[j][0])
                break

    # Joining the final result in a single list
    finalresult = zip(totalfreq, word, freq1, freq2)
    finalresult = sorted(finalresult)  # Sorting the joined list

    counter = 1
    print("NO   WORD   FREQ_1   FREQ_2  TOTAL")
    if(len(finalresult) >= 20):
        # Printing in descending order
        for i in range(len(finalresult)-1, len(finalresult)-PRINT_LIMIT-1, -1):
            print(counter, "  ", finalresult[i][1], "  ", finalresult[i]
                  [2], "  ", finalresult[i][3], "  ", finalresult[i][0])
            counter += 1
    elif(len(finalresult) != 0):
        for i in range(len(finalresult)-1, 0, -1):
            print(counter, "  ", finalresult[i][1], "  ", finalresult[i]
                  [2], "  ", finalresult[i][3], "  ", finalresult[i][0])
            counter += 1
    else:
        print("There seems to be no words in common")


def menu():  # Menu
    print("                 WELCOME TO THE MENU")
    print()
    print("1- Find the most common words in", FILE_NAME_1)
    print("2- Find the total frequency of words in",
          FILE_NAME_1, "and", FILE_NAME_2)
    print("3- Find the most common words in a file of your choice")
    print("4- Find the total frequency of words in two files of your choice")
    isValidAnswer = False
    while not isValidAnswer:
        ans = input().strip()
        if ans == "1":
            readFile(ans)
            isValidAnswer = True
        elif ans == "2":
            readFile(ans)
            isValidAnswer = True
        elif ans == "3":
            readFile(ans)
            isValidAnswer = True
        elif ans == "4":
            readFile(ans)
            isValidAnswer = True
        else:
            print("Incorrect Input")


def main():
    menu()


main()
