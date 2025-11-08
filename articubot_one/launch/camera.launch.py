import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='camera_ros',
            executable='camera_node',
            output='screen',
            namespace='camera', # 토픽 이름 앞에 /camera/ 를 붙여줍니다. (예: /camera/image_raw)
            parameters=[{
                # 'image_size' 대신 'width'와 'height'를 사용해야 합니다.
                'width': 640,
                'height': 480,
                'framerate: 90.0'
                'camera_frame_id': 'camera_link_optical'
                # 프레임레이트(FPS)는 이 노드에서 직접 설정이 복잡할 수 있어 우선 제외했습니다.
                }]
    )
    ])