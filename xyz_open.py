import laspy as lp
import open3d as o3d
import numpy as np

#region Конвертация в XYZ с сохранением цвета
# output_path = 'example_cloud.las'
#
# pc_las = lp.read(output_path)
#
# with open('example_cloud.xyz', 'w') as pc_xyz:
#     for i in range(len(pc_las)):
#         x = pc_las.x[i]
#         y = pc_las.y[i]
#         z = pc_las.z[i]
#         r = pc_las.red[i] / 65535
#         g = pc_las.green[i] / 65535
#         b = pc_las.blue[i] / 65535
#         pc_xyz.write(f"{x} {y} {z} {r} {g} {b}\n")
# endregion

#region Don't working
# points = np.vstack((pc_las.X, pc_las.Y, pc_las.Z)).transpose()
# colors = np.vstack((pc_las.red, pc_las.green, pc_las.blue)).transpose()
#
# np.savetxt("example_cloud_wclrs.xyz", np.hstack((points, colors)), delimiter=" ", fmt="%f %f %f %d %d %d")
#endregion

pc_xyz = o3d.io.read_point_cloud("example_cloud.xyz", format='xyzrgb')

o3d.visualization.draw_geometries([pc_xyz])