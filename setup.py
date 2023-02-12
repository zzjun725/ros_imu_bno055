import os
from glob import glob
from setuptools import setup

#from distutils.core import setup
#from catkin_pkg.python_setup import generate_distutils_setup

package_name = 'ros_imu_bno055'

setup(
        packages=['ros_imu_bno055'],
        package_dir={'': 'include'},
        data_files=[
            (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
            ]
        )
#setup_args = generate_distutils_setup(
 #   packages=['ros_imu_bno055'],
  #  package_dir={'': 'include'},
#)

#setup(**setup_args)
