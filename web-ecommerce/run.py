import pytest, sys
if __name__ == '__main__':
    sys.exit(pytest.main(["tests/", "--html=reports/report.html", "--self-contained-html", "-v"]))