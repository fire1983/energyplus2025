import os
from pathlib import Path
import subprocess

def run_energyplus_simulation():
    # EnergyPlus安装路径
    eplus_path = r"D:\EnergyPlusV24-2-0"
    # 工作目录路径
    work_dir = os.path.dirname(os.path.abspath(__file__))
    # IDF文件路径
    idf_path = os.path.join(work_dir, "mall.idf")
    # 气象文件路径
    epw_path = os.path.join(work_dir, "CHN_Guangzhou.epw")
    # 输出目录
    output_dir = os.path.join(work_dir, "output")
    
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)
    
    # 构建EnergyPlus命令
    eplus_exe = os.path.join(eplus_path, "energyplus.exe")
    cmd = [
        eplus_exe,
        "-w", epw_path,  # 气象文件
        "-d", output_dir,  # 输出目录
        "-r",  # 运行模式
        idf_path  # 输入文件
    ]
    
    try:
        # 运行EnergyPlus模拟
        print("开始运行EnergyPlus模拟...")
        subprocess.run(cmd, check=True)
        print("模拟完成！")
        print(f"输出文件保存在: {output_dir}")
        
    except subprocess.CalledProcessError as e:
        print(f"模拟过程中出错: {e}")
        return False
    
    return True

if __name__ == "__main__":
    run_energyplus_simulation() 