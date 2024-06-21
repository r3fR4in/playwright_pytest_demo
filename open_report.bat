@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
cd ..

@REM 拷贝进生成报告根目录下，allure-report改成报告文件夹名
allure open allure-report
