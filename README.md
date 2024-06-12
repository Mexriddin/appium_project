# Проект по автоматизации тестирования мобильного приложения MY DEMO APP

<br>
<p align="center">
<img width="122" title="DemoApp" src="media/logo/mydemoapp.png" alt="demoaapp">
</p>
<br>

##  📌Содержание:


- [Использованный стек технологий](#использованный-стек-технологий)
- [Реализованные проверки](#реализованные-проверки)
- [Запуск тестов](#запуск-тестов)
- [Сборка в Jenkins](#-сборка-в-jenkins)
- [Пример Allure-отчета](![Снимок экрана 2024-06-12 004831.png](..%2F..%2FOneDrive%2F%D0%E0%E1%EE%F7%E8%E9%20%F1%F2%EE%EB%2Fdock%2F%D1%ED%E8%EC%EE%EA%20%FD%EA%F0%E0%ED%E0%202024-06-12%20004831.png)#-пример-allure-отчета)
- [Интеграция с Allure TestOps](#-интеграция-с-allure-testops)
- [Уведомления в Telegram с использованием бота](#-уведомления-в-telegram-с-использованием-бота)
- [Видео примера запуска теста в Selenoid](#-видео-примера-запуска-теста-в-selenoid)

## Использованный стек технологий

<p align="center">
<code><a href="https://www.python.org/"><img width="6%" title="Python" src="media/logo/python.png"></a></code>
<code><a href="https://www.jetbrains.com/pycharm/"><img width="6%" title="PyCharm IDEA" src="media/logo/PyCharm_Icon.png"></a></code>
<code><a href="https://docs.pytest.org/"><img width="6%" title="Pytest" src="media/logo/Pytest_logo.svg"></a></code>
<code><a href="https://python-poetry.org/"><img width="5%" title="Poetry" src="media/logo/poetry.svg"></a></code>
<code><a href="https://appium.io/"><img width="6%" title="Appium" src="media/logo/appium.svg"></a></code>
<code><a href="https://developer.android.com/"><img width="6%" title="AndroidStudio" src="media/logo/AndroidStudio.svg"></a></code>
<code><a href="https://www.browserstack.com/"><img width="6%" title="Browser Stack" src="media/logo/Browserstack.svg"></a></code>
<code><a href="https://allurereport.org/"><img width="6%" title="Allure Report" src="media/logo/AllureReports.png"></a></code>
<code><a href="https://qameta.io/"><img width="6%" title="Allure TestOps" src="media/logo/AllureTestOps.svg"></a></code>
<code><a href="https://telegram.org/"><img width="6%" title="Telegram" src="media/logo/Telegram.png"></a></code>
<code><a href="https://github.com/"><img width="6%" title="GitHub" src="media/logo/GitHub.png"></a></code>
<code><a href="https://docs.github.com/ru/actions"><img width="6%" title="GitHub Action" src="media/logo/action.png"></a></code>
</p>


Запуск тестов можно осуществлять локально или с помощью [BrowserStack](https://www.browserstack.com/).
Также реализована сборка в <code>GitHub Action</code> с формированием Allure-отчета и отправкой уведомления с результатами в <code>Telegram</code> после завершения прогона.

Автотесты написаны на `Python` с использованием фреймворк `Appium`.
- `Poetry` - используется в качестве инструмента сборки зависимости.
- `Pytest` - to execute tests.
- `Appium, Android Studio` - для выполнения тестов локально на машине
- `Browserstack` - для удаленного проведения тестов.
- `GitHub Action` - CI/CD для удаленного выполнения тестов.
- `Telegram Bot` - для уведомлений о результатах теста.
- `Allure Report` - для результатов теста визуализация.
- `Allure TestOps` - в качестве системы управления тестами.

Allure-отчет включает в себя:
* шаги выполнения тестов;
* скриншот и видеозапись экрана в устройстве в момент подение автотеста;
* логи браузерной консоли;

## Реализованные проверки

- [x] *Проверка логирование пользователя*
- [x] *Проверка добавление продукта в корзинку*
- [x] *Проверка сортировки продуктов*
- [x] *Проверка оформление покупки*
- [x] *Проверка АПИ запросов*

## Запуск тестов
Перед выполением необходимо:
* в .env определить параметры конфигурации:
    - `BROWSERSTACK_USERNAME`
    - `BROWSERSTACK_ACCESS_KEY`
    - `TG_TOKEN`
    - `CHAT_ID`

### Локальный запуск тестов
```sh
poetry run pytest --mode_run local_em
```
При необходимости можно переопределить параметры запуска
```
pytest -m  positive - запуск позитивных тестов
pytest -m  negative - запауск негативных
pytest -m  smoke - только smoke
```

### Запуск тестов на удаленном браузере
```sh
poetry run pytest --mode_run remote_bs
```
При необходимости также можно переопределить параметры запуска

## <img width="4%" style="vertical-align:middle" title="GitHub Action" src="media/logo/action.png"> <a href="https://github.com/Mexriddin/appium_project/actions/workflows/allure_action.yml"> Сборка в GitHub Action</a>
<p align="center">
<img title="Jenkins Build" src="media/screenshots/github_action.png">
</p>

## <img width="4%" style="vertical-align:middle" title="Allure Report" src="media/logo/AllureReports.png"> <a href="https://mexriddin.github.io/appium_project/">Пример Allure-отчета</a>
### Обзор

<p align="center">
<img title="Allure Overview" src="media/screenshots/allure_report_dash.png">
</p>

### Результат выполнения теста

<p align="center">
<img title="Test Results in Alure" src="media/screenshots/allure_report_result.png">
</p>

## <img width="4%" title="Allure TestOPS" src="media/logo/allureTestOps.svg"> Интеграция с [Allure TestOps](https://qameta.io/)

### Запуски

<p align="center">
  <img src="media/screenshots/launch.png" alt="dashboard" width="900">
</p>

### Основной дашборд

<p align="center">
  <img src="media/screenshots/testops_dash.png" alt="dashboard" width="900">
</p>

### Список тестов с результатами прогона

<p align="center">
  <img src="media/screenshots/result_all.png" alt="dashboard" width="900">
</p>

### Успешный тест

<p align="center">
  <img src="media/screenshots/result_pass.png" alt="dashboard" width="900">
</p>

### Проваленный тест

<p align="center">
  <img src="media/screenshots/result_faild.png" alt="dashboard" width="900">
</p>

### Тест-кейсы

<p align="center">
  <img src="media/screenshots/test_cases.png" alt="testcase" width="900">
</p>



### <img width="4%" style="vertical-align:middle" title="Telegram" src="media/logo/Telegram.png"> Уведомления в Telegram с использованием бота

После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img width="70%" title="Telegram Notifications" src="media/screenshots/notification.png">
</p>
