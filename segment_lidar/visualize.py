import open3d as o3d
import numpy as np

def visualize(points):

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    pcd.colors = o3d.utility.Vector3dVector(points[:, 3:6] / 255)

                # Visualize the point cloud and save the image
    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(visible=True, width=1000, height=700)
    vis.add_geometry(pcd)
    render = vis.get_render_option()
    render.point_size = 1
    render.background_color = np.asarray([0, 0, 0])
    vis.run()
    vis.destroy_window()