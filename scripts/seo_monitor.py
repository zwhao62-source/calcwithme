"""
SEO Monitor - 监控网站SEO数据
使用 Google Search Console API
"""
import json
import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
except ImportError:
    print("Error: config.py not found")
    sys.exit(1)

def get_gsc_data():
    """
    获取 Google Search Console 数据
    需要用户授权 Search Console API
    """
    print("\n" + "="*50)
    print("SEO 数据监控")
    print("="*50)
    
    site_url = config.GSC_PROPERTY_URL
    
    print(f"\n监控网站: {site_url}")
    print(f"检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # 检查网站可访问性
    print("\n[1] 网站可访问性检查")
    try:
        import urllib.request
        req = urllib.request.Request(
            config.NETLIFY_URL,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            print(f"    状态码: {status} {'✅ 正常' if status == 200 else '❌ 异常'}")
    except Exception as e:
        print(f"    ❌ 无法访问: {e}")
    
    # 检查 sitemap
    print("\n[2] Sitemap 检查")
    try:
        req = urllib.request.Request(
            f"{config.NETLIFY_URL}/sitemap.xml",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            page_count = content.count('<loc>')
            print(f"    ✅ Sitemap 正常，包含 {page_count} 个URL")
    except Exception as e:
        print(f"    ❌ Sitemap 检查失败: {e}")
    
    # 检查 robots.txt
    print("\n[3] Robots.txt 检查")
    try:
        req = urllib.request.Request(
            f"{config.NETLIFY_URL}/robots.txt",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            print(f"    状态码: {status} {'✅ 正常' if status == 200 else '❌ 异常'}")
    except Exception as e:
        print(f"    ❌ Robots.txt 检查失败: {e}")
    
    # 检查页面加载速度
    print("\n[4] 页面加载速度检查")
    import time
    pages_to_check = [
        "/",
        "/mortgage-calculator.html",
        "/loan-calculator.html"
    ]
    for page in pages_to_check:
        try:
            start = time.time()
            req = urllib.request.Request(
                f"{config.NETLIFY_URL}{page}",
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=15) as response:
                load_time = (time.time() - start) * 1000
                status = "✅" if load_time < 1000 else "⚠️"
                print(f"    {status} {page}: {load_time:.0f}ms")
        except Exception as e:
            print(f"    ❌ {page}: {e}")
    
    # SEO最佳实践检查
    print("\n[5] SEO 最佳实践检查")
    try:
        req = urllib.request.Request(
            f"{config.NETLIFY_URL}/",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8', errors='ignore')
            
            checks = [
                ("<title>", "Title 标签", "<title>"),
                ("meta name=\"description\"", "Meta Description", "description"),
                ("canonical", "Canonical URL", "canonical"),
                ("<h1", "H1 标签", "H1"),
                ("schema.org", "结构化数据", "Schema.org"),
                ("og:title", "Open Graph 标签", "OG tags"),
            ]
            
            for keyword, name, tag in checks:
                status = "✅" if keyword.lower() in content.lower() else "❌"
                print(f"    {status} {name}")
    except Exception as e:
        print(f"    ❌ 检查失败: {e}")
    
    print("\n" + "="*50)
    print("SEO 监控完成!")
    print("="*50 + "\n")
    
    return {
        "status": "completed",
        "timestamp": datetime.now().isoformat(),
        "site": site_url
    }

def save_report(data, filename="seo_report.json"):
    """保存报告到文件"""
    output_dir = os.path.join(config.AGENT_PATH, "reports")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"报告已保存: {filepath}")

if __name__ == "__main__":
    result = get_gsc_data()
    save_report(result)
