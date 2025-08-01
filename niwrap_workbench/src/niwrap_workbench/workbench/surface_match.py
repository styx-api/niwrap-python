# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_MATCH_METADATA = Metadata(
    id="7d679c04784ea9862b5def825b069decfde8f8d4.boutiques",
    name="surface-match",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceMatchParameters = typing.TypedDict('SurfaceMatchParameters', {
    "__STYXTYPE__": typing.Literal["surface-match"],
    "match_surface_file": InputPathType,
    "input_surface_file": InputPathType,
    "output_surface_name": str,
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
        "surface-match": surface_match_cargs,
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


class SurfaceMatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_match(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_match_params(
    match_surface_file: InputPathType,
    input_surface_file: InputPathType,
    output_surface_name: str,
) -> SurfaceMatchParameters:
    """
    Build parameters.
    
    Args:
        match_surface_file: Match (Reference) Surface.
        input_surface_file: File containing surface that will be transformed.
        output_surface_name: Surface File after transformation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-match",
        "match_surface_file": match_surface_file,
        "input_surface_file": input_surface_file,
        "output_surface_name": output_surface_name,
    }
    return params


def surface_match_cargs(
    params: SurfaceMatchParameters,
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
    cargs.append("-surface-match")
    cargs.append(execution.input_file(params.get("match_surface_file")))
    cargs.append(execution.input_file(params.get("input_surface_file")))
    cargs.append(params.get("output_surface_name"))
    return cargs


def surface_match_outputs(
    params: SurfaceMatchParameters,
    execution: Execution,
) -> SurfaceMatchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceMatchOutputs(
        root=execution.output_file("."),
    )
    return ret


def surface_match_execute(
    params: SurfaceMatchParameters,
    execution: Execution,
) -> SurfaceMatchOutputs:
    """
    Surface match.
    
    The Input Surface File will be transformed so that its coordinate ranges
    (bounding box) match that of the Match Surface File.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceMatchOutputs`).
    """
    params = execution.params(params)
    cargs = surface_match_cargs(params, execution)
    ret = surface_match_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_match(
    match_surface_file: InputPathType,
    input_surface_file: InputPathType,
    output_surface_name: str,
    runner: Runner | None = None,
) -> SurfaceMatchOutputs:
    """
    Surface match.
    
    The Input Surface File will be transformed so that its coordinate ranges
    (bounding box) match that of the Match Surface File.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        match_surface_file: Match (Reference) Surface.
        input_surface_file: File containing surface that will be transformed.
        output_surface_name: Surface File after transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceMatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_MATCH_METADATA)
    params = surface_match_params(
        match_surface_file=match_surface_file,
        input_surface_file=input_surface_file,
        output_surface_name=output_surface_name,
    )
    return surface_match_execute(params, execution)


__all__ = [
    "SURFACE_MATCH_METADATA",
    "SurfaceMatchOutputs",
    "SurfaceMatchParameters",
    "surface_match",
    "surface_match_params",
]
