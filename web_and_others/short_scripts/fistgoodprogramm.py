import os
import time
source = ['C:\\Documents'], ['C:\\Code']
target_dir = 'C:\\Backup'
target = target_dir + os.sep + time.strftime('%d%m%Y%H%M%S') + '.zip'
zip_command = '"C:\\Program Files (x86)\\GnuWin32\\bin\\zip" -qr {0} {1}'.format(target, ' '.join(source))
#Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная опия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')
