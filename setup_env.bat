@echo off
echo ================================
echo Gemini LangChain 环境安装脚本
echo ================================
echo.

REM 检查 environment.yml 是否存在
if not exist environment.yml (
    echo 未找到 environment.yml 文件！
    echo 请确认本脚本和 environment.yml 在同一个项目文件夹中。
    pause
    exit /b
)

echo 正在检查 ai 环境是否已经存在...
conda env list | findstr /C:"ai" >nul

if %errorlevel%==0 (
    echo 检测到 ai 环境已存在，开始更新环境...
    call conda env update -n ai -f environment.yml --prune
) else (
    echo 未检测到 ai 环境，开始创建环境...
    call conda env create -f environment.yml
)

echo.
echo 正在激活 ai 环境...
call conda activate ai

echo.
echo 当前 Python 版本：
python --version

echo.
echo 环境安装/更新完成！
echo 之后可以运行 run.bat 或执行 python main.py 启动项目。
echo.

pause