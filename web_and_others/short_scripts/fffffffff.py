import os
import time
source = ['C:\\Users\\79511\\Downloads']
target_dir = 'C:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = '"C:\\Program Files (x86)\\GnuWin32\\bin\\zip.exe" -qr {0} {1}'.format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
