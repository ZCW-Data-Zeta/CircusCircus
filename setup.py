from setuptools import setup

setup(
    name='forum',
    packages=['forum/', 'forum/forum_IM'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)