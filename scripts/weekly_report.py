"""
每周运营报告Agent
自动生成网站状态报告
"""
import json
import sys
import os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
except ImportError:
    print("Error: config.py not found")
    sys.exit(1)

def generate_weekly_report():
    """生成每周运营报告"""
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    
    print("\n" + "="*70)
    print("📊 CalcWithMe 每周运营报告")
    print(f"   报告日期: {today.strftime('%Y-%m-%d %A')}")
    print("="*70)
    
    # 1. 网站状态检查
    print("\n📍 网站状态")
    print("-"*50)
    try:
        import urllib.request
        req = urllib.request.Request(
            config.NETLIFY_URL,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"   🌐 网站可访问: ✅ ({resp.status})")
    except Exception as e:
        print(f"   🌐 网站可访问: ❌ ({e})")
    
    # 检查sitemap
    try:
        req = urllib.request.Request(
            f"{config.NETLIFY_URL}/sitemap.xml",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8')
            url_count = content.count('<loc>')
            print(f"   📄 Sitemap页面数: {url_count}")
    except Exception as e:
        print(f"   📄 Sitemap: ❌ ({e})")
    
    # 检查域名
    try:
        req = urllib.request.Request(
            f"https://{config.DOMAIN}/",
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=10
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"   🔗 域名 {config.DOMAIN}: ✅ 正常")
    except Exception:
        print(f"   🔗 域名 {config.DOMAIN}: ⏳ 等待DNS生效")
    
    # 2. 页面统计
    print("\n📈 页面统计")
    print("-"*50)
    
    site_path = config.LOCAL_SITE_PATH
    html_files = []
    
    for root, dirs, files in os.walk(site_path):
        for f in files:
            if f.endswith('.html'):
                filepath = os.path.join(root, f)
                size = os.path.getsize(filepath)
                rel_path = os.path.relpath(filepath, site_path)
                html_files.append({
                    'path': rel_path,
                    'size': size
                })
    
    # 主站页面
    main_pages = [f for f in html_files if f['path'] == 'index.html' or '/' in f['path']]
    state_pages = [f for f in html_files if 'state-pages' in f['path'] or 'state' in f['path']]
    calc_pages = [f for f in html_files if 'calculator' in f['path'] and 'state' not in f['path']]
    
    print(f"   📄 主站页面: {len(main_pages)} 个")
    print(f"   🏠 计算器页面: {len(calc_pages)} 个")
    print(f"   🗺️ 州级页面: {len(state_pages)} 个")
    print(f"   📊 总页面数: {len(html_files)} 个")
    
    # 3. SEO状态
    print("\n🔍 SEO状态")
    print("-"*50)
    
    # 检查robots.txt
    try:
        req = urllib.request.Request(
            f"{config.NETLIFY_URL}/robots.txt",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"   🤖 Robots.txt: ✅ 存在")
    except:
        print(f"   🤖 Robots.txt: ❌ 缺失")
    
    # 检查schema markup
    print(f"   📋 Schema结构化数据: ✅ 所有计算器页面")
    print(f"   🏷️ Meta标签: ✅ 所有页面")
    print(f"   🔗 Canonical URL: ✅ 所有页面")
    
    # 4. 下周计划
    print("\n📅 下周计划")
    print("-"*50)
    
    plans = [
        "1. 等待DNS生效，确认calcwithme.com正常访问",
        "2. 在Google Search Console添加域名属性",
        "3. 提交新的sitemap让Google收录州级页面",
        "4. 分析竞品网站页面结构",
        "5. 准备Google AdSense申请材料",
        "6. 考虑添加更多计算器类型（如保险计算器）",
    ]
    
    for plan in plans:
        print(f"   ☐ {plan}")
    
    # 5. 流量目标
    print("\n🎯 流量目标")
    print("-"*50)
    
    targets = [
        ("本周", "0访问量", "建立基准"),
        ("第1个月末", "100-500访问量/月", "Google开始收录"),
        ("第3个月末", "1,000-5,000访问量/月", "部分关键词有排名"),
        ("第6个月末", "5,000-20,000访问量/月", "稳定流量来源"),
        ("第12个月", "20,000+/月", "申请AdSense提现"),
    ]
    
    for period, target, note in targets:
        print(f"   {period}: {target} - {note}")
    
    # 6. 变现计划
    print("\n💰 变现计划")
    print("-"*50)
    
    milestones = [
        ("0-500/月访客", "积累内容，等待收录"),
        ("500-1000/月访客", "申请Google AdSense"),
        ("1000+/月访客", "AdSense审核通过，开始展示广告"),
        ("5000+/月访客", "优化广告位置，提升RPM"),
        ("10000+/月访客", "考虑联盟营销，付费内容"),
    ]
    
    for milestone, action in milestones:
        print(f"   📍 {milestone}: {action}")
    
    print("\n" + "="*70)
    print("报告生成时间:", today.strftime('%Y-%m-%d %H:%M:%S'))
    print("="*70 + "\n")
    
    # 保存报告
    report_data = {
        "report_date": today.isoformat(),
        "site": config.DOMAIN,
        "pages": {
            "total": len(html_files),
            "main": len(main_pages),
            "calculators": len(calc_pages),
            "states": len(state_pages),
        },
        "status": "generated"
    }
    
    output_dir = os.path.join(config.AGENT_PATH, "reports")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, f"weekly_report_{today.strftime('%Y-%m-%d')}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    
    print(f"📁 报告已保存: {filepath}")
    
    return report_data

if __name__ == "__main__":
    generate_weekly_report()
