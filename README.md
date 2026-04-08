# CalcWithMe Agent - 自动运营系统

## 概述

CalcWithMe Agent 是一套自动运营脚本，用于监控、优化和增长 CalcWithMe.com 网站。

## 文件结构

```
calcwithme-agent/
├── config.py                    # 配置文件（网站地址、域名等）
├── README.md                    # 说明文档
├── scripts/
│   ├── seo_monitor.py          # SEO监控脚本
│   ├── competitor_analysis.py    # 竞品分析脚本
│   ├── generate_state_pages.py  # 批量生成州级页面
│   └── weekly_report.py         # 每周运营报告
├── reports/                     # 生成的报告存放目录
└── output/                      # 输出文件目录
```

## 快速开始

### 1. 运行SEO监控
```bash
cd C:\Users\Administrator\.qclaw\workspace\calcwithme-agent
python scripts/seo_monitor.py
```

### 2. 运行竞品分析
```bash
python scripts/competitor_analysis.py
```

### 3. 生成州级房贷计算器页面
```bash
python scripts/generate_state_pages.py
```
- 会生成50个美国各州的房贷计算器页面
- 输出到 `calcwithme-site/state-pages/` 目录

### 4. 生成每周运营报告
```bash
python scripts/weekly_report.py
```

## 定时任务设置（Windows计划任务）

### 每天自动运行SEO监控
1. 打开"任务计划程序"
2. 创建基本任务
3. 触发器：每天 9:00 AM
4. 操作：启动程序
5. 程序：`python`
6. 参数：`C:\Users\Administrator\.qclaw\workspace\calcwithme-agent\scripts\seo_monitor.py`

### 每周自动生成报告
1. 触发器：每周一 9:00 AM
2. 操作：启动程序
3. 参数：`C:\Users\Administrator\.qclaw\workspace\calcwithme-agent\scripts\weekly_report.py`

## 报告查看

报告保存在 `reports/` 目录：
- `seo_report.json` - SEO监控报告
- `competitor_analysis.json` - 竞品分析报告
- `weekly_report_YYYY-MM-DD.json` - 每周运营报告

## 配置修改

编辑 `config.py` 修改以下内容：

```python
# 网站配置
DOMAIN = "calcwithme.com"  # 你的域名
NETLIFY_URL = "https://xxx.netlify.app"  # Netlify临时地址

# 路径配置
LOCAL_SITE_PATH = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"
```

## 下一步开发计划

- [ ] Google Search Console API 集成（自动获取排名数据）
- [ ] Google Analytics 4 集成（流量监控）
- [ ] 自动生成更多长尾关键词页面
- [ ] 用户行为分析（热力图集成）
- [ ] 自动提交 sitemap 到 Google
- [ ] 竞品价格监控（利率变化）
- [ ] 自动生成内容更新提醒

## 联系方式

如有问题，请在项目中提交 Issue。
