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
    model_command = [JAVA_CMD]
    if len(JAVA_OPTS) > 0:
        model_command.append(JAVA_OPTS)
    model_command.extend(
        [
            '-cp',
            MAXENT_JAR,
            MAXENT_MODEL_TOOL,
            f'samplesfile={points_filename}',
            '-e',
            layer_dir,
            '-o',
            work_dir
        ]
    )

    model_command.extend(maxent_arguments.split(' '))
    subprocess.run(model_command, capture_output=True, check=True)
