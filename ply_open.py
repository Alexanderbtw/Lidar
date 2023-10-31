import numpy as np
import laspy as lp
import trimesh
import open3d as o3d

# region Конвертация в PLY
# las_file = lp.read("example_cloud.las")
#
# points = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()
# colors = np.vstack((las_file.red, las_file.green, las_file.blue)).transpose() / 255.0
#
# mesh = trimesh.Trimesh(vertices=points, vertex_colors=colors, process=False)
#
# mesh.export("example_cloud.ply")
# endregion

# region Find Normals (Stupid)
# pc_ply = o3d.io.read_point_cloud("example_cloud.ply")
#
# points = pc_ply.points
# colors = pc_ply.colors
# pc_ply.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
#
# mesh = trimesh.Trimesh(vertices=points, vertex_colors=colors, vertex_normals=pc_ply.normals, process=False)
# mesh.export("outfile_normals.ply")
#
# normals = np.asarray(pc_ply.normals)
# print(normals[:10])
# endregion

# region Find Normals (Mesh)
# mesh = trimesh.load("example_cloud.ply")
#
# mesh.compute_normal()
# normals = mesh.vertex_normals
#
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(mesh.vertices)
#
# line_set = o3d.geometry.LineSet.create_from_triangle_mesh(mesh)
# line_set.normals = o3d.utility.Vector3dVector(normals)
#
# o3d.visualization.draw_geometries([pcd, line_set], point_show_normals=True)
# endregion

pc_ply = o3d.io.read_point_cloud("example_cloud.ply")

# region Select
roi = [(84.8, 86.6), (97.25, 101.35), (1, 5)]  # [(x_min, x_max), (y_min, y_max), (z_min, z_max)]
bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound=np.array([roi[0][0], roi[1][0], roi[2][0]]),
                                           max_bound=np.array([roi[0][1], roi[1][1], roi[2][1]]))

cropped_cloud = pc_ply.crop(bbox)
cropped_cloud.paint_uniform_color([0, 0, 1])
o3d.visualization.draw_geometries([cropped_cloud, pc_ply])
# endregion

#region Voxel Downsampling
# down_pc = pc_ply.voxel_down_sample(voxel_size=0.5)
# o3d.visualization.draw_geometries([down_pc])
# o3d.io.write_point_cloud("down_pc.ply", down_pc)
#endregion

# o3d.visualization.draw_geometries([pc_ply], point_show_normal=False)