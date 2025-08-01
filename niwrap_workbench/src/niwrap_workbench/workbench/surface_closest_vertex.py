# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_CLOSEST_VERTEX_METADATA = Metadata(
    id="b247f4f20d018925392cfcdef99f6eaa3f24d896.boutiques",
    name="surface-closest-vertex",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceClosestVertexParameters = typing.TypedDict('SurfaceClosestVertexParameters', {
    "__STYXTYPE__": typing.Literal["surface-closest-vertex"],
    "surface": InputPathType,
    "coord_list_file": str,
    "vertex_list_out": str,
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
        "surface-closest-vertex": surface_closest_vertex_cargs,
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


class SurfaceClosestVertexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_closest_vertex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_closest_vertex_params(
    surface: InputPathType,
    coord_list_file: str,
    vertex_list_out: str,
) -> SurfaceClosestVertexParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to use.
        coord_list_file: text file with coordinates.
        vertex_list_out: output - the output text file with vertex numbers.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-closest-vertex",
        "surface": surface,
        "coord_list_file": coord_list_file,
        "vertex_list_out": vertex_list_out,
    }
    return params


def surface_closest_vertex_cargs(
    params: SurfaceClosestVertexParameters,
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
    cargs.append("-surface-closest-vertex")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("coord_list_file"))
    cargs.append(params.get("vertex_list_out"))
    return cargs


def surface_closest_vertex_outputs(
    params: SurfaceClosestVertexParameters,
    execution: Execution,
) -> SurfaceClosestVertexOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceClosestVertexOutputs(
        root=execution.output_file("."),
    )
    return ret


def surface_closest_vertex_execute(
    params: SurfaceClosestVertexParameters,
    execution: Execution,
) -> SurfaceClosestVertexOutputs:
    """
    Find closest surface vertex to coordinates.
    
    For each coordinate XYZ triple, find the closest vertex in the surface, and
    output its vertex number into a text file. The input file should only use
    whitespace to separate coordinates (spaces, newlines, tabs), for instance:
    
    20 30 25
    30 -20 10.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceClosestVertexOutputs`).
    """
    params = execution.params(params)
    cargs = surface_closest_vertex_cargs(params, execution)
    ret = surface_closest_vertex_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_closest_vertex(
    surface: InputPathType,
    coord_list_file: str,
    vertex_list_out: str,
    runner: Runner | None = None,
) -> SurfaceClosestVertexOutputs:
    """
    Find closest surface vertex to coordinates.
    
    For each coordinate XYZ triple, find the closest vertex in the surface, and
    output its vertex number into a text file. The input file should only use
    whitespace to separate coordinates (spaces, newlines, tabs), for instance:
    
    20 30 25
    30 -20 10.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use.
        coord_list_file: text file with coordinates.
        vertex_list_out: output - the output text file with vertex numbers.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceClosestVertexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CLOSEST_VERTEX_METADATA)
    params = surface_closest_vertex_params(
        surface=surface,
        coord_list_file=coord_list_file,
        vertex_list_out=vertex_list_out,
    )
    return surface_closest_vertex_execute(params, execution)


__all__ = [
    "SURFACE_CLOSEST_VERTEX_METADATA",
    "SurfaceClosestVertexOutputs",
    "SurfaceClosestVertexParameters",
    "surface_closest_vertex",
    "surface_closest_vertex_params",
]
