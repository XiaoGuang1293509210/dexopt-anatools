# AIproject

AI燥起来
日志分析工具
截止日期：2024.10.20 周日

输入格式：
路径：本地路径，不输入则默认第一个txt文件
cmd：'key1:value1', 'key2:value2', ..., 'keyN:valueN'，
    例：'System:System','System:update','key1:Error:','key2:0'
    分析：这将会把log中包含'System'和'update'或'Error'或'0'的log打印出来
输入不能出现的关键词：例：key1,key2,key3
起始日期、截止日期:XX-XX 例：10-15 
起始时间、截止时间：XX:XX:XX.XXX 例：02:36:57.020
进程、线程：XXXX XXXX XXXX 例：1974 1988
选择log等级:'','V:Verbose,调试信息', 'D:Debug,调试信息', 'I:Info,一般信息', 'W:Warn', 'E:ERROR'

功能开发：
    *日志过滤功能：
        当前功能：多个关键词检索，日期、时间、进程、线程、log等级过滤
        后续研发功能：组合检索
    *日志分析功能：
        当前功能：简单打印
        后续研发功能：弹出相似日志总结
    *UI：
        当前功能：简单显示
        后续研发功能：满足所有功能显示即可
