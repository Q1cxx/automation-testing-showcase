# 🧪 Automation Testing Showcase
&gt; 面试专用：软件 & 游戏 自动化脚本合集

| 模块 | 技术 | 状态 |
|---|---|---|
| Web 自动化 | Selenium + Pytest | ✅ 已上传样例 |
| API 测试 | Requests + Pytest | ✅ 已上传样例 |
| Unity 测试 | Unity Test Runner | ✅ 已上传样例 |
| 手游自动化 | Airtest | ✅ 已上传样例 |
| CI/CD | GitHub Actions | ✅ 已配置 |

## ▶️ 一键本地运行
```bash
git clone https://github.com/YOUR_NAME/automation-testing-showcase.git
cd automation-testing-showcase
# Web 测试
pip install -r software-testing/web-automation/requirements.txt
pytest software-testing/web-automation/tests

---

#### ② `software-testing/web-automation/requirements.txt`

---

#### ③ `software-testing/web-automation/pytest.ini`
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
addopts = --html=reports/report.html --self-contained-html
// 占位脚本，Unity 识别后即可出 Test Runner 窗口
public class TestRunner {}
# Python
__pycache__/
*.pyc
reports/

# Unity
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/