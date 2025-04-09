# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ICO_SUPERSAMPLE_METADATA = Metadata(
    id="a325b40c5e9a6433abb23e27b0d456238f472064.boutiques",
    name="ico_supersample",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


IcoSupersampleParameters = typing.TypedDict('IcoSupersampleParameters', {
    "__STYX_TYPE__": typing.Literal["ico_supersample"],
    "refine": bool,
    "radius": typing.NotRequired[float | None],
    "projection_point": typing.NotRequired[list[float] | None],
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
        "ico_supersample": ico_supersample_cargs,
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
        "ico_supersample": ico_supersample_outputs,
    }.get(t)


class IcoSupersampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ico_supersample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output file containing the refined icosahedron mesh."""


def ico_supersample_params(
    refine: bool = False,
    radius: float | None = None,
    projection_point: list[float] | None = None,
) -> IcoSupersampleParameters:
    """
    Build parameters.
    
    Args:
        refine: Refine the icosahedron mesh.
        radius: Radius of the sphere onto which the icosahedron is projected.
        projection_point: Projection point for the icosahedron refinement.\
            Enter three floating point values separated by spaces.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ico_supersample",
        "refine": refine,
    }
    if radius is not None:
        params["radius"] = radius
    if projection_point is not None:
        params["projection_point"] = projection_point
    return params


def ico_supersample_cargs(
    params: IcoSupersampleParameters,
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
    cargs.append("ico_supersample")
    if params.get("refine"):
        cargs.append("-y")
    if params.get("radius") is not None:
        cargs.append(str(params.get("radius")))
    if params.get("projection_point") is not None:
        cargs.extend(map(str, params.get("projection_point")))
    return cargs


def ico_supersample_outputs(
    params: IcoSupersampleParameters,
    execution: Execution,
) -> IcoSupersampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IcoSupersampleOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("refined_icosahedron.obj"),
    )
    return ret


def ico_supersample_execute(
    params: IcoSupersampleParameters,
    execution: Execution,
) -> IcoSupersampleOutputs:
    """
    A tool for refining icosahedron meshes with user-specified parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IcoSupersampleOutputs`).
    """
    params = execution.params(params)
    cargs = ico_supersample_cargs(params, execution)
    ret = ico_supersample_outputs(params, execution)
    execution.run(cargs)
    return ret


def ico_supersample(
    refine: bool = False,
    radius: float | None = None,
    projection_point: list[float] | None = None,
    runner: Runner | None = None,
) -> IcoSupersampleOutputs:
    """
    A tool for refining icosahedron meshes with user-specified parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        refine: Refine the icosahedron mesh.
        radius: Radius of the sphere onto which the icosahedron is projected.
        projection_point: Projection point for the icosahedron refinement.\
            Enter three floating point values separated by spaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IcoSupersampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ICO_SUPERSAMPLE_METADATA)
    params = ico_supersample_params(
        refine=refine,
        radius=radius,
        projection_point=projection_point,
    )
    return ico_supersample_execute(params, execution)


__all__ = [
    "ICO_SUPERSAMPLE_METADATA",
    "IcoSupersampleOutputs",
    "IcoSupersampleParameters",
    "ico_supersample",
    "ico_supersample_params",
]
