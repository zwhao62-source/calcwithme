"""
竞品分析器 - 学习成功网站的优秀策略
"""
import json
import sys
import os
import re
from datetime import datetime
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
except ImportError:
    print("Error: config.py not found")
    sys.exit(1)

class SimpleHTMLParser(HTMLParser):
    """简单HTML解析器"""
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_desc = ""
        self.h1_tags = []
        self.h2_tags = []
        self.in_title = False
        self.current_tag = ""
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            if attrs_dict.get("name") == "description":
                self.meta_desc = attrs_dict.get("content", "")
        if tag == "h1":
            self.h1_tags.append("")
            self.in_h1 = True
        if tag == "h2":
            self.h2_tags.append("")
            self.in_h2 = True
            
    def handle_data(self, data):
        data = data.strip()
        if self.in_title:
            self.title += data
            self.in_title = False
        if hasattr(self, 'in_h1') and self.in_h1 and self.h1_tags:
            self.h1_tags[-1] += data
            self.in_h1 = False
        if hasattr(self, 'in_h2') and self.in_h2 and self.h2_tags:
            self.h2_tags[-1] += data
            self.in_h2 = False
            
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False
        if tag == "h2":
            self.in_h2 = False

def analyze_page(url, name):
    """分析单个页面"""
    print(f"\n分析: {name}")
    print(f"URL: {url}")
    print("-" * 40)
    
    try:
        import urllib.request
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8', errors='ignore')
            
            parser = SimpleHTMLParser()
            parser.feed(content)
            
            print(f"  ✅ 状态: 成功")
            print(f"  📝 Title: {parser.title[:80] if parser.title else 'N/A'}...")
            print(f"  📄 Meta描述: {parser.meta_desc[:100] if parser.meta_desc else 'N/A'}...")
            print(f"  🏷️ H1标签数: {len(parser.h1_tags)}")
            if parser.h1_tags:
                print(f"     H1: {parser.h1_tags[0][:60]}")
            print(f"  📑 H2标签数: {len(parser.h2_tags)}")
            if parser.h2_tags:
                for h2 in parser.h2_tags[:5]:
                    if h2.strip():
                        print(f"     H2: {h2[:60]}")
            
            # 分析页面结构
            print(f"\n  📊 页面分析:")
            calc_links = len(re.findall(r'calculator', content.lower()))
            tool_links = len(re.findall(r'tool', content.lower()))
            print(f"     'calculator' 出现次数: {calc_links}")
            print(f"     'tool' 出现次数: {tool_links}")
            print(f"     页面大小: {len(content)/1024:.1f} KB")
            
            # 提取链接
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            external_links = [l for l in links if l.startswith('http') and name not in l]
            internal_links = [l for l in links if not l.startswith('http')]
            print(f"     内链数: {len(internal_links)}")
            print(f"     外链数: {len(external_links)}")
            
            return {
                "name": name,
                "url": url,
                "title": parser.title,
                "meta_desc": parser.meta_desc,
                "h1_count": len(parser.h1_tags),
                "h2_count": len(parser.h2_tags),
                "status": "success"
            }
            
    except Exception as e:
        print(f"  ❌ 失败: {e}")
        return {
            "name": name,
            "url": url,
            "status": "error",
            "error": str(e)
        }

def generate_seo_recommendations(analysis_results):
    """根据竞品分析生成SEO建议"""
    print("\n" + "="*50)
    print("📋 SEO 优化建议")
    print("="*50)
    
    recommendations = []
    
    # 分析成功网站的共同特点
    successful_sites = [r for r in analysis_results if r.get("status") == "success"]
    
    if successful_sites:
        # 提取共同模式
        common_titles = []
        for site in successful_sites:
            if site.get("title"):
                common_titles.append(site["title"])
        
        print("\n🎯 学习到的成功模式:")
        print("   1. Title格式: '[计算器名称] - Free [类型] Calculator | SiteName'")
        print("   2. Meta描述: 包含关键词 + 用途 + 免费声明")
        print("   3. 每个页面专注一个计算器")
        print("   4. FAQ内容部分增加SEO深度")
        print("   5. 相关计算器内链丰富")
        
        print("\n💡 针对CalcWithMe的优化建议:")
        recommendations = [
            "1. 为每个计算器页面添加更详细的FAQ部分",
            "2. 标题改为更具体的格式：'Mortgage Calculator - Calculate Monthly Payments | CalcWithMe'",
            "3. 每个页面增加'How to use'和'Related Calculators'部分",
            "4. 添加更多长尾关键词页面",
            "5. 考虑增加计算器对比页面（如：30年 vs 15年贷款）",
            "6. 为每个州创建独立的房贷计算器页面",
        ]
        
        for rec in recommendations:
            print(f"   {rec}")
    
    return recommendations

def run_analysis():
    """运行竞品分析"""
    print("\n" + "="*60)
    print("🔍 CalcWithMe 竞品分析报告")
    print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)
    
    results = []
    
    for name, info in config.COMPETITORS.items():
        result = analyze_page(info["url"], name)
        results.append(result)
        print()
    
    # 生成优化建议
    recommendations = generate_seo_recommendations(results)
    
    # 保存报告
    report = {
        "timestamp": datetime.now().isoformat(),
        "site": config.DOMAIN,
        "competitors_analyzed": len(results),
        "results": results,
        "recommendations": recommendations
    }
    
    output_dir = os.path.join(config.AGENT_PATH, "reports")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, "competitor_analysis.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n📁 报告已保存: {filepath}")
    print("="*60 + "\n")
    
    return report

if __name__ == "__main__":
    run_analysis()
