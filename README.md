# quokka
Our project to show programming skills at the end of the course

Описание: представим что есть ресурсоемкая задача, которую нужно выполнить большое количество раз
(в нашем случае это ресайз изображения и его деколоризация), и ее не очень выгодно выполнять
на данном устройстве. Тогда ее можно раскидать по другим устройствам, которые выполнят её и вернут пользователю
готовые результаты.

Задачи -> очередь задач -> множество машин, подписанных на очередь -> возвращающая очередь -> user.

Для работы программ необходима машина с установленным и настроенным RabbitMQ.
Для запуска обеих составляющих, в скриптах handler и producer подставить вместо текущего IP адрес
машинки с сервером RabbitMQ. В 'имя пользователя' и 'пароль' (Сейчас Raccoon и CoolRaccoon) подставить
данные пользователя сервера, имеющего все права доступа.

Далее запустить handler.py на всех машинках, где планируется производить вычисления, а затем в
скрипте producer.py указать путь к директории с изображениями и
список файлов, которые будут обработаны.

Все изображения будут добавлены в очередь, а затем распределены по исполняющим машинкам. По завершению исполненияя
каждой задачи она будет добавлена в возвращающую очередь, откуда вернется на компьютер отправителя и
материализуется в директории со скриптом producer.py

P.S В связи с тем, что программа умирает, когда натыкается на QFileDialog даже при исполнении примеров с документацией, графический интерфейс для пользователя будет предоставлен позже.
