import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
            launch.actions.DeclareLaunchArgument('operation_mode', default_value='NDOF'),
            launch.actions.DeclareLaunchArgument('operation_mode', default_value='NDOF'),
            launch_ros.actions.Node(
                package='ros_imu_bno055',
                executable='imu_calibration.py',
                name='ros_imu_bno055_calibration_node',
                ),
        ])

