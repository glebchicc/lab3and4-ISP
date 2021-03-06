# lab3and4-ISP
Лабораторные номер 3 и 4 по ИСП

Буткевич Глеб Олегович, группа 053505, 2022 г.

# Расписание автобусов
https://buslaba.herokuapp.com/

Заходя на сайт, пользователь видит две вещи. Во-первых, сайт предлагает ему авторизоваться или зарегистрироваться. Во-вторых, он видит меню выбора мест отправления и назначения. Если пользователь проигнорирует регистрацию/вход, то сайт сам предложит ему авторизоваться.
![image](https://user-images.githubusercontent.com/38133117/174634868-609cbf0c-dbbf-4d39-91e4-4600f90fb280.png)

Страница входа выглядит таким образом. Чуть что, пользователь всегда может перейти на форму регистрации.
![image](https://user-images.githubusercontent.com/38133117/174635067-4f33c52f-c0ff-4831-8321-45bad7d6aa2f.png)

То же относится и к форме регистрации: при ошибочном попадании пользователь может вернуться на форму входа.
![image](https://user-images.githubusercontent.com/38133117/174635736-10fe4352-9d9c-410e-b662-682daf8412f3.png)

Зайдя в аккаунт, мы возвращаемся к меню выбора мест отправления и пребытия. Но на этот раз мы уже авторизованы и можем просмотреть список маршрутов. Также при необходимости можно выйти из аккаунта.
![image](https://user-images.githubusercontent.com/38133117/174636029-3cd76df9-8816-4a59-9ab3-b125ebb14eac.png)

Войдя в аккаунт за обычного пользователя, мы можем просматривать список автобусов, однако не можем его изменять.
![image](https://user-images.githubusercontent.com/38133117/174636263-2a0d182b-e55c-4ff5-89b9-67f47d0ed678.png)

Когда же мы зайдем за суперпользователя, то появится возможность изменять список маршрутов прямо на сайте.
![image](https://user-images.githubusercontent.com/38133117/174636804-0fcd17f9-837a-44c3-a25d-740bc29c7323.png)

Зайдя на страницу CRUDа, мы можем создавать новый маршруты, а также изменять или удалять старые
![image](https://user-images.githubusercontent.com/38133117/174637180-10a41200-38dc-4758-8bb9-cf8562c2f8b8.png)

Например, изменим самый верхний маршрут, увеличив число мест и его размер:
![image](https://user-images.githubusercontent.com/38133117/174637363-e1d9a796-7d68-4723-83a6-a8e6a0080584.png)
![image](https://user-images.githubusercontent.com/38133117/174637493-4e83957d-b6b7-4d4f-bce9-cfae4913cf1e.png)

А потом можем и вовсе его удалить (скриншот после удаления):
![image](https://user-images.githubusercontent.com/38133117/174637682-b7e581c5-ee68-4f40-ac45-32b58326c49f.png)
