# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_BASED_SMOOTHING_METADATA = Metadata(
    id="0f212837e6cfdb7d79585c7f58fe041aca5a9ef1.boutiques",
    name="SurfaceBasedSmoothing",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


SurfaceBasedSmoothingParameters = typing.TypedDict('SurfaceBasedSmoothingParameters', {
    "__STYXTYPE__": typing.Literal["SurfaceBasedSmoothing"],
    "image_to_smooth": InputPathType,
    "sigma": float,
    "surface_image": InputPathType,
    "outname": str,
    "num_repeats": typing.NotRequired[int | None],
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
        "SurfaceBasedSmoothing": surface_based_smoothing_cargs,
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
        "SurfaceBasedSmoothing": surface_based_smoothing_outputs,
    }.get(t)


class SurfaceBasedSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_based_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    smoothed_output: OutputPathType
    """The output smoothed image."""


def surface_based_smoothing_params(
    image_to_smooth: InputPathType,
    sigma: float,
    surface_image: InputPathType,
    outname: str,
    num_repeats: int | None = None,
) -> SurfaceBasedSmoothingParameters:
    """
    Build parameters.
    
    Args:
        image_to_smooth: The image that needs to be smoothed.
        sigma: Geodesic neighborhood radius.
        surface_image: Assumes a label == 1 that defines the surface.
        outname: The name of the output file.
        num_repeats: Number of times the geodesic neighborhood is applied\
            repeatedly.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfaceBasedSmoothing",
        "image_to_smooth": image_to_smooth,
        "sigma": sigma,
        "surface_image": surface_image,
        "outname": outname,
    }
    if num_repeats is not None:
        params["num_repeats"] = num_repeats
    return params


def surface_based_smoothing_cargs(
    params: SurfaceBasedSmoothingParameters,
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
    cargs.append("SurfaceBasedSmoothing")
    cargs.append(execution.input_file(params.get("image_to_smooth")))
    cargs.append(str(params.get("sigma")))
    cargs.append(execution.input_file(params.get("surface_image")))
    cargs.append(params.get("outname"))
    if params.get("num_repeats") is not None:
        cargs.append(str(params.get("num_repeats")))
    return cargs


def surface_based_smoothing_outputs(
    params: SurfaceBasedSmoothingParameters,
    execution: Execution,
) -> SurfaceBasedSmoothingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceBasedSmoothingOutputs(
        root=execution.output_file("."),
        smoothed_output=execution.output_file(params.get("outname")),
    )
    return ret


def surface_based_smoothing_execute(
    params: SurfaceBasedSmoothingParameters,
    execution: Execution,
) -> SurfaceBasedSmoothingOutputs:
    """
    Surface-based smoothing applied to ImageToSmooth using a geodesic neighbourhood
    defined by sigma and the surface image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceBasedSmoothingOutputs`).
    """
    params = execution.params(params)
    cargs = surface_based_smoothing_cargs(params, execution)
    ret = surface_based_smoothing_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_based_smoothing(
    image_to_smooth: InputPathType,
    sigma: float,
    surface_image: InputPathType,
    outname: str,
    num_repeats: int | None = None,
    runner: Runner | None = None,
) -> SurfaceBasedSmoothingOutputs:
    """
    Surface-based smoothing applied to ImageToSmooth using a geodesic neighbourhood
    defined by sigma and the surface image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_to_smooth: The image that needs to be smoothed.
        sigma: Geodesic neighborhood radius.
        surface_image: Assumes a label == 1 that defines the surface.
        outname: The name of the output file.
        num_repeats: Number of times the geodesic neighborhood is applied\
            repeatedly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceBasedSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_BASED_SMOOTHING_METADATA)
    params = surface_based_smoothing_params(
        image_to_smooth=image_to_smooth,
        sigma=sigma,
        surface_image=surface_image,
        outname=outname,
        num_repeats=num_repeats,
    )
    return surface_based_smoothing_execute(params, execution)


__all__ = [
    "SURFACE_BASED_SMOOTHING_METADATA",
    "SurfaceBasedSmoothingOutputs",
    "SurfaceBasedSmoothingParameters",
    "surface_based_smoothing",
    "surface_based_smoothing_params",
]
