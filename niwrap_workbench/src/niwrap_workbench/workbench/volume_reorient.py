# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_REORIENT_METADATA = Metadata(
    id="64a53eb5b1219001c981ca04003ea946af095932.boutiques",
    name="volume-reorient",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


VolumeReorientParameters = typing.TypedDict('VolumeReorientParameters', {
    "__STYXTYPE__": typing.Literal["volume-reorient"],
    "volume": InputPathType,
    "orient_string": str,
    "volume_out": str,
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
        "volume-reorient": volume_reorient_cargs,
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


class VolumeReorientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_reorient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_reorient_params(
    volume: InputPathType,
    orient_string: str,
    volume_out: str,
) -> VolumeReorientParameters:
    """
    Build parameters.
    
    Args:
        volume: the volume to reorient.
        orient_string: the desired orientation.
        volume_out: out - the reoriented volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-reorient",
        "volume": volume,
        "orient_string": orient_string,
        "volume_out": volume_out,
    }
    return params


def volume_reorient_cargs(
    params: VolumeReorientParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-reorient")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(params.get("orient_string"))
    cargs.append(params.get("volume_out"))
    return cargs


def volume_reorient_outputs(
    params: VolumeReorientParameters,
    execution: Execution,
) -> VolumeReorientOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeReorientOutputs(
        root=execution.output_file("."),
    )
    return ret


def volume_reorient_execute(
    params: VolumeReorientParameters,
    execution: Execution,
) -> VolumeReorientOutputs:
    """
    Change voxel order of a volume file.
    
    Changes the voxel order and the header spacing/origin information such that
    the value of any spatial point is unchanged. Orientation strings look like
    'LPI', which means first index is left to right, second is posterior to
    anterior, and third is inferior to superior. The valid characters are:
    
    L left to right
    R right to left
    P posterior to anterior
    A anterior to posterior
    I inferior to superior
    S superior to inferior.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeReorientOutputs`).
    """
    params = execution.params(params)
    cargs = volume_reorient_cargs(params, execution)
    ret = volume_reorient_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_reorient(
    volume: InputPathType,
    orient_string: str,
    volume_out: str,
    runner: Runner | None = None,
) -> VolumeReorientOutputs:
    """
    Change voxel order of a volume file.
    
    Changes the voxel order and the header spacing/origin information such that
    the value of any spatial point is unchanged. Orientation strings look like
    'LPI', which means first index is left to right, second is posterior to
    anterior, and third is inferior to superior. The valid characters are:
    
    L left to right
    R right to left
    P posterior to anterior
    A anterior to posterior
    I inferior to superior
    S superior to inferior.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the volume to reorient.
        orient_string: the desired orientation.
        volume_out: out - the reoriented volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeReorientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REORIENT_METADATA)
    params = volume_reorient_params(
        volume=volume,
        orient_string=orient_string,
        volume_out=volume_out,
    )
    return volume_reorient_execute(params, execution)


__all__ = [
    "VOLUME_REORIENT_METADATA",
    "VolumeReorientOutputs",
    "VolumeReorientParameters",
    "volume_reorient",
    "volume_reorient_params",
]
