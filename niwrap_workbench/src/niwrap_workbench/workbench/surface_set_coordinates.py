# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_SET_COORDINATES_METADATA = Metadata(
    id="c6fdf4a985aef6d3f7d1b691e3c199ed0f7a2777.boutiques",
    name="surface-set-coordinates",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceSetCoordinatesParameters = typing.TypedDict('SurfaceSetCoordinatesParameters', {
    "__STYX_TYPE__": typing.Literal["surface-set-coordinates"],
    "surface_in": InputPathType,
    "coord_metric": InputPathType,
    "surface_out": str,
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
        "surface-set-coordinates": surface_set_coordinates_cargs,
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
        "surface-set-coordinates": surface_set_coordinates_outputs,
    }.get(t)


class SurfaceSetCoordinatesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_set_coordinates(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the new surface"""


def surface_set_coordinates_params(
    surface_in: InputPathType,
    coord_metric: InputPathType,
    surface_out: str,
) -> SurfaceSetCoordinatesParameters:
    """
    Build parameters.
    
    Args:
        surface_in: the surface to use for the topology.
        coord_metric: the new coordinates, as a 3-column metric file.
        surface_out: the new surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-set-coordinates",
        "surface_in": surface_in,
        "coord_metric": coord_metric,
        "surface_out": surface_out,
    }
    return params


def surface_set_coordinates_cargs(
    params: SurfaceSetCoordinatesParameters,
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
    cargs.append("-surface-set-coordinates")
    cargs.append(execution.input_file(params.get("surface_in")))
    cargs.append(execution.input_file(params.get("coord_metric")))
    cargs.append(params.get("surface_out"))
    return cargs


def surface_set_coordinates_outputs(
    params: SurfaceSetCoordinatesParameters,
    execution: Execution,
) -> SurfaceSetCoordinatesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceSetCoordinatesOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
    )
    return ret


def surface_set_coordinates_execute(
    params: SurfaceSetCoordinatesParameters,
    execution: Execution,
) -> SurfaceSetCoordinatesOutputs:
    """
    Modify coordinates of a surface.
    
    Takes the topology from an existing surface file, and uses values from a
    metric file as coordinates to construct a new surface file.
    
    See -surface-coordinates-to-metric for how to get surface coordinates as a
    metric file, such that you can then modify them via metric commands, etc.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceSetCoordinatesOutputs`).
    """
    params = execution.params(params)
    cargs = surface_set_coordinates_cargs(params, execution)
    ret = surface_set_coordinates_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_set_coordinates(
    surface_in: InputPathType,
    coord_metric: InputPathType,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceSetCoordinatesOutputs:
    """
    Modify coordinates of a surface.
    
    Takes the topology from an existing surface file, and uses values from a
    metric file as coordinates to construct a new surface file.
    
    See -surface-coordinates-to-metric for how to get surface coordinates as a
    metric file, such that you can then modify them via metric commands, etc.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_in: the surface to use for the topology.
        coord_metric: the new coordinates, as a 3-column metric file.
        surface_out: the new surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceSetCoordinatesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SET_COORDINATES_METADATA)
    params = surface_set_coordinates_params(
        surface_in=surface_in,
        coord_metric=coord_metric,
        surface_out=surface_out,
    )
    return surface_set_coordinates_execute(params, execution)


__all__ = [
    "SURFACE_SET_COORDINATES_METADATA",
    "SurfaceSetCoordinatesOutputs",
    "SurfaceSetCoordinatesParameters",
    "surface_set_coordinates",
    "surface_set_coordinates_params",
]
