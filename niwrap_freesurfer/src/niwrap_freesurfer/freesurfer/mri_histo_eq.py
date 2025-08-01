# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_HISTO_EQ_METADATA = Metadata(
    id="2b9bbd0abe6f9fc2ebfcea12661024fe348b3d7c.boutiques",
    name="mri_histo_eq",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriHistoEqParameters = typing.TypedDict('MriHistoEqParameters', {
    "__STYXTYPE__": typing.Literal["mri_histo_eq"],
    "input_volume_1": InputPathType,
    "input_volume_2": InputPathType,
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
        "mri_histo_eq": mri_histo_eq_cargs,
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
    }.get(t)


class MriHistoEqOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_histo_eq(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_histo_eq_params(
    input_volume_1: InputPathType,
    input_volume_2: InputPathType,
) -> MriHistoEqParameters:
    """
    Build parameters.
    
    Args:
        input_volume_1: Input volume 1.
        input_volume_2: Input volume 2.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_histo_eq",
        "input_volume_1": input_volume_1,
        "input_volume_2": input_volume_2,
    }
    return params


def mri_histo_eq_cargs(
    params: MriHistoEqParameters,
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
    cargs.append("mri_histo_eq")
    cargs.append(execution.input_file(params.get("input_volume_1")))
    cargs.append(execution.input_file(params.get("input_volume_2")))
    return cargs


def mri_histo_eq_outputs(
    params: MriHistoEqParameters,
    execution: Execution,
) -> MriHistoEqOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriHistoEqOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_histo_eq_execute(
    params: MriHistoEqParameters,
    execution: Execution,
) -> MriHistoEqOutputs:
    """
    MRI histogram equalization tool from Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriHistoEqOutputs`).
    """
    params = execution.params(params)
    cargs = mri_histo_eq_cargs(params, execution)
    ret = mri_histo_eq_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_histo_eq(
    input_volume_1: InputPathType,
    input_volume_2: InputPathType,
    runner: Runner | None = None,
) -> MriHistoEqOutputs:
    """
    MRI histogram equalization tool from Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume_1: Input volume 1.
        input_volume_2: Input volume 2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriHistoEqOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_HISTO_EQ_METADATA)
    params = mri_histo_eq_params(
        input_volume_1=input_volume_1,
        input_volume_2=input_volume_2,
    )
    return mri_histo_eq_execute(params, execution)


__all__ = [
    "MRI_HISTO_EQ_METADATA",
    "MriHistoEqOutputs",
    "MriHistoEqParameters",
    "mri_histo_eq",
    "mri_histo_eq_params",
]
