# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CURVATURE2IMAGE_METADATA = Metadata(
    id="39d168b98aa409f7185978cb8e4d30fc3f31b37b.boutiques",
    name="mris_curvature2image",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisCurvature2imageParameters = typing.TypedDict('MrisCurvature2imageParameters', {
    "__STYX_TYPE__": typing.Literal["mris_curvature2image"],
    "surface": InputPathType,
    "mask": InputPathType,
    "output_overlay": str,
    "output_distance": str,
    "overlay": InputPathType,
    "label": InputPathType,
    "invert_flag": bool,
    "radius": float,
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
        "mris_curvature2image": mris_curvature2image_cargs,
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
        "mris_curvature2image": mris_curvature2image_outputs,
    }.get(t)


class MrisCurvature2imageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_curvature2image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlay_img: OutputPathType
    """Generated overlay image file."""
    output_distance_img: OutputPathType
    """Generated distance image file."""


def mris_curvature2image_params(
    surface: InputPathType,
    mask: InputPathType,
    output_overlay: str,
    output_distance: str,
    overlay: InputPathType,
    label: InputPathType,
    radius: float,
    invert_flag: bool = False,
) -> MrisCurvature2imageParameters:
    """
    Build parameters.
    
    Args:
        surface: Input surface file.
        mask: Input mask file.
        output_overlay: Output overlay image file.
        output_distance: Output distance image file.
        overlay: Overlay file.
        label: Label file.
        radius: Radius value for processing.
        invert_flag: Flag to invert the curvature values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_curvature2image",
        "surface": surface,
        "mask": mask,
        "output_overlay": output_overlay,
        "output_distance": output_distance,
        "overlay": overlay,
        "label": label,
        "invert_flag": invert_flag,
        "radius": radius,
    }
    return params


def mris_curvature2image_cargs(
    params: MrisCurvature2imageParameters,
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
    cargs.append("mris_curvature2image")
    cargs.extend([
        "-s",
        execution.input_file(params.get("surface"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask"))
    ])
    cargs.extend([
        "-o",
        params.get("output_overlay")
    ])
    cargs.extend([
        "-d",
        params.get("output_distance")
    ])
    cargs.extend([
        "-c",
        execution.input_file(params.get("overlay"))
    ])
    cargs.extend([
        "-l",
        execution.input_file(params.get("label"))
    ])
    if params.get("invert_flag"):
        cargs.append("-inv")
    cargs.extend([
        "-r",
        str(params.get("radius"))
    ])
    return cargs


def mris_curvature2image_outputs(
    params: MrisCurvature2imageParameters,
    execution: Execution,
) -> MrisCurvature2imageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCurvature2imageOutputs(
        root=execution.output_file("."),
        output_overlay_img=execution.output_file(params.get("output_overlay")),
        output_distance_img=execution.output_file(params.get("output_distance")),
    )
    return ret


def mris_curvature2image_execute(
    params: MrisCurvature2imageParameters,
    execution: Execution,
) -> MrisCurvature2imageOutputs:
    """
    Tool to convert surface curvature data to an image using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCurvature2imageOutputs`).
    """
    params = execution.params(params)
    cargs = mris_curvature2image_cargs(params, execution)
    ret = mris_curvature2image_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_curvature2image(
    surface: InputPathType,
    mask: InputPathType,
    output_overlay: str,
    output_distance: str,
    overlay: InputPathType,
    label: InputPathType,
    radius: float,
    invert_flag: bool = False,
    runner: Runner | None = None,
) -> MrisCurvature2imageOutputs:
    """
    Tool to convert surface curvature data to an image using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface file.
        mask: Input mask file.
        output_overlay: Output overlay image file.
        output_distance: Output distance image file.
        overlay: Overlay file.
        label: Label file.
        radius: Radius value for processing.
        invert_flag: Flag to invert the curvature values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCurvature2imageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CURVATURE2IMAGE_METADATA)
    params = mris_curvature2image_params(
        surface=surface,
        mask=mask,
        output_overlay=output_overlay,
        output_distance=output_distance,
        overlay=overlay,
        label=label,
        invert_flag=invert_flag,
        radius=radius,
    )
    return mris_curvature2image_execute(params, execution)


__all__ = [
    "MRIS_CURVATURE2IMAGE_METADATA",
    "MrisCurvature2imageOutputs",
    "MrisCurvature2imageParameters",
    "mris_curvature2image",
    "mris_curvature2image_params",
]
