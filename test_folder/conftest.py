#conftest.py
import pytest

# def pytest_runtest_setup(item):
#     print(f"\nИмя: {item.name}")
#     print(f"Путь: {item.nodeid}")
#     print(f"Маркировки: {list(item.keywords)}")
#     print(f"Функция: {item.function.__name__}")

def pytest_runtest_setup(item):
    print(f"\n[SETUP] Подготовка к тесту: {item.name}")


# def pytest_runtest_setup(item):
#     if "slow" in item.keywords:
#         pytest.skip("Скипаем медленные тесты")

# import logging
#
# logging.basicConfig(filename="test_log.txt", level=logging.INFO, encoding="utf-8")
#
# def pytest_runtest_logreport(report):
#     if report.when == "call" and report.outcome == "passed":
#         logging.info(f"Тест {report.nodeid} прошёл успешно!")
#     elif report.when == "call" and report.outcome == "failed":
#         logging.error(f"Тест {report.nodeid} не прошёл!")






# def pytest_sessionstart(session):
#     print("🚀 Старт всей тестовой сессии")
#
# def pytest_runtest_setup(item):
#     print(f"\n🔧 Настройка перед тестом: {item.name}")
#
# def pytest_runtest_teardown(item, nextitem):
#     print(f"🧹 Очистка после теста: {item.name}")
#
# def pytest_sessionfinish(session, exitstatus):
#     print(f"✅ Тестирование завершено. Код выхода: {exitstatus}")


# import pytest
#
# @pytest.fixture
# def file():
#     print("\n📂 Открываю файл")
#     yield "data.txt"
#     print("🧹 Закрываю файл")
#
#
# @pytest.fixture
# def user_info(request):
#     print(f"🔎 Фикстура вызвана в тесте: {request.node.name}")
#     return {"user": "admin"}
