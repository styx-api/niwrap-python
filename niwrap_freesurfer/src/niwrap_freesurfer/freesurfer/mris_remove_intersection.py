# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_REMOVE_INTERSECTION_METADATA = Metadata(
    id="35105f4c486e8643420cf4f167c32a531bdc3428.boutiques",
    name="mris_remove_intersection",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisRemoveIntersectionParameters = typing.TypedDict('MrisRemoveIntersectionParameters', {
    "__STYXTYPE__": typing.Literal["mris_remove_intersection"],
    "surface_in_file": InputPathType,
    "corrected_surface_out_file": str,
    "fill_holes": bool,
    "map_option": typing.NotRequired[InputPathType | None],
    "projdistmm": typing.NotRequired[float | None],
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
        "mris_remove_intersection": mris_remove_intersection_cargs,
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
        "mris_remove_intersection": mris_remove_intersection_outputs,
    }.get(t)


class MrisRemoveIntersectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_remove_intersection(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_corrected_surface: OutputPathType
    """Corrected surface output file."""
    out_map_file: OutputPathType | None
    """Binary map of intersections."""


def mris_remove_intersection_params(
    surface_in_file: InputPathType,
    corrected_surface_out_file: str,
    fill_holes: bool = False,
    map_option: InputPathType | None = None,
    projdistmm: float | None = None,
) -> MrisRemoveIntersectionParameters:
    """
    Build parameters.
    
    Args:
        surface_in_file: Input surface file.
        corrected_surface_out_file: Corrected output surface file.
        fill_holes: Fill any holes in the intersection mark map and include\
            them in the fix.
        map_option: Create a binary map of intersections.
        projdistmm: Projection distance in mm when using -map option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_remove_intersection",
        "surface_in_file": surface_in_file,
        "corrected_surface_out_file": corrected_surface_out_file,
        "fill_holes": fill_holes,
    }
    if map_option is not None:
        params["map_option"] = map_option
    if projdistmm is not None:
        params["projdistmm"] = projdistmm
    return params


def mris_remove_intersection_cargs(
    params: MrisRemoveIntersectionParameters,
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
    cargs.append("mris_remove_intersection")
    cargs.append(execution.input_file(params.get("surface_in_file")))
    cargs.append(params.get("corrected_surface_out_file"))
    if params.get("fill_holes"):
        cargs.append("-fill-holes")
    if params.get("map_option") is not None:
        cargs.extend([
            "-map",
            execution.input_file(params.get("map_option"))
        ])
    if params.get("projdistmm") is not None:
        cargs.append(str(params.get("projdistmm")))
    return cargs


def mris_remove_intersection_outputs(
    params: MrisRemoveIntersectionParameters,
    execution: Execution,
) -> MrisRemoveIntersectionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRemoveIntersectionOutputs(
        root=execution.output_file("."),
        out_corrected_surface=execution.output_file(params.get("corrected_surface_out_file")),
        out_map_file=execution.output_file(pathlib.Path(params.get("map_option")).name) if (params.get("map_option") is not None) else None,
    )
    return ret


def mris_remove_intersection_execute(
    params: MrisRemoveIntersectionParameters,
    execution: Execution,
) -> MrisRemoveIntersectionOutputs:
    """
    Tool to remove intersections in surface files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRemoveIntersectionOutputs`).
    """
    params = execution.params(params)
    cargs = mris_remove_intersection_cargs(params, execution)
    ret = mris_remove_intersection_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_remove_intersection(
    surface_in_file: InputPathType,
    corrected_surface_out_file: str,
    fill_holes: bool = False,
    map_option: InputPathType | None = None,
    projdistmm: float | None = None,
    runner: Runner | None = None,
) -> MrisRemoveIntersectionOutputs:
    """
    Tool to remove intersections in surface files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface_in_file: Input surface file.
        corrected_surface_out_file: Corrected output surface file.
        fill_holes: Fill any holes in the intersection mark map and include\
            them in the fix.
        map_option: Create a binary map of intersections.
        projdistmm: Projection distance in mm when using -map option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRemoveIntersectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REMOVE_INTERSECTION_METADATA)
    params = mris_remove_intersection_params(
        surface_in_file=surface_in_file,
        corrected_surface_out_file=corrected_surface_out_file,
        fill_holes=fill_holes,
        map_option=map_option,
        projdistmm=projdistmm,
    )
    return mris_remove_intersection_execute(params, execution)


__all__ = [
    "MRIS_REMOVE_INTERSECTION_METADATA",
    "MrisRemoveIntersectionOutputs",
    "MrisRemoveIntersectionParameters",
    "mris_remove_intersection",
    "mris_remove_intersection_params",
]
