# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_AVERAGE_METADATA = Metadata(
    id="e4592244ed0a54b4182ce9f5b2c0d504dc9489bf.boutiques",
    name="surface-average",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceAverageSurfParameters = typing.TypedDict('SurfaceAverageSurfParameters', {
    "__STYXTYPE__": typing.Literal["surf"],
    "surface": InputPathType,
    "opt_weight_weight": typing.NotRequired[float | None],
})


SurfaceAverageParameters = typing.TypedDict('SurfaceAverageParameters', {
    "__STYXTYPE__": typing.Literal["surface-average"],
    "surface_out": str,
    "opt_stddev_stddev_metric_out": typing.NotRequired[str | None],
    "opt_uncertainty_uncert_metric_out": typing.NotRequired[str | None],
    "surf": typing.NotRequired[list[SurfaceAverageSurfParameters] | None],
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
        "surface-average": surface_average_cargs,
        "surf": surface_average_surf_cargs,
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
        "surface-average": surface_average_outputs,
    }.get(t)


def surface_average_surf_params(
    surface: InputPathType,
    opt_weight_weight: float | None = None,
) -> SurfaceAverageSurfParameters:
    """
    Build parameters.
    
    Args:
        surface: a surface file to average.
        opt_weight_weight: specify a weighted average: the weight to use\
            (default 1).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surf",
        "surface": surface,
    }
    if opt_weight_weight is not None:
        params["opt_weight_weight"] = opt_weight_weight
    return params


def surface_average_surf_cargs(
    params: SurfaceAverageSurfParameters,
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
    cargs.append("-surf")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_weight_weight") is not None:
        cargs.extend([
            "-weight",
            str(params.get("opt_weight_weight"))
        ])
    return cargs


class SurfaceAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output averaged surface"""
    opt_stddev_stddev_metric_out: OutputPathType | None
    """compute 3D sample standard deviation: the output metric for 3D sample
    standard deviation"""
    opt_uncertainty_uncert_metric_out: OutputPathType | None
    """compute caret5 'uncertainty': the output metric for uncertainty"""


def surface_average_params(
    surface_out: str,
    opt_stddev_stddev_metric_out: str | None = None,
    opt_uncertainty_uncert_metric_out: str | None = None,
    surf: list[SurfaceAverageSurfParameters] | None = None,
) -> SurfaceAverageParameters:
    """
    Build parameters.
    
    Args:
        surface_out: the output averaged surface.
        opt_stddev_stddev_metric_out: compute 3D sample standard deviation: the\
            output metric for 3D sample standard deviation.
        opt_uncertainty_uncert_metric_out: compute caret5 'uncertainty': the\
            output metric for uncertainty.
        surf: specify a surface to include in the average.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-average",
        "surface_out": surface_out,
    }
    if opt_stddev_stddev_metric_out is not None:
        params["opt_stddev_stddev_metric_out"] = opt_stddev_stddev_metric_out
    if opt_uncertainty_uncert_metric_out is not None:
        params["opt_uncertainty_uncert_metric_out"] = opt_uncertainty_uncert_metric_out
    if surf is not None:
        params["surf"] = surf
    return params


def surface_average_cargs(
    params: SurfaceAverageParameters,
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
    cargs.append("-surface-average")
    cargs.append(params.get("surface_out"))
    if params.get("opt_stddev_stddev_metric_out") is not None:
        cargs.extend([
            "-stddev",
            params.get("opt_stddev_stddev_metric_out")
        ])
    if params.get("opt_uncertainty_uncert_metric_out") is not None:
        cargs.extend([
            "-uncertainty",
            params.get("opt_uncertainty_uncert_metric_out")
        ])
    if params.get("surf") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("surf")] for a in c])
    return cargs


def surface_average_outputs(
    params: SurfaceAverageParameters,
    execution: Execution,
) -> SurfaceAverageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceAverageOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
        opt_stddev_stddev_metric_out=execution.output_file(params.get("opt_stddev_stddev_metric_out")) if (params.get("opt_stddev_stddev_metric_out") is not None) else None,
        opt_uncertainty_uncert_metric_out=execution.output_file(params.get("opt_uncertainty_uncert_metric_out")) if (params.get("opt_uncertainty_uncert_metric_out") is not None) else None,
    )
    return ret


def surface_average_execute(
    params: SurfaceAverageParameters,
    execution: Execution,
) -> SurfaceAverageOutputs:
    """
    Average surface files together.
    
    The 3D sample standard deviation is computed as 'sqrt(sum(squaredlength(xyz
    - mean(xyz)))/(n - 1))'.
    
    Uncertainty is a legacy measure used in caret5, and is computed as
    'sum(length(xyz - mean(xyz)))/n'.
    
    When weights are used, the 3D sample standard deviation treats them as
    reliability weights.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceAverageOutputs`).
    """
    params = execution.params(params)
    cargs = surface_average_cargs(params, execution)
    ret = surface_average_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_average(
    surface_out: str,
    opt_stddev_stddev_metric_out: str | None = None,
    opt_uncertainty_uncert_metric_out: str | None = None,
    surf: list[SurfaceAverageSurfParameters] | None = None,
    runner: Runner | None = None,
) -> SurfaceAverageOutputs:
    """
    Average surface files together.
    
    The 3D sample standard deviation is computed as 'sqrt(sum(squaredlength(xyz
    - mean(xyz)))/(n - 1))'.
    
    Uncertainty is a legacy measure used in caret5, and is computed as
    'sum(length(xyz - mean(xyz)))/n'.
    
    When weights are used, the 3D sample standard deviation treats them as
    reliability weights.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_out: the output averaged surface.
        opt_stddev_stddev_metric_out: compute 3D sample standard deviation: the\
            output metric for 3D sample standard deviation.
        opt_uncertainty_uncert_metric_out: compute caret5 'uncertainty': the\
            output metric for uncertainty.
        surf: specify a surface to include in the average.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_AVERAGE_METADATA)
    params = surface_average_params(
        surface_out=surface_out,
        opt_stddev_stddev_metric_out=opt_stddev_stddev_metric_out,
        opt_uncertainty_uncert_metric_out=opt_uncertainty_uncert_metric_out,
        surf=surf,
    )
    return surface_average_execute(params, execution)


__all__ = [
    "SURFACE_AVERAGE_METADATA",
    "SurfaceAverageOutputs",
    "SurfaceAverageParameters",
    "SurfaceAverageSurfParameters",
    "surface_average",
    "surface_average_params",
    "surface_average_surf_params",
]
