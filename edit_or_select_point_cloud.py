import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("down_pc.ply")

print(" 1 - Редактирование облака точек с выделением отдельных точек")
print(" 2 - Выделение областей точек")
mode = int(input("Введите режим: "))

if mode == 1:
    o3d.visualization.draw_geometries_with_editing([pcd])
    # Ctrl+S - сохранить кропнутый файл
elif mode == 2:
    vis = o3d.visualization.VisualizerWithVertexSelection()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()
    idx = vis.get_picked_points()
    for i in idx:
        print(i.coord) # (i.index)
else:
    print("Ошибка, режим выбран неверно")
