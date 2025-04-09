# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_DISTORTION_METADATA = Metadata(
    id="48fa054376bf4c18372dba53ab95fa9cc3a1605c.boutiques",
    name="surface-distortion",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceDistortionSmoothParameters = typing.TypedDict('SurfaceDistortionSmoothParameters', {
    "__STYX_TYPE__": typing.Literal["smooth"],
    "sigma": float,
    "opt_fwhm": bool,
})


SurfaceDistortionLocalAffineMethodParameters = typing.TypedDict('SurfaceDistortionLocalAffineMethodParameters', {
    "__STYX_TYPE__": typing.Literal["local_affine_method"],
    "opt_log2": bool,
})


SurfaceDistortionParameters = typing.TypedDict('SurfaceDistortionParameters', {
    "__STYX_TYPE__": typing.Literal["surface-distortion"],
    "surface_reference": InputPathType,
    "surface_distorted": InputPathType,
    "metric_out": str,
    "smooth": typing.NotRequired[SurfaceDistortionSmoothParameters | None],
    "opt_caret5_method": bool,
    "opt_edge_method": bool,
    "local_affine_method": typing.NotRequired[SurfaceDistortionLocalAffineMethodParameters | None],
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
        "surface-distortion": surface_distortion_cargs,
        "smooth": surface_distortion_smooth_cargs,
        "local_affine_method": surface_distortion_local_affine_method_cargs,
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
        "surface-distortion": surface_distortion_outputs,
    }.get(t)


def surface_distortion_smooth_params(
    sigma: float,
    opt_fwhm: bool = False,
) -> SurfaceDistortionSmoothParameters:
    """
    Build parameters.
    
    Args:
        sigma: the size of the smoothing kernel in mm, as sigma by default.
        opt_fwhm: kernel size is FWHM, not sigma.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "smooth",
        "sigma": sigma,
        "opt_fwhm": opt_fwhm,
    }
    return params


def surface_distortion_smooth_cargs(
    params: SurfaceDistortionSmoothParameters,
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
    cargs.append("-smooth")
    cargs.append(str(params.get("sigma")))
    if params.get("opt_fwhm"):
        cargs.append("-fwhm")
    return cargs


def surface_distortion_local_affine_method_params(
    opt_log2: bool = False,
) -> SurfaceDistortionLocalAffineMethodParameters:
    """
    Build parameters.
    
    Args:
        opt_log2: apply base-2 log transform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "local_affine_method",
        "opt_log2": opt_log2,
    }
    return params


def surface_distortion_local_affine_method_cargs(
    params: SurfaceDistortionLocalAffineMethodParameters,
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
    cargs.append("-local-affine-method")
    if params.get("opt_log2"):
        cargs.append("-log2")
    return cargs


class SurfaceDistortionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_distortion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output distortion metric"""


def surface_distortion_params(
    surface_reference: InputPathType,
    surface_distorted: InputPathType,
    metric_out: str,
    smooth: SurfaceDistortionSmoothParameters | None = None,
    opt_caret5_method: bool = False,
    opt_edge_method: bool = False,
    local_affine_method: SurfaceDistortionLocalAffineMethodParameters | None = None,
) -> SurfaceDistortionParameters:
    """
    Build parameters.
    
    Args:
        surface_reference: the reference surface.
        surface_distorted: the distorted surface.
        metric_out: the output distortion metric.
        smooth: smooth the area data.
        opt_caret5_method: use the surface distortion method from caret5.
        opt_edge_method: calculate distortion of edge lengths rather than areas.
        local_affine_method: calculate distortion by the local affines between\
            triangles.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-distortion",
        "surface_reference": surface_reference,
        "surface_distorted": surface_distorted,
        "metric_out": metric_out,
        "opt_caret5_method": opt_caret5_method,
        "opt_edge_method": opt_edge_method,
    }
    if smooth is not None:
        params["smooth"] = smooth
    if local_affine_method is not None:
        params["local_affine_method"] = local_affine_method
    return params


def surface_distortion_cargs(
    params: SurfaceDistortionParameters,
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
    cargs.append("-surface-distortion")
    cargs.append(execution.input_file(params.get("surface_reference")))
    cargs.append(execution.input_file(params.get("surface_distorted")))
    cargs.append(params.get("metric_out"))
    if params.get("smooth") is not None:
        cargs.extend(dyn_cargs(params.get("smooth")["__STYXTYPE__"])(params.get("smooth"), execution))
    if params.get("opt_caret5_method"):
        cargs.append("-caret5-method")
    if params.get("opt_edge_method"):
        cargs.append("-edge-method")
    if params.get("local_affine_method") is not None:
        cargs.extend(dyn_cargs(params.get("local_affine_method")["__STYXTYPE__"])(params.get("local_affine_method"), execution))
    return cargs


def surface_distortion_outputs(
    params: SurfaceDistortionParameters,
    execution: Execution,
) -> SurfaceDistortionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceDistortionOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def surface_distortion_execute(
    params: SurfaceDistortionParameters,
    execution: Execution,
) -> SurfaceDistortionOutputs:
    """
    Measure distortion between surfaces.
    
    This command, when not using -caret5-method, -edge-method, or
    -local-affine-method, is equivalent to using -surface-vertex-areas on each
    surface, smoothing both output metrics with the GEO_GAUSS_EQUAL method on
    the surface they came from if -smooth is specified, and then using the
    formula 'ln(distorted/reference)/ln(2)' on the smoothed results.
    
    When using -caret5-method, it uses the surface distortion method from
    caret5, which takes the base 2 log of the ratio of tile areas, then averages
    those results at each vertex, and then smooths the result on the reference
    surface.
    
    When using -edge-method, the -smooth option is ignored, and the output at
    each vertex is the average of 'abs(ln(refEdge/distortEdge)/ln(2))' over all
    edges connected to the vertex.
    
    When using -local-affine-method, the -smooth option is ignored. The output
    is two columns, the first is the area distortion ratio, and the second is
    anisotropic strain. These are calculated by an affine transform between
    matching triangles, and then averaged across the triangles of a vertex.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceDistortionOutputs`).
    """
    params = execution.params(params)
    cargs = surface_distortion_cargs(params, execution)
    ret = surface_distortion_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_distortion(
    surface_reference: InputPathType,
    surface_distorted: InputPathType,
    metric_out: str,
    smooth: SurfaceDistortionSmoothParameters | None = None,
    opt_caret5_method: bool = False,
    opt_edge_method: bool = False,
    local_affine_method: SurfaceDistortionLocalAffineMethodParameters | None = None,
    runner: Runner | None = None,
) -> SurfaceDistortionOutputs:
    """
    Measure distortion between surfaces.
    
    This command, when not using -caret5-method, -edge-method, or
    -local-affine-method, is equivalent to using -surface-vertex-areas on each
    surface, smoothing both output metrics with the GEO_GAUSS_EQUAL method on
    the surface they came from if -smooth is specified, and then using the
    formula 'ln(distorted/reference)/ln(2)' on the smoothed results.
    
    When using -caret5-method, it uses the surface distortion method from
    caret5, which takes the base 2 log of the ratio of tile areas, then averages
    those results at each vertex, and then smooths the result on the reference
    surface.
    
    When using -edge-method, the -smooth option is ignored, and the output at
    each vertex is the average of 'abs(ln(refEdge/distortEdge)/ln(2))' over all
    edges connected to the vertex.
    
    When using -local-affine-method, the -smooth option is ignored. The output
    is two columns, the first is the area distortion ratio, and the second is
    anisotropic strain. These are calculated by an affine transform between
    matching triangles, and then averaged across the triangles of a vertex.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_reference: the reference surface.
        surface_distorted: the distorted surface.
        metric_out: the output distortion metric.
        smooth: smooth the area data.
        opt_caret5_method: use the surface distortion method from caret5.
        opt_edge_method: calculate distortion of edge lengths rather than areas.
        local_affine_method: calculate distortion by the local affines between\
            triangles.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceDistortionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_DISTORTION_METADATA)
    params = surface_distortion_params(
        surface_reference=surface_reference,
        surface_distorted=surface_distorted,
        metric_out=metric_out,
        smooth=smooth,
        opt_caret5_method=opt_caret5_method,
        opt_edge_method=opt_edge_method,
        local_affine_method=local_affine_method,
    )
    return surface_distortion_execute(params, execution)


__all__ = [
    "SURFACE_DISTORTION_METADATA",
    "SurfaceDistortionLocalAffineMethodParameters",
    "SurfaceDistortionOutputs",
    "SurfaceDistortionParameters",
    "SurfaceDistortionSmoothParameters",
    "surface_distortion",
    "surface_distortion_local_affine_method_params",
    "surface_distortion_params",
    "surface_distortion_smooth_params",
]
