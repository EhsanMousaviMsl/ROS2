from setuptools import setup

package_name = 'vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ehsan',
    maintainer_email='57229151+EhsanMousaviMsl@users.noreply.github.com',
    description='TODO: Vision Task',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_talker = vision.vision_pub:main',
            'vision_listener = vision.vision_sub:main',
        ],
    },
)
