import nibabel as nib
import os
from pathlib import Path
import numpy as np

# 输入和输出文件夹路径
input_folder = Path("D:/yang/YangCazz/Vessels/vesselFM/data/raw")
output_folder = Path("D:/yang/YangCazz/Vessels/vesselFM/data/output")

# 获取所有输入和输出文件
input_files = list(input_folder.glob("*.nii.gz"))
output_files = list(output_folder.glob("*_pred.nii.gz"))

print(f"输入文件数量: {len(input_files)}")
print(f"输出文件数量: {len(output_files)}")

# 对每对文件进行比较
for in_file in input_files:
    base_name = in_file.stem.split('.')[0]
    out_file = output_folder / f"{base_name}_pred.nii.gz"
    
    if out_file.exists():
        # 加载图像
        in_img = nib.load(in_file)
        out_img = nib.load(out_file)
        
        # 获取尺寸
        in_shape = in_img.shape
        out_shape = out_img.shape
        
        # 获取体素大小
        in_voxel = in_img.header.get_zooms()
        out_voxel = out_img.header.get_zooms()
        
        print(f"\n文件: {base_name}")
        print(f"输入尺寸: {in_shape}")
        print(f"输出尺寸: {out_shape}")
        print(f"输入体素大小: {in_voxel}")
        print(f"输出体素大小: {out_voxel}")
        
        # 详细检查输出图像的header信息
        print("\n输出图像详细信息:")
        print(f"数据类型: {out_img.get_data_dtype()}")
        print(f"仿射矩阵:\n{out_img.affine}")
        
        # 检查差异
        if in_shape != out_shape:
            print("尺寸不匹配!")
        if in_voxel != out_voxel:
            print("体素大小不匹配!")
            print(f"输入体素大小: {in_voxel}")
            print(f"输出体素大小: {out_voxel}")
    else:
        print(f"\n未找到对应的输出文件: {out_file}") 