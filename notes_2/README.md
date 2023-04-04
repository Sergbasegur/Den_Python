# Промежуточная контрольная работа по блоку специализация.
## Урок 1. Приложение заметки (Python)

### Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

# Промежуточная аттестация
## Приложение заметки
## Информация о проекте
1. Необходимо написать проект, содержащий функционал работы с заметками.
2. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
## Как сдавать проект
1. Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этомрепозитории, использовать пул реквесты на изменения
2. Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.
## Задание
1. Реализовать консольное приложение заметки, с сохранением, чтением,добавлением, редактированием и удалением заметок. 
2. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
3. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). 
4. Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента. 
### Например: 
*** python notes.py add --title "новая заметка" –msg "тело новой заметки" ***
### Или так:
*** python note.py ***
*** Введите команду: add ***
*** Введите заголовок заметки: новая заметка
 - Введите тело заметки: тело новой заметки
- Заметка успешно сохранена
- Введите команду:  

### При чтении списка заметок реализовать фильтрацию по дате.

## Критерии оценки
### Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.