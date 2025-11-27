import http.server
import socketserver
import webbrowser
import os

# 设置端口
PORT = 8000

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 打印启动信息
print(f"\n🚀 烟花秀网页服务器启动中...")
print(f"📁 服务目录: {current_dir}")
print(f"🌐 本地访问地址: http://localhost:{PORT}")
print(f"📱 手机访问地址: http://[你的电脑IP]:{PORT}")
print(f"💡 提示: 在微信中直接打开上述手机访问地址即可查看烟花秀")
print(f"\n按 Ctrl+C 停止服务器\n")

# 启动HTTP服务器
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
        httpd.shutdown()