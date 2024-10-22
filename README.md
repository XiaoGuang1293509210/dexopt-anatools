# AIproject

AI燥起来
日志分析工具

输入格式：
    数据库文件：本地路径，不输入默认/sqlite目录下第一个.db文件
    log文件：  本地路径，不输入则默认当前文件下第一个txt文件
    关键词：   key1,key2,key3   例：System,Error,2024   分析：这将会把log中包含'System'或'Error'或'2024'的log打印出来
    排除关键词：例：key1,key2,key3
    起止日期：  XX-XX 例：10-15 
    起止时间：  XX:XX:XX.XXX 例：02:36:57.020
    进程、线程：XXXX XXXX XXXX 例：1974 1988
    log等级:  'ALL','V:Verbose,调试信息', 'D:Debug,调试信息', 'I:Info,一般信息', 'W:Warn', 'E:ERROR'

功能开发：
    *日志过滤功能：
        当前功能：多个关键词检索，日期、时间、进程、线程、log等级过滤、组合检索
    *日志分析功能：
        当前功能：简单打印, 弹出相似日志总结
    *输出编辑与保存功能：
        当前功能：输出后的日志可以进行编辑，分析后的日志可以保存到文件
    *UI：
        当前功能：简单显示

使用方法:
    windows:
        将打包好的exe文件(源代码的dist文件夹下)放在同一个目录下,直接使用即可.
        如果不想输入文件路径的话,日志放在同一文件夹下,数据库文件放在sqlite子文件夹下
    Linux:
        python3 mLogSqlite.py  #运行数据库工具
        python3 mLogMain.py    #运行log分析工具