"""Module containing MaxEnt constants."""
import os
import subprocess


# .....................................................................................
JAVA_CMD = os.environ['JAVA_CMD']
JAVA_OPTS = os.environ['JAVA_OPTIONS']
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
            ME_CMD,
            MAXENT_MODEL_TOOL,
            f'-s {points_filename}',
            f'-o {work_dir}',
            f'-e {layer_dir}',
            maxent_arguments
        ]
    )
    model_proc = subprocess.Popen(
        model_command,
        shell=True,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )
    while model_proc.poll() is None:
        sleep(10)
