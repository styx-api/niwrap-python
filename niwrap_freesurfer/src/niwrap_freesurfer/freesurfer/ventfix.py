# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VENTFIX_METADATA = Metadata(
    id="e71901d7b79bb5fd53811d2c81452b885bbecc11.boutiques",
    name="ventfix",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


VentfixParameters = typing.TypedDict('VentfixParameters', {
    "__STYX_TYPE__": typing.Literal["ventfix"],
    "subject_dir": str,
    "option1": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "ventfix": ventfix_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "ventfix": ventfix_outputs,
    }.get(t)


class VentfixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ventfix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixed_ventricles: OutputPathType
    """Output image with fixed ventricles"""


def ventfix_params(
    subject_dir: str,
    option1: str | None = None,
) -> VentfixParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Path to the subject's directory containing MRI scans.
        option1: Description of option 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ventfix",
        "subject_dir": subject_dir,
    }
    if option1 is not None:
        params["option1"] = option1
    return params


def ventfix_cargs(
    params: VentfixParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("ventfix")
    cargs.append(params.get("subject_dir"))
    if params.get("option1") is not None:
        cargs.extend([
            "--option1",
            params.get("option1")
        ])
    return cargs


def ventfix_outputs(
    params: VentfixParameters,
    execution: Execution,
) -> VentfixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VentfixOutputs(
        root=execution.output_file("."),
        fixed_ventricles=execution.output_file(params.get("subject_dir") + "/fixed_ventricles.nii.gz"),
    )
    return ret


def ventfix_execute(
    params: VentfixParameters,
    execution: Execution,
) -> VentfixOutputs:
    """
    Tool for fixing ventricles in MRI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VentfixOutputs`).
    """
    params = execution.params(params)
    cargs = ventfix_cargs(params, execution)
    ret = ventfix_outputs(params, execution)
    execution.run(cargs)
    return ret


def ventfix(
    subject_dir: str,
    option1: str | None = None,
    runner: Runner | None = None,
) -> VentfixOutputs:
    """
    Tool for fixing ventricles in MRI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the subject's directory containing MRI scans.
        option1: Description of option 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VentfixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VENTFIX_METADATA)
    params = ventfix_params(
        subject_dir=subject_dir,
        option1=option1,
    )
    return ventfix_execute(params, execution)


__all__ = [
    "VENTFIX_METADATA",
    "VentfixOutputs",
    "VentfixParameters",
    "ventfix",
    "ventfix_params",
]
