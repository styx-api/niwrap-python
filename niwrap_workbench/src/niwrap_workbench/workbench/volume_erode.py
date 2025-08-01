# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_ERODE_METADATA = Metadata(
    id="4ac0d4ccac9419431d55b6e2a0cd4ad69eed4f20.boutiques",
    name="volume-erode",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


VolumeErodeParameters = typing.TypedDict('VolumeErodeParameters', {
    "__STYXTYPE__": typing.Literal["volume-erode"],
    "volume": InputPathType,
    "distance": float,
    "volume_out": str,
    "opt_roi_roi_volume": typing.NotRequired[InputPathType | None],
    "opt_subvolume_subvol": typing.NotRequired[str | None],
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
        "volume-erode": volume_erode_cargs,
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
        "volume-erode": volume_erode_outputs,
    }.get(t)


class VolumeErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_erode_params(
    volume: InputPathType,
    distance: float,
    volume_out: str,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
) -> VolumeErodeParameters:
    """
    Build parameters.
    
    Args:
        volume: the volume to erode.
        distance: distance in mm to erode.
        volume_out: the output volume.
        opt_roi_roi_volume: assume voxels outside this roi are nonzero: volume\
            file, positive values denote voxels that have data.
        opt_subvolume_subvol: select a single subvolume to dilate: the\
            subvolume number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-erode",
        "volume": volume,
        "distance": distance,
        "volume_out": volume_out,
    }
    if opt_roi_roi_volume is not None:
        params["opt_roi_roi_volume"] = opt_roi_roi_volume
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    return params


def volume_erode_cargs(
    params: VolumeErodeParameters,
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
    cargs.append("-volume-erode")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(str(params.get("distance")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_roi_roi_volume") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_volume"))
        ])
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    return cargs


def volume_erode_outputs(
    params: VolumeErodeParameters,
    execution: Execution,
) -> VolumeErodeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeErodeOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_erode_execute(
    params: VolumeErodeParameters,
    execution: Execution,
) -> VolumeErodeOutputs:
    """
    Erode a volume file.
    
    Around each voxel with a value of zero, set surrounding voxels to zero. The
    surrounding voxels are all face neighbors and all voxels within the
    specified distance (center to center).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeErodeOutputs`).
    """
    params = execution.params(params)
    cargs = volume_erode_cargs(params, execution)
    ret = volume_erode_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_erode(
    volume: InputPathType,
    distance: float,
    volume_out: str,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeErodeOutputs:
    """
    Erode a volume file.
    
    Around each voxel with a value of zero, set surrounding voxels to zero. The
    surrounding voxels are all face neighbors and all voxels within the
    specified distance (center to center).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the volume to erode.
        distance: distance in mm to erode.
        volume_out: the output volume.
        opt_roi_roi_volume: assume voxels outside this roi are nonzero: volume\
            file, positive values denote voxels that have data.
        opt_subvolume_subvol: select a single subvolume to dilate: the\
            subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ERODE_METADATA)
    params = volume_erode_params(
        volume=volume,
        distance=distance,
        volume_out=volume_out,
        opt_roi_roi_volume=opt_roi_roi_volume,
        opt_subvolume_subvol=opt_subvolume_subvol,
    )
    return volume_erode_execute(params, execution)


__all__ = [
    "VOLUME_ERODE_METADATA",
    "VolumeErodeOutputs",
    "VolumeErodeParameters",
    "volume_erode",
    "volume_erode_params",
]
