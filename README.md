# 自动计算 WES iGPA

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/Auto-WES-iGPA-Calculator)](../../graphs/commit-activity)
![Python package](https://github.com/HollowMan6/Auto-WES-iGPA-Calculator/workflows/Python%20package/badge.svg)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/Auto-WES-iGPA-Calculator?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/Auto-WES-iGPA-Calculator?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/Auto-WES-iGPA-Calculator?style=social)](../../network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/Auto-WES-iGPA-Calculator.svg)](../../archive/master.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/Auto-WES-iGPA-Calculator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Auto-WES-iGPA-Calculator/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/Auto-WES-iGPA-Calculator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Auto-WES-iGPA-Calculator/context:python)

(English version is down below)

[Python库依赖](../../network/dependencies)

当计算WES GPA时自动输入课程名，学分和成绩。

此程序使用Python的selenium库，使用前请确保电脑上已经安装了Google Chrome浏览器，并且在程序执行目录下放置了[Chrome Driver](https://chromedriver.chromium.org)。

## 使用方法

成绩文件应为csv格式，无文件头，类似于：

```文本
课程名,学分,成绩
   ...
```

确保成绩在0到100之间。

[成绩文件示例](grade.csv)

运行[脚本](Auto-WES-iGPA-Calculator.py)，然后输入成绩文件位置（空为`grade.csv`）。

之后，首先在打开的浏览器（WES iGPA计算器）中输入并提交相关信息，程序会在需要时自动填充。

最后，查看你的GPA，然后手动关闭浏览器。

**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***

# Auto WES iGPA Calculator

[Python library dependency](../../network/dependencies)

Automatically input your course title, credit and grade when calculating WES GPA.

Using selenium to realize the function. Before using, make sure that Google Chrome browser is installed on the computer, and [Chrome Driver](https://chromedriver.chromium.org) is placed in the programme execution directory.

## Usage

The grade file should be in csv format without header like:

```text
title,credit,grade
   ...
```

Make sure that the grade is ranged between 0 and 100.

[Example grade file](grade.csv)

Run the [script](Auto-WES-iGPA-Calculator.py), then enter the grade file location (empty to be `grade.csv`).

Afterwards, input and submit relevant information in the opened browser (WES iGPA Calculator) first, the programme will automatically fill when needed.

Finally, check your GPA and then close the browser manually. 

**Warning**:

***For TESTING ONLY, not for any ILLEGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***
