import os
import pytest

if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', './allure/xml'])
    os.system('allure generate ./allure/xml -o ./allure/html --clean')
