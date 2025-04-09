# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_GENERATE_INFLATED_METADATA = Metadata(
    id="9c016947a1a72f762f5cf06f27ae9587bfe30607.boutiques",
    name="surface-generate-inflated",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceGenerateInflatedParameters = typing.TypedDict('SurfaceGenerateInflatedParameters', {
    "__STYX_TYPE__": typing.Literal["surface-generate-inflated"],
    "anatomical_surface_in": InputPathType,
    "inflated_surface_out": str,
    "very_inflated_surface_out": str,
    "opt_iterations_scale_iterations_scale_value": typing.NotRequired[float | None],
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
        "surface-generate-inflated": surface_generate_inflated_cargs,
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
        "surface-generate-inflated": surface_generate_inflated_outputs,
    }.get(t)


class SurfaceGenerateInflatedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_generate_inflated(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inflated_surface_out: OutputPathType
    """the output inflated surface"""
    very_inflated_surface_out: OutputPathType
    """the output very inflated surface"""


def surface_generate_inflated_params(
    anatomical_surface_in: InputPathType,
    inflated_surface_out: str,
    very_inflated_surface_out: str,
    opt_iterations_scale_iterations_scale_value: float | None = None,
) -> SurfaceGenerateInflatedParameters:
    """
    Build parameters.
    
    Args:
        anatomical_surface_in: the anatomical surface.
        inflated_surface_out: the output inflated surface.
        very_inflated_surface_out: the output very inflated surface.
        opt_iterations_scale_iterations_scale_value: optional iterations\
            scaling: iterations-scale value.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-generate-inflated",
        "anatomical_surface_in": anatomical_surface_in,
        "inflated_surface_out": inflated_surface_out,
        "very_inflated_surface_out": very_inflated_surface_out,
    }
    if opt_iterations_scale_iterations_scale_value is not None:
        params["opt_iterations_scale_iterations_scale_value"] = opt_iterations_scale_iterations_scale_value
    return params


def surface_generate_inflated_cargs(
    params: SurfaceGenerateInflatedParameters,
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
    cargs.append("-surface-generate-inflated")
    cargs.append(execution.input_file(params.get("anatomical_surface_in")))
    cargs.append(params.get("inflated_surface_out"))
    cargs.append(params.get("very_inflated_surface_out"))
    if params.get("opt_iterations_scale_iterations_scale_value") is not None:
        cargs.extend([
            "-iterations-scale",
            str(params.get("opt_iterations_scale_iterations_scale_value"))
        ])
    return cargs


def surface_generate_inflated_outputs(
    params: SurfaceGenerateInflatedParameters,
    execution: Execution,
) -> SurfaceGenerateInflatedOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceGenerateInflatedOutputs(
        root=execution.output_file("."),
        inflated_surface_out=execution.output_file(params.get("inflated_surface_out")),
        very_inflated_surface_out=execution.output_file(params.get("very_inflated_surface_out")),
    )
    return ret


def surface_generate_inflated_execute(
    params: SurfaceGenerateInflatedParameters,
    execution: Execution,
) -> SurfaceGenerateInflatedOutputs:
    """
    Surface generate inflated.
    
    Generate inflated and very inflated surfaces. The output surfaces are
    'matched' (have same XYZ range) to the anatomical surface. In most cases, an
    iterations-scale of 1.0 (default) is sufficient. However, if the surface
    contains a large number of vertices (150,000), try an iterations-scale of
    2.5.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceGenerateInflatedOutputs`).
    """
    params = execution.params(params)
    cargs = surface_generate_inflated_cargs(params, execution)
    ret = surface_generate_inflated_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_generate_inflated(
    anatomical_surface_in: InputPathType,
    inflated_surface_out: str,
    very_inflated_surface_out: str,
    opt_iterations_scale_iterations_scale_value: float | None = None,
    runner: Runner | None = None,
) -> SurfaceGenerateInflatedOutputs:
    """
    Surface generate inflated.
    
    Generate inflated and very inflated surfaces. The output surfaces are
    'matched' (have same XYZ range) to the anatomical surface. In most cases, an
    iterations-scale of 1.0 (default) is sufficient. However, if the surface
    contains a large number of vertices (150,000), try an iterations-scale of
    2.5.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        anatomical_surface_in: the anatomical surface.
        inflated_surface_out: the output inflated surface.
        very_inflated_surface_out: the output very inflated surface.
        opt_iterations_scale_iterations_scale_value: optional iterations\
            scaling: iterations-scale value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceGenerateInflatedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_GENERATE_INFLATED_METADATA)
    params = surface_generate_inflated_params(
        anatomical_surface_in=anatomical_surface_in,
        inflated_surface_out=inflated_surface_out,
        very_inflated_surface_out=very_inflated_surface_out,
        opt_iterations_scale_iterations_scale_value=opt_iterations_scale_iterations_scale_value,
    )
    return surface_generate_inflated_execute(params, execution)


__all__ = [
    "SURFACE_GENERATE_INFLATED_METADATA",
    "SurfaceGenerateInflatedOutputs",
    "SurfaceGenerateInflatedParameters",
    "surface_generate_inflated",
    "surface_generate_inflated_params",
]
