from niwrap_mrtrix3tissue import mrtrix3tissue
from niwrap_niftyreg import niftyreg
from niwrap_fastsurfer import fastsurfer
from niwrap_fsl import fsl
from niwrap_workbench import workbench
from niwrap_afni import afni
from niwrap_mrtrix import mrtrix
from niwrap_ants import ants
from niwrap_c3d import c3d
from niwrap_freesurfer import freesurfer
from niwrap_greedy import greedy
from niwrap_dcm2niix import dcm2niix
from styxdefs import *  # Reexport styxdefs


def _create_runner(module_name, runner_class, *args, **kwargs):
    """
    Helper function to create and set a runner from a module.
    
    Args:
        module_name: Name of the module to import (without 'styx' prefix)
        runner_class: Name of the runner class to instantiate
        *args, **kwargs: Arguments to pass to the runner constructor
    
    Raises:
        ImportError: If the module cannot be imported
    """
    try:
        module = __import__(f"styx{module_name.lower()}")
        runner = getattr(module, f"{runner_class}Runner")
        set_global_runner(runner(*args, **kwargs))
    except ImportError:
        package = f"styx{module_name.lower()}"
        raise ImportError(f"{module_name} runner not available. Install with `pip install {package}`")


def use_docker(*args, **kwargs):
    """Set Docker as the global runner."""
    _create_runner("docker", "Docker", *args, **kwargs)


def use_singularity(*args, **kwargs):
    """Set Singularity as the global runner."""
    _create_runner("singularity", "Singularity", *args, **kwargs)


def use_graph(*args, **kwargs):
    """Set Graph as the global runner."""
    _create_runner("graph", "Graph", *args, **kwargs)