import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))




# import os

# os.chdir("c:/Users/Swift3/Desktop/hackathon/")
#klasör konumu ayarlama


def demoAi(inputText):
    
    def createStruc(inputText):
        textSplitted = inputText.split()
        textList = list()
        #yapıyı oluşturma, list of list
        for number in textSplitted:
            list0 = list()
            list0.append(number)
            list0.append(0)
            textList.append(list0)
        #kaç kelime olduğunu sayma
        for number in range(len(textList)):
            for number2 in range(len(textList)):
                if textList[number][0] == textList[number2][0]:
                    textList[number][1] += 1

        #çoklu ögeleri silme
        tempList = []
        newList = []
        for i in textList:
            if i[0] not in tempList:
                tempList.append(i[0])
                list1 = list()
                list1.append(i[0])
                list1.append(i[1])
                newList.append(list1)

        textList = newList
        return textList

    textList = createStruc(inputText)


    #sınıf oluşturma uyuşmazlık
    class Disagre():
        def __init__(self, name, word_list):
            self.name = name
            self.word_list = word_list



    #puan oluşturma son

    #educateai için source açma
    #internet için uyarlama lazım
    with open("C:\\Users\\Swift3\\Desktop\\hackathon\\legalproject\\legalapp\\demo\\source.txt", "r+", encoding="utf8") as text:
        data = text.read()
        data = data.lower()

    with open("C:\\Users\\Swift3\\Desktop\\hackathon\\legalproject\\legalapp\\demo\\sourceabone.txt", "r+", encoding="utf8") as text2:
        data2 = text2.read()
        data2 = data2.lower()


    def educateAi(data):
        data = data.splitlines()
        counter = []
        counterValue = []
        for i in data:
            
            splitted = i.split()
            for j in splitted:
                if j in counter:
                    numeroIndex = counter.index(j)
                    counterValue[numeroIndex] += 1
                elif j not in counter:
                    counter.append(j)
                    counterValue.append(1)

        # print(len(counter), len(counterValue))
        wordCount = []
        for i in range(len(counter)):
            list2 = list()
            list2.append(counter[i])
            list2.append(counterValue[i])
            wordCount.append(list2)



        def bubble_sort(listfororder):
            # We set swapped to True so the loop looks runs at least once
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(listfororder) - 1):
                    if listfororder[i][1] > listfororder[i + 1][1]:
                        # Swap the elements
                        listfororder[i], listfororder[i + 1] = listfororder[i + 1], listfororder[i]
                        # Set the flag to True so we'll loop again
                        swapped = True
            return listfororder


        bubble_sort(wordCount)
        sortedWordCount = wordCount[-30:]
        for i in range(len(sortedWordCount)):
            sortedWordCount[i][1] = sortedWordCount[i][1]/10

        return sortedWordCount




    #kelime arama kısmı
    


    ayipliMal = Disagre("Ayıplı Mal", educateAi(data))
    abonelikSoz = Disagre("Abonelik Sözleşmeleri", educateAi(data2))
    #class içinde uyuşmazlığın çarpanı olacak bunu da kelime sayısıyla bir işleme sokup final score u sıralayacağız
    # print(ayipliMal.word_list)
    def calValue(textList, disagr):
        totalValue = 0
        for i in textList:
            for j in disagr.word_list:
                if i[0] == j[0]:
                    totalValue += i[1]*j[1]
        return totalValue
    
    return calValue(textList, ayipliMal), calValue(textList, abonelikSoz)

# print("ayıplı mal değeri : ", calValue(textList, ayipliMal))
# print("abonelik değeri : ", calValue(textList, abonelikSoz))
           
# print(demoAi(inputText1))