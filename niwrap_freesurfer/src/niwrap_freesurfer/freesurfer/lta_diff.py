# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LTA_DIFF_METADATA = Metadata(
    id="e99c49541b6ef2ad5939381bb81d7249502ffc0c.boutiques",
    name="lta_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


LtaDiffParameters = typing.TypedDict('LtaDiffParameters', {
    "__STYX_TYPE__": typing.Literal["lta_diff"],
    "transform1": InputPathType,
    "transform2": typing.NotRequired[InputPathType | None],
    "dist_type": typing.NotRequired[int | None],
    "invert1": bool,
    "invert2": bool,
    "vox": bool,
    "normdiv": typing.NotRequired[float | None],
    "radius": typing.NotRequired[float | None],
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
        "lta_diff": lta_diff_cargs,
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


class LtaDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `lta_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def lta_diff_params(
    transform1: InputPathType,
    transform2: InputPathType | None = None,
    dist_type: int | None = None,
    invert1: bool = False,
    invert2: bool = False,
    vox: bool = False,
    normdiv: float | None = None,
    radius: float | None = None,
) -> LtaDiffParameters:
    """
    Build parameters.
    
    Args:
        transform1: First transform file.
        transform2: Second transform file.
        dist_type: Distance type: 1 (Rigid Trans. Dist.), 2 (Affine Transform\
            Distance), 3 (8-corners mean distance), 4 (Max Displacement), 5\
            (Determinant scaling), 6 (Interpolation Smoothing), 7 (Decomposition).\
            Default is 2.
        invert1: Invert first transform before computing difference matrix D.
        invert2: Invert second transform before computing difference matrix D.
        vox: Compute distance in vox coordinates, after adjusting for voxel\
            sizes. Default is RAS coordinates.
        normdiv: Divide final distance by this value for step adjustment.
        radius: Radius in mm, used for RMS distance. Default is 100 to include\
            the head.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "lta_diff",
        "transform1": transform1,
        "invert1": invert1,
        "invert2": invert2,
        "vox": vox,
    }
    if transform2 is not None:
        params["transform2"] = transform2
    if dist_type is not None:
        params["dist_type"] = dist_type
    if normdiv is not None:
        params["normdiv"] = normdiv
    if radius is not None:
        params["radius"] = radius
    return params


def lta_diff_cargs(
    params: LtaDiffParameters,
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
    cargs.append("lta_diff")
    cargs.append(execution.input_file(params.get("transform1")))
    if params.get("transform2") is not None:
        cargs.append(execution.input_file(params.get("transform2")))
    if params.get("dist_type") is not None:
        cargs.extend([
            "--dist",
            str(params.get("dist_type"))
        ])
    if params.get("invert1"):
        cargs.append("--invert1")
    if params.get("invert2"):
        cargs.append("--invert2")
    if params.get("vox"):
        cargs.append("--vox")
    if params.get("normdiv") is not None:
        cargs.extend([
            "--normdiv",
            str(params.get("normdiv"))
        ])
    if params.get("radius") is not None:
        cargs.extend([
            "--radius",
            str(params.get("radius"))
        ])
    return cargs


def lta_diff_outputs(
    params: LtaDiffParameters,
    execution: Execution,
) -> LtaDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LtaDiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def lta_diff_execute(
    params: LtaDiffParameters,
    execution: Execution,
) -> LtaDiffOutputs:
    """
    A tool to compute different distance norms for a single transform or for the
    difference between two transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LtaDiffOutputs`).
    """
    params = execution.params(params)
    cargs = lta_diff_cargs(params, execution)
    ret = lta_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def lta_diff(
    transform1: InputPathType,
    transform2: InputPathType | None = None,
    dist_type: int | None = None,
    invert1: bool = False,
    invert2: bool = False,
    vox: bool = False,
    normdiv: float | None = None,
    radius: float | None = None,
    runner: Runner | None = None,
) -> LtaDiffOutputs:
    """
    A tool to compute different distance norms for a single transform or for the
    difference between two transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        transform1: First transform file.
        transform2: Second transform file.
        dist_type: Distance type: 1 (Rigid Trans. Dist.), 2 (Affine Transform\
            Distance), 3 (8-corners mean distance), 4 (Max Displacement), 5\
            (Determinant scaling), 6 (Interpolation Smoothing), 7 (Decomposition).\
            Default is 2.
        invert1: Invert first transform before computing difference matrix D.
        invert2: Invert second transform before computing difference matrix D.
        vox: Compute distance in vox coordinates, after adjusting for voxel\
            sizes. Default is RAS coordinates.
        normdiv: Divide final distance by this value for step adjustment.
        radius: Radius in mm, used for RMS distance. Default is 100 to include\
            the head.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LtaDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LTA_DIFF_METADATA)
    params = lta_diff_params(
        transform1=transform1,
        transform2=transform2,
        dist_type=dist_type,
        invert1=invert1,
        invert2=invert2,
        vox=vox,
        normdiv=normdiv,
        radius=radius,
    )
    return lta_diff_execute(params, execution)


__all__ = [
    "LTA_DIFF_METADATA",
    "LtaDiffOutputs",
    "LtaDiffParameters",
    "lta_diff",
    "lta_diff_params",
]
