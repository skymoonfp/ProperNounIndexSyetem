# ProperNounIndexSystem


===========================


######功能描述

    1. 书籍、专名的录入和查询
    
    2. 练手
    

######环境依赖

    1. Python 3
    
    2. Django
    
    3. MySQL


######部署步骤

    1. 和Django放置在同一目录下
    
    2. 运行服务器端：
        python manage.py runserver
    
    3. 更新数据库：
        python manage.py makemigrations
        python manage.py migrate


######目录结构描述

    ├── Readme.md                   // help
    ├── ProperNounIndexSystem            
    │   ├── __init__.py
    │   ├── activator.py            // 自动路由系统
    │   ├── settings.py
    │   ├── urls.py                
    │   └── wsgi.py
    ├── Templates                   
    │   ├── master
    │   │   ├── general.html        // 一般模版
    │   │   └── operation_page.html // 主功能页模版
    │   ├── static
    │   │   ├── css                 // css配置文件夹
    │   │   │   ├── basic_tab.css
    │   │   │   ├── easyui.css
    │   │   │   ├── form.css
    │   │   │   ├── fullscreen.css
    │   │   │   ├── operation_tab.css
    │   │   │   └── ...
    │   │   ├── img                 // 图片文件夹
    │   │   │   └── ...
    │   │   └── js                  // javascript文件夹
    │   │       ├── jQuery-3.4.1.js
    │   │       ├── jquery.cookie.js
    │   │       ├── jquery.easyui.min.js
    │   │       ├── basic_tab.js
    │   │       └── ...
    │   ├── __init__.py
    │   ├── favicon.ico             // logo
    │   ├── index.html              // 主页
    │   ├── login.html              // 登录页
    │   ├── register.html           // 注册页
    │   ├── books_input.html        // 书籍录入页
    │   ├── propernoun_input.html   // 专名录入页
    │   └── search.html             // 查询页
    ├── Admin                       // 管理员app
    │   └── ...
    ├── Main                        // 主功能app
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── templatetags
    │   │   └── ...
    │   ├── utility
    │   │   ├── helper.py
    │   │   ├── html_helper.py
    │   │   └── ...
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py                 // 运行服务器端
    ├── db.sqlite3                // 自带数据库
    └── ... 
    
    
######V1.0.0 版本内容更新

    1. 新功能     aaaaaaaaa
    2. 新功能     bbbbbbbbb
    3. 新功能     ccccccccc
    4. 新功能     ddddddddd


######历史版本

    V1.0.0


######更新链接

    https://github.com/skymoonfp/ProperNounIndexSyetem


######作者列表
    
    心齋觀化


######联系方式

    <心齋觀化>954918@qq.com
