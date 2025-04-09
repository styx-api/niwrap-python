# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIBER_DOT_PRODUCTS_METADATA = Metadata(
    id="6de4250098eba964a2de1317984029cbcc59eda2.boutiques",
    name="fiber-dot-products",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


FiberDotProductsParameters = typing.TypedDict('FiberDotProductsParameters', {
    "__STYX_TYPE__": typing.Literal["fiber-dot-products"],
    "white_surf": InputPathType,
    "fiber_file": InputPathType,
    "max_dist": float,
    "direction": str,
    "dot_metric": str,
    "f_metric": str,
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
        "fiber-dot-products": fiber_dot_products_cargs,
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
        "fiber-dot-products": fiber_dot_products_outputs,
    }.get(t)


class FiberDotProductsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fiber_dot_products(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dot_metric: OutputPathType
    """the metric of dot products"""
    f_metric: OutputPathType
    """a metric of the f values of the fiber distributions"""


def fiber_dot_products_params(
    white_surf: InputPathType,
    fiber_file: InputPathType,
    max_dist: float,
    direction: str,
    dot_metric: str,
    f_metric: str,
) -> FiberDotProductsParameters:
    """
    Build parameters.
    
    Args:
        white_surf: the white/gray boundary surface.
        fiber_file: the fiber orientation file.
        max_dist: the maximum distance from any surface vertex a fiber\
            population may be, in mm.
        direction: test against surface for whether a fiber population should\
            be used.
        dot_metric: the metric of dot products.
        f_metric: a metric of the f values of the fiber distributions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fiber-dot-products",
        "white_surf": white_surf,
        "fiber_file": fiber_file,
        "max_dist": max_dist,
        "direction": direction,
        "dot_metric": dot_metric,
        "f_metric": f_metric,
    }
    return params


def fiber_dot_products_cargs(
    params: FiberDotProductsParameters,
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
    cargs.append("-fiber-dot-products")
    cargs.append(execution.input_file(params.get("white_surf")))
    cargs.append(execution.input_file(params.get("fiber_file")))
    cargs.append(str(params.get("max_dist")))
    cargs.append(params.get("direction"))
    cargs.append(params.get("dot_metric"))
    cargs.append(params.get("f_metric"))
    return cargs


def fiber_dot_products_outputs(
    params: FiberDotProductsParameters,
    execution: Execution,
) -> FiberDotProductsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FiberDotProductsOutputs(
        root=execution.output_file("."),
        dot_metric=execution.output_file(params.get("dot_metric")),
        f_metric=execution.output_file(params.get("f_metric")),
    )
    return ret


def fiber_dot_products_execute(
    params: FiberDotProductsParameters,
    execution: Execution,
) -> FiberDotProductsOutputs:
    """
    Compute dot products of fiber orientations with surface normals.
    
    For each vertex, this command finds the closest fiber population that
    satisfies the <direction> test, and computes the absolute value of the dot
    product of the surface normal and the normalized mean direction of each
    fiber. The <direction> test must be one of INSIDE, OUTSIDE, or ANY, which
    causes the command to only use fiber populations that are inside the
    surface, outside the surface, or to not care which direction it is from the
    surface. Each fiber population is output in a separate metric column.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FiberDotProductsOutputs`).
    """
    params = execution.params(params)
    cargs = fiber_dot_products_cargs(params, execution)
    ret = fiber_dot_products_outputs(params, execution)
    execution.run(cargs)
    return ret


def fiber_dot_products(
    white_surf: InputPathType,
    fiber_file: InputPathType,
    max_dist: float,
    direction: str,
    dot_metric: str,
    f_metric: str,
    runner: Runner | None = None,
) -> FiberDotProductsOutputs:
    """
    Compute dot products of fiber orientations with surface normals.
    
    For each vertex, this command finds the closest fiber population that
    satisfies the <direction> test, and computes the absolute value of the dot
    product of the surface normal and the normalized mean direction of each
    fiber. The <direction> test must be one of INSIDE, OUTSIDE, or ANY, which
    causes the command to only use fiber populations that are inside the
    surface, outside the surface, or to not care which direction it is from the
    surface. Each fiber population is output in a separate metric column.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        white_surf: the white/gray boundary surface.
        fiber_file: the fiber orientation file.
        max_dist: the maximum distance from any surface vertex a fiber\
            population may be, in mm.
        direction: test against surface for whether a fiber population should\
            be used.
        dot_metric: the metric of dot products.
        f_metric: a metric of the f values of the fiber distributions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FiberDotProductsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIBER_DOT_PRODUCTS_METADATA)
    params = fiber_dot_products_params(
        white_surf=white_surf,
        fiber_file=fiber_file,
        max_dist=max_dist,
        direction=direction,
        dot_metric=dot_metric,
        f_metric=f_metric,
    )
    return fiber_dot_products_execute(params, execution)


__all__ = [
    "FIBER_DOT_PRODUCTS_METADATA",
    "FiberDotProductsOutputs",
    "FiberDotProductsParameters",
    "fiber_dot_products",
    "fiber_dot_products_params",
]
