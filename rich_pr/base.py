from rich import print as rprint
from rich.console import Console

x = {
    'name': 'MedusaSorcerer',
    'blog': 'https://juejin.im/user/2805609406139950',
    'locals()': '返回当前位置全部局部变量, 并以字典的方式展示',
    'python': '一种简单直接的开发语言, 好用就对了',
}

console = Console(width=20)

style = 'bold white on blue blink'
console.print('A', style=style, justify='right')
