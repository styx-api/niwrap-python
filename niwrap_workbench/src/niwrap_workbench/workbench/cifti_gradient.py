# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_GRADIENT_METADATA = Metadata(
    id="f39faf9e44389b76874a4aaef665f54cb7870989.boutiques",
    name="cifti-gradient",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiGradientLeftSurfaceParameters = typing.TypedDict('CiftiGradientLeftSurfaceParameters', {
    "__STYXTYPE__": typing.Literal["left_surface"],
    "surface": InputPathType,
    "opt_left_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})


CiftiGradientRightSurfaceParameters = typing.TypedDict('CiftiGradientRightSurfaceParameters', {
    "__STYXTYPE__": typing.Literal["right_surface"],
    "surface": InputPathType,
    "opt_right_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})


CiftiGradientCerebellumSurfaceParameters = typing.TypedDict('CiftiGradientCerebellumSurfaceParameters', {
    "__STYXTYPE__": typing.Literal["cerebellum_surface"],
    "surface": InputPathType,
    "opt_cerebellum_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})


CiftiGradientParameters = typing.TypedDict('CiftiGradientParameters', {
    "__STYXTYPE__": typing.Literal["cifti-gradient"],
    "cifti": InputPathType,
    "direction": str,
    "cifti_out": str,
    "left_surface": typing.NotRequired[CiftiGradientLeftSurfaceParameters | None],
    "right_surface": typing.NotRequired[CiftiGradientRightSurfaceParameters | None],
    "cerebellum_surface": typing.NotRequired[CiftiGradientCerebellumSurfaceParameters | None],
    "opt_surface_presmooth_surface_kernel": typing.NotRequired[float | None],
    "opt_volume_presmooth_volume_kernel": typing.NotRequired[float | None],
    "opt_presmooth_fwhm": bool,
    "opt_average_output": bool,
    "opt_vectors_vectors_out": typing.NotRequired[str | None],
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
        "cifti-gradient": cifti_gradient_cargs,
        "left_surface": cifti_gradient_left_surface_cargs,
        "right_surface": cifti_gradient_right_surface_cargs,
        "cerebellum_surface": cifti_gradient_cerebellum_surface_cargs,
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
        "cifti-gradient": cifti_gradient_outputs,
    }.get(t)


def cifti_gradient_left_surface_params(
    surface: InputPathType,
    opt_left_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiGradientLeftSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the left surface file.
        opt_left_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the left surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_surface",
        "surface": surface,
    }
    if opt_left_corrected_areas_area_metric is not None:
        params["opt_left_corrected_areas_area_metric"] = opt_left_corrected_areas_area_metric
    return params


def cifti_gradient_left_surface_cargs(
    params: CiftiGradientLeftSurfaceParameters,
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
    cargs.append("-left-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_left_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-left-corrected-areas",
            execution.input_file(params.get("opt_left_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_gradient_right_surface_params(
    surface: InputPathType,
    opt_right_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiGradientRightSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the right surface file.
        opt_right_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the right surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_surface",
        "surface": surface,
    }
    if opt_right_corrected_areas_area_metric is not None:
        params["opt_right_corrected_areas_area_metric"] = opt_right_corrected_areas_area_metric
    return params


def cifti_gradient_right_surface_cargs(
    params: CiftiGradientRightSurfaceParameters,
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
    cargs.append("-right-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_right_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-right-corrected-areas",
            execution.input_file(params.get("opt_right_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_gradient_cerebellum_surface_params(
    surface: InputPathType,
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiGradientCerebellumSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the cerebellum surface file.
        opt_cerebellum_corrected_areas_area_metric: vertex areas to use instead\
            of computing them from the cerebellum surface: the corrected vertex\
            areas, as a metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_surface",
        "surface": surface,
    }
    if opt_cerebellum_corrected_areas_area_metric is not None:
        params["opt_cerebellum_corrected_areas_area_metric"] = opt_cerebellum_corrected_areas_area_metric
    return params


def cifti_gradient_cerebellum_surface_cargs(
    params: CiftiGradientCerebellumSurfaceParameters,
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
    cargs.append("-cerebellum-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_cerebellum_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-cerebellum-corrected-areas",
            execution.input_file(params.get("opt_cerebellum_corrected_areas_area_metric"))
        ])
    return cargs


class CiftiGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""
    opt_vectors_vectors_out: OutputPathType | None
    """output gradient vectors: the vectors, as a dscalar file"""


def cifti_gradient_params(
    cifti: InputPathType,
    direction: str,
    cifti_out: str,
    left_surface: CiftiGradientLeftSurfaceParameters | None = None,
    right_surface: CiftiGradientRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiGradientCerebellumSurfaceParameters | None = None,
    opt_surface_presmooth_surface_kernel: float | None = None,
    opt_volume_presmooth_volume_kernel: float | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_average_output: bool = False,
    opt_vectors_vectors_out: str | None = None,
) -> CiftiGradientParameters:
    """
    Build parameters.
    
    Args:
        cifti: the input cifti.
        direction: which dimension to take the gradient along, ROW or COLUMN.
        cifti_out: the output cifti.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_surface_presmooth_surface_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian surface smoothing\
            kernel in mm, as sigma by default.
        opt_volume_presmooth_volume_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian volume smoothing\
            kernel in mm, as sigma by default.
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma.
        opt_average_output: output the average of the gradient magnitude maps\
            instead of each gradient map separately.
        opt_vectors_vectors_out: output gradient vectors: the vectors, as a\
            dscalar file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-gradient",
        "cifti": cifti,
        "direction": direction,
        "cifti_out": cifti_out,
        "opt_presmooth_fwhm": opt_presmooth_fwhm,
        "opt_average_output": opt_average_output,
    }
    if left_surface is not None:
        params["left_surface"] = left_surface
    if right_surface is not None:
        params["right_surface"] = right_surface
    if cerebellum_surface is not None:
        params["cerebellum_surface"] = cerebellum_surface
    if opt_surface_presmooth_surface_kernel is not None:
        params["opt_surface_presmooth_surface_kernel"] = opt_surface_presmooth_surface_kernel
    if opt_volume_presmooth_volume_kernel is not None:
        params["opt_volume_presmooth_volume_kernel"] = opt_volume_presmooth_volume_kernel
    if opt_vectors_vectors_out is not None:
        params["opt_vectors_vectors_out"] = opt_vectors_vectors_out
    return params


def cifti_gradient_cargs(
    params: CiftiGradientParameters,
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
    cargs.append("-cifti-gradient")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(params.get("direction"))
    cargs.append(params.get("cifti_out"))
    if params.get("left_surface") is not None:
        cargs.extend(dyn_cargs(params.get("left_surface")["__STYXTYPE__"])(params.get("left_surface"), execution))
    if params.get("right_surface") is not None:
        cargs.extend(dyn_cargs(params.get("right_surface")["__STYXTYPE__"])(params.get("right_surface"), execution))
    if params.get("cerebellum_surface") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_surface")["__STYXTYPE__"])(params.get("cerebellum_surface"), execution))
    if params.get("opt_surface_presmooth_surface_kernel") is not None:
        cargs.extend([
            "-surface-presmooth",
            str(params.get("opt_surface_presmooth_surface_kernel"))
        ])
    if params.get("opt_volume_presmooth_volume_kernel") is not None:
        cargs.extend([
            "-volume-presmooth",
            str(params.get("opt_volume_presmooth_volume_kernel"))
        ])
    if params.get("opt_presmooth_fwhm"):
        cargs.append("-presmooth-fwhm")
    if params.get("opt_average_output"):
        cargs.append("-average-output")
    if params.get("opt_vectors_vectors_out") is not None:
        cargs.extend([
            "-vectors",
            params.get("opt_vectors_vectors_out")
        ])
    return cargs


def cifti_gradient_outputs(
    params: CiftiGradientParameters,
    execution: Execution,
) -> CiftiGradientOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiGradientOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
        opt_vectors_vectors_out=execution.output_file(params.get("opt_vectors_vectors_out")) if (params.get("opt_vectors_vectors_out") is not None) else None,
    )
    return ret


def cifti_gradient_execute(
    params: CiftiGradientParameters,
    execution: Execution,
) -> CiftiGradientOutputs:
    """
    Take gradient of a cifti file.
    
    Performs gradient calculation on each component of the cifti file, and
    optionally averages the resulting gradients. The -vectors and
    -average-output options may not be used together. You must specify a surface
    for each surface structure in the cifti file. The COLUMN direction should be
    faster, and is the direction that works on dtseries. For dconn, you probably
    want ROW, unless you are using -average-output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiGradientOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_gradient_cargs(params, execution)
    ret = cifti_gradient_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_gradient(
    cifti: InputPathType,
    direction: str,
    cifti_out: str,
    left_surface: CiftiGradientLeftSurfaceParameters | None = None,
    right_surface: CiftiGradientRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiGradientCerebellumSurfaceParameters | None = None,
    opt_surface_presmooth_surface_kernel: float | None = None,
    opt_volume_presmooth_volume_kernel: float | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_average_output: bool = False,
    opt_vectors_vectors_out: str | None = None,
    runner: Runner | None = None,
) -> CiftiGradientOutputs:
    """
    Take gradient of a cifti file.
    
    Performs gradient calculation on each component of the cifti file, and
    optionally averages the resulting gradients. The -vectors and
    -average-output options may not be used together. You must specify a surface
    for each surface structure in the cifti file. The COLUMN direction should be
    faster, and is the direction that works on dtseries. For dconn, you probably
    want ROW, unless you are using -average-output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti: the input cifti.
        direction: which dimension to take the gradient along, ROW or COLUMN.
        cifti_out: the output cifti.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_surface_presmooth_surface_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian surface smoothing\
            kernel in mm, as sigma by default.
        opt_volume_presmooth_volume_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian volume smoothing\
            kernel in mm, as sigma by default.
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma.
        opt_average_output: output the average of the gradient magnitude maps\
            instead of each gradient map separately.
        opt_vectors_vectors_out: output gradient vectors: the vectors, as a\
            dscalar file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_GRADIENT_METADATA)
    params = cifti_gradient_params(
        cifti=cifti,
        direction=direction,
        cifti_out=cifti_out,
        left_surface=left_surface,
        right_surface=right_surface,
        cerebellum_surface=cerebellum_surface,
        opt_surface_presmooth_surface_kernel=opt_surface_presmooth_surface_kernel,
        opt_volume_presmooth_volume_kernel=opt_volume_presmooth_volume_kernel,
        opt_presmooth_fwhm=opt_presmooth_fwhm,
        opt_average_output=opt_average_output,
        opt_vectors_vectors_out=opt_vectors_vectors_out,
    )
    return cifti_gradient_execute(params, execution)


__all__ = [
    "CIFTI_GRADIENT_METADATA",
    "CiftiGradientCerebellumSurfaceParameters",
    "CiftiGradientLeftSurfaceParameters",
    "CiftiGradientOutputs",
    "CiftiGradientParameters",
    "CiftiGradientRightSurfaceParameters",
    "cifti_gradient",
    "cifti_gradient_cerebellum_surface_params",
    "cifti_gradient_left_surface_params",
    "cifti_gradient_params",
    "cifti_gradient_right_surface_params",
]
