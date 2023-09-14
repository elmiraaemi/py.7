import pyfiglet
import qrcode
file = open('E:\.vscode\web di\python\T7\stor .txt', 'r')
data = file.read()
product_list = data.split('\n')
products = []
for i in range(len(product_list)):
    product_list_info = product_list[i].split(',')
    mydict =   {'id': int(product_list_info[0]),
                'name': product_list_info[1],
                'price': int(product_list_info[2]),
                'count': int(product_list_info[3]) }
    products.append(mydict)
file.close()

def loading():
    result = pyfiglet.figlet_format('MY STORE', font = 'roman')
    print(result)

def menu_productes():
    print('1 for add product')
    print('2 for edit product')
    print('3 for delete product')
    print('4 for search product')
    print('5 for show list productes')
    print('6 for buy product')
    print('7 for Qr code of product')
    print('8 for exit')

def add_productes():
    c=int(input('id ? : '))
    n=input('name ? : ')
    p=int(input('price ? : '))
    k=int(input('count ? : '))
    products.append({'id':c,'name':n,'price':p,'count':k})
    print('Done')

def edit_productes():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            while True:
                print('1 for name')
                print('2 for price')
                print('3 for count')
                print('4 for exit')
                e = int(input())
                if e == 1:
                    products[i]['name']=input(' type rename product : ')
                    print('Done')
                elif e ==2:
                    products[i]['price']=float(input(' type reprice product : '))
                    print('Done')
                elif e == 3:
                    products[i]['count']=int(input(' type recount product : '))
                    print('Done')
                elif e ==4:
                    break  
                else:
                    print('Does not exist')

def delete_productes():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            products.remove(products[i])
            print('Done')
            break
    else:
        print('Does not exist')

def search_productes():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            print(products[i])
            break
    else:
        print('Does not exist')

def show_productes():
    for i in range(len(products)):
        print(products[i])

def Qr_productes():
    name=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == name or str(products[i]['id'] )== name:
          QR=[]
          QR.append(products[i]['name'])
          QR.append(products[i]['id'])
          img=qrcode.make(QR)
          img.save("qrcode.jpg")
          print('Done')

def buy_productes():
    pri=[]
    while True:
        name=input('name or id of product ? : ')
        for i in range(len(product_list)):
            if products[i]['name'] == name or str(products[i]['id'] )== name:
                cou=int(input('count ? : '))
                if int(products[i]['count'])>=cou:
                    pri.append({'name':products[i]['name'],
                            'price':products[i]['price'],
                            'count':cou})
                    products[i]['count']-=cou  
                else:
                    print('The number of products is not enough')
                    print('we have',products[i]['count'])
                s=int(input('Do you still want to buy something? : (1 for yes 2 for no)'))
                if s==2:
                    break
        else:
            print('Does not exist')
        print(pri)
        tpri=0
        for j in range(len(pri)):
            tpri+=pri[i]['price']*pri[i]['count']
        print('total price : ', tpri)
        break

def exit_store():
    f=open('E:\.vscode\web di\python\T7\stor .txt','w')
    for i in range(len(products)):
        data=str(products[i]['id'])+','+products[i]['name']+','+str(products[i]['price'])+','+str(products[i]['count'])+'\n'  
        f.write(data)
    f.close()
    exit()



loading()
while True:
        menu_productes()
    a=int(input())
    if   a<2:
        add_productes()
    elif a==2:
        edit_productes()
    elif a==3:
        delete_productes()
    elif a==4:
        search_productes()
    elif a==5:
        show_productes()
    elif a==6:
        buy_productes()
    elif a==7:
        Qr_productes()
    elif a==8:
        exit_store()
