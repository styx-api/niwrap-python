# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_PAINT_METADATA = Metadata(
    id="6516a3cbf50c0b983fd6dd6fca7b67e4566c67bc.boutiques",
    name="mri_paint",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriPaintParameters = typing.TypedDict('MriPaintParameters', {
    "__STYXTYPE__": typing.Literal["mri_paint"],
    "input_volume": InputPathType,
    "input_surface": InputPathType,
    "registration_file": InputPathType,
    "output_float_file": str,
    "image_offset": typing.NotRequired[float | None],
    "paint_surf_coords": bool,
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
        "mri_paint": mri_paint_cargs,
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
        "mri_paint": mri_paint_outputs,
    }.get(t)


class MriPaintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_paint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_float: OutputPathType
    """The output .float file resulting from the painting process"""


def mri_paint_params(
    input_volume: InputPathType,
    input_surface: InputPathType,
    registration_file: InputPathType,
    output_float_file: str,
    image_offset: float | None = None,
    paint_surf_coords: bool = False,
) -> MriPaintParameters:
    """
    Build parameters.
    
    Args:
        input_volume: The input volume file.
        input_surface: The input surface file.
        registration_file: The registration file.
        output_float_file: The output .float file.
        image_offset: Set offset to use.
        paint_surf_coords: Paint using surface coordinates.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_paint",
        "input_volume": input_volume,
        "input_surface": input_surface,
        "registration_file": registration_file,
        "output_float_file": output_float_file,
        "paint_surf_coords": paint_surf_coords,
    }
    if image_offset is not None:
        params["image_offset"] = image_offset
    return params


def mri_paint_cargs(
    params: MriPaintParameters,
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
    cargs.append("mri_paint")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("registration_file")))
    cargs.append(params.get("output_float_file"))
    if params.get("image_offset") is not None:
        cargs.extend([
            "-imageoffset",
            str(params.get("image_offset"))
        ])
    if params.get("paint_surf_coords"):
        cargs.append("-S")
    return cargs


def mri_paint_outputs(
    params: MriPaintParameters,
    execution: Execution,
) -> MriPaintOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriPaintOutputs(
        root=execution.output_file("."),
        output_float=execution.output_file(params.get("output_float_file")),
    )
    return ret


def mri_paint_execute(
    params: MriPaintParameters,
    execution: Execution,
) -> MriPaintOutputs:
    """
    This program will paint average Talairach stats onto a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriPaintOutputs`).
    """
    params = execution.params(params)
    cargs = mri_paint_cargs(params, execution)
    ret = mri_paint_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_paint(
    input_volume: InputPathType,
    input_surface: InputPathType,
    registration_file: InputPathType,
    output_float_file: str,
    image_offset: float | None = None,
    paint_surf_coords: bool = False,
    runner: Runner | None = None,
) -> MriPaintOutputs:
    """
    This program will paint average Talairach stats onto a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume file.
        input_surface: The input surface file.
        registration_file: The registration file.
        output_float_file: The output .float file.
        image_offset: Set offset to use.
        paint_surf_coords: Paint using surface coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPaintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PAINT_METADATA)
    params = mri_paint_params(
        input_volume=input_volume,
        input_surface=input_surface,
        registration_file=registration_file,
        output_float_file=output_float_file,
        image_offset=image_offset,
        paint_surf_coords=paint_surf_coords,
    )
    return mri_paint_execute(params, execution)


__all__ = [
    "MRI_PAINT_METADATA",
    "MriPaintOutputs",
    "MriPaintParameters",
    "mri_paint",
    "mri_paint_params",
]
