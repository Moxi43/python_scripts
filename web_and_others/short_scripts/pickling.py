import pickle
#имя файла, в котором мы сохраним объекто
shoplistfile = 'shoplist.data'

shoplist = ['яблоки', 'манго', 'морковь']

#Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)#помещаем объект в файл
f.close()

del shoplist #Уничтожаем переменную shoplist

#Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)#Загружаем объект из файла
print(storedlist)
