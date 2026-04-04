# testAutomation
We are planning to support both Selenium (web) and Appium (mobile), design the project as a driver-agnostic, layered framework from day one. 

Don’t bolt Appium later—keep a clean abstraction so both stacks plug into the same test + config + reporting layers.

Folder Structure: 
==========================
testautomation-framework/
│
├── config/
│   ├── config.yaml              # env configs (urls, timeouts)
│   ├── capabilities/
│   │   ├── web.yaml             # browser configs
│   │   ├── android.yaml         # appium android caps
│   │   └── ios.yaml             # appium ios caps
│
├── core/
│   ├── driver_factory.py        # central driver creation (KEY)
│   ├── base_test.py             # setup/teardown
│   ├── logger.py
│   └── utils.py
│
├── drivers/
│   ├── web_driver.py            # selenium wrapper
│   └── mobile_driver.py         # appium wrapper
│
├── pages/
│   ├── web/
│   │   └── google_page.py
│   └── mobile/
│       └── login_page.py
│
├── tests/
│   ├── web/
│   │   └── test_google.py
│   └── mobile/
│       └── test_login.py
│
├── reports/
│
├── requirements.txt
├── pytest.ini
├── Jenkinsfile
└── README.md


Key Design Principle:
==================================
Single Driver Factory → Multiple Platforms

Everything (web/mobile) should flow through one abstraction layer.


Python Dependencies Needed:
====================================
Core
selenium → Web automation
Appium-Python-Client → Mobile automation

Test Layer
pytest → base runner
pytest-xdist → parallel execution (critical for CI)
pytest-rerunfailures → handle flaky infra (very useful with Selenium/Grid)

Infra / Stability
requests → health check (like your Selenium validation)
tenacity → production-grade retry (replace manual loops later)

Config
PyYAML → external config (capabilities, env)
python-dotenv → env management

Reporting
pytest-html → quick report
allure-pytest → enterprise-level reporting