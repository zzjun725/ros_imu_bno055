import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('serial_port', default_value='/dev/ttyUSB0'),
        launch.actions.DeclareLaunchArgument('frame_id', default_value='imu_link'),
        launch.actions.DeclareLaunchArgument('operation_mode', default_value='NDOF'),
        launch.actions.DeclareLaunchArgument('oscillator', default_value='EXTERNAL'),
        launch.actions.DeclareLaunchArgument('reset_orientation', default_value='true'),
        launch.actions.DeclareLaunchArgument('frequency', default_value='50'),
        launch.actions.DeclareLaunchArgument('use_magnetometer', default_value='false'),
        launch.actions.DeclareLaunchArgument('use_temperature', default_value='false'),
        Node(
            package='ros_imu_bno055',
            executable='imu_ros.py',
            name='ros_imu_bno055_node',
            output='screen',
            ),
        ])

