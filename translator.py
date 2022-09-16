file=open('E://hdd/my websayt/python/t7/translator.txt', 'r')
data=file.read()
word_list=data.split('\n')
words=[]
for i in range(len(word_list)):
    word_list_info = word_list[i].split(',')
    mydict =   {'english': word_list_info[0],
                'persian': word_list_info[1] }
    words.append(mydict)
file.close()
def add_word():
    e=input('english ? : ')
    p=input('persian ? : ')
    nd=({'english':e,'persian':p})
    words.append(nd)
    print('Done')
def english_to_persian():
    print('Be sure to put a period at the end of each sentence. ')
    s=input('English sentence : ')
    sn=s.split('.')
    for j in range(len(sn)):
        n=sn[j].split(' ')
        for k in range(len(n)):
            for i in range(len(words)):
                if n[k] == words[i]['english']:
                    print(words[i]['persian'] , end=' ')
                else:
                    pass
        else:
                print('This word ',n[k],' out of our dictionary')
        print('.',end='  ')
def persian_to_english():
    print('Be sure to put a period at the end of each sentence. ')
    s=input('Pesian sentence : ')
    sn=s.split('.')
    for j in range(len(sn)):
        n=sn[j].split(' ')
        for k in range(len(n)):
            for i in range(len(words)):
                if n[k] == words[i]['persian']:
                    print(words[i]['english'] , end=' ')
                else:
                    pass
            else:
                print('This word ',n[k],' out of our dictionary')
        print('.',end='  ')
def sive():
    f=open('E://hdd/my websayt/python/t7/translator.txt','w')
    for i in range(len(words)):
        data=words[i]['english']+','+words[i]['persian']+'\n'  
        f.write(data)
    f.close()
    exit()
def menu():
    print(' 1 for Add a word ')
    print(' 2 for English to Persian translator ')
    print(' 3 for Persian to English ')
    print(' 4 for Exit the app ')
while True:
    menu()
    a=int(input())
    if   a<2:
        add_word()
    elif a==2:
        english_to_persian()
    elif a==3:
        persian_to_english()
    elif a==4:
        sive()