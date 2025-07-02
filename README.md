
# Программа на python с дуже классним кодом!

# Інструкція з встановлення та збірки програми "Потужномір"

# Файл exe в моєму телеграммі!

# Вимоги
Python 3.8 або новіший

Бібліотеки Python:

Pillow

tkinter (у деяких Linux-дистрибутивах потрібно встановити окремо)

PyInstaller (для збірки в виконуваний файл)

Встановлення залежностей
Для Linux
Встанови Python, якщо його ще нема.

Встанови пакет для tkinter (наприклад, в Ubuntu/Debian):

bash
Копировать
Редактировать
sudo apt-get install python3-tk
Рекомендується створити віртуальне середовище і встановити пакети там:

bash
Копировать
Редактировать
python3 -m venv venv
source venv/bin/activate
pip install Pillow pyinstaller
Якщо отримуєш помилку про "externally managed environment" (наприклад в Arch Linux), користуйся віртуальним середовищем, як показано вище.

Для Windows
Встанови Python з офіційного сайту https://python.org (версія 3.8+).

Відкрий PowerShell або CMD та виконай:

powershell
Копировать
Редактировать
python -m venv venv
.\venv\Scripts\activate
pip install Pillow pyinstaller
Запуск скрипта напряму
В активованому віртуальному середовищі виконай:

bash
Копировать
Редактировать
python potujnomits.py
Збірка у виконуваний файл (.exe для Windows або бінарник для Linux)
Linux
Перемісти файли potujnomits.py і ukr.png в папку без кирилиці у шляху (наприклад, ~/projects):

bash
Копировать
Редактировать
mkdir -p ~/projects
mv ~/Загрузки/potujnomits.py ~/projects/
mv ~/Загрузки/ukr.png ~/projects/
cd ~/projects
Запусти PyInstaller:

bash
Копировать
Редактировать
pyinstaller --onefile --windowed \
--hidden-import=PIL._tkinter_finder \
--hidden-import=PIL.ImageTk \
--collect-submodules=PIL \
--add-data "ukr.png:." \
potujnomits.py
Виконуваний файл з'явиться у папці dist/:

bash
Копировать
Редактировать
./dist/potujnomits
Windows
Помісти файли potujnomits.py і ukr.png у папку, наприклад C:\projects\.

Відкрий PowerShell, перейди до папки:

powershell
Копировать
Редактировать
cd C:\projects\
.\venv\Scripts\activate
Запусти PyInstaller:

powershell
Копировать
Редактировать
pyinstaller --onefile --windowed --add-data "ukr.png;." potujnomits.py
Зверни увагу на символ ; (крапка з комою) замість двокрапки : у --add-data для Windows.

Виконуваний файл з'явиться у папці dist\potujnomits.exe.

Запуск зібраної програми
Запусти файл potujnomits (Linux) або potujnomits.exe (Windows).

Важливі моменти
Файл картинки ukr.png має бути поруч з виконуваним файлом або доданий через параметр --add-data.

Якщо виникають помилки, перевір, чи встановлені всі залежності і чи правильні шляхи.

Для зручності рекомендується працювати у віртуальному середовищі Python.

# Готово!
