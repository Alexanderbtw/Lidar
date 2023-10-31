import laspy as lp
import open3d as o3d
import numpy as np
import gdown

# cloud_file_url = "https://drive.google.com/file/d/1DUEy-gayYudkuJUou_cfNmPAmwdbbgml/view?usp=share_link"
output_path = 'example_cloud.las'

#gdown.download(cloud_file_url, output_path, quiet=False, fuzzy=True)

pc_las = lp.read(output_path)

points = np.vstack((pc_las.X, pc_las.Y, pc_las.Z)).transpose()
colors = np.vstack((pc_las.red, pc_las.green, pc_las.blue)).transpose()

#region Later
# buildings = lp.create(point_format=pc_las.header.point_format, file_version=pc_las.header.version)
# buildings.points = pc_las.points[pc_las.classification == 6]
#endregion

geom = o3d.geometry.PointCloud()

geom.points = o3d.utility.Vector3dVector(points)
geom.colors = o3d.utility.Vector3dVector(colors / 65535)

#region Normals numpy
# geom.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
# xyz = np.asarray(geom.points)
# normals = np.asarray(geom.normals)
# endregion

o3d.visualization.draw_geometries([geom])