from hoshino.util import get_list_environ, get_environ, get_bool_environ
import os

"""这是一份实例配置文件

将其修改为你需要的配置，并将文件夹config_example重命名为config
"""

# hoshino监听的端口与ip
PORT = int(get_environ('PORT', 8000))
#HOST = get_environ('HOST', '0.0.0.0')  # Windows部署使用此条配置
# HOST = '172.17.0.1'   # linux + docker使用此条配置
# docker桥的ip可能随环境不同而有变化
# 使用这行命令`ip addr show docker0 | grep -Po 'inet \K[\d.]+'`查看你的docker桥ip
# HOST = '172.18.0.1'   # 阿里云的linux + docker多数情况是这样
HOST = '0.0.0.0'      # 开放公网访问使用此条配置（不安全）

DEBUG = True if os.environ.get('DEBUG') else False  # 调试模式

SUPERUSERS = get_list_environ('SUPERUSERS', [10000])  # 填写超级用户的QQ号，可填多个用半角逗号","隔开
NICKNAME = get_environ('NICKNAME', '')  # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称

COMMAND_START = {get_environ('COMMAND_START', '')}  # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()  # 命令分隔符（hoshino不需要该特性，保持为set()即可）

USE_CQPRO = True if os.environ.get('USE_CQPRO') else False  # 是否使用Pro版酷Q功能

# 发送图片的协议
# 可选 http, file, base64
# 建议Windows部署使用file协议
# 建议Linux部署配合本地web server使用http协议
# 如果你不清楚上面在说什么，请用base64协议（发送大图时可能会失败）
RES_PROTOCOL = get_environ('RES_PROTOCOL', 'file')
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = get_environ('RES_DIR', r'./res/')
# 使用http协议时需填写，原则上该url应指向RES_DIR目录
RES_URL = get_environ('RES_URL', 'http://127.0.0.1:5000/static/')

# 允许私聊
ALLOW_PRIVATE = get_bool_environ('ALLOW_PRIVATE', False)
# ICP内容
ICP_CONTENT = get_environ('ICP_CONTENT')
# 启用的模块
# 初次尝试部署时请先保持默认
# 如欲启用新模块，请认真阅读部署说明，逐个启用逐个配置
# 切忌一次性开启多个
MODULES_ON = {
    'auth_inspect',
    'bot_manager',
    'bot_manager_web',
    'dice',
    'group_master',
    # 'hourcall',
    # 'kancolle',
    # 'mikan',
    'pcrclanbattle',
    'priconne',
    # 'setu',
    # 'translate',
    # 'twitter',
    'yobot',
    #'mantra',
    'buy_potion_reminder',
    'shebot',
}
