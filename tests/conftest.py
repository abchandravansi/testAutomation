import pytest
from src.core.config_loader import load_env_config
from src.core.utils import load_capabilities
from src.drivers.web_driver import create_web_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome,firefox,edge",
        help="Comma separated browser list"
    )


@pytest.fixture(scope="function")
def driver(request):
    env_config = load_env_config()

    browsers = request.config.getoption("--browser").split(",")

    # pytest param will inject one browser at a time
    browser = request.param

    caps = load_capabilities("web", browser)

    drv = create_web_driver(env_config, caps)

    yield drv

    drv.quit()