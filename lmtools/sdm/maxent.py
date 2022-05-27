"""Module containing MaxEnt constants."""
import os
import subprocess


# .....................................................................................
try:
    JAVA_CMD = os.environ['JAVA_CMD']
except KeyError:
    JAVA_CMD = 'java'
try:
    JAVA_OPTS = os.environ['JAVA_OPTIONS']
except KeyError:
    JAVA_OPTS = ''
MAXENT_JAR = os.environ['MAXENT_JAR']
MAXENT_MODEL_TOOL = 'density.MaxEnt'
MAXENT_PROJECT_TOOL = 'density.Project'
MAXENT_CONVERT_TOOL = 'density.Convert'
MAXENT_VERSION = os.environ['MAXENT_VERSION']

DEFAULT_MAXENT_OPTIONS = 'nowarnings nocache autorun -z'


# .....................................................................................
def create_maxent_model(
    points_filename,
    layer_dir,
    work_dir='.',
    maxent_arguments=DEFAULT_MAXENT_OPTIONS
):
    """Run Maxent."""
    model_command = ' '.join(
        [
            JAVA_CMD,
            JAVA_OPTS,
            MAXENT_JAR,
            MAXENT_MODEL_TOOL,
            f'-s {points_filename}',
            f'-o {work_dir}',
            f'-e {layer_dir}',
            maxent_arguments
        ]
    )
    subprocess.run(model_command)
