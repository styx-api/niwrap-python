# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_REPOSITION_SURFACE_METADATA = Metadata(
    id="0c77cbb7786fb79ce602e33afe3529727da1fb02.boutiques",
    name="mris_reposition_surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisRepositionSurfaceParameters = typing.TypedDict('MrisRepositionSurfaceParameters', {
    "__STYXTYPE__": typing.Literal["mris_reposition_surface"],
    "surf": InputPathType,
    "volume": InputPathType,
    "points": InputPathType,
    "output": str,
    "size": typing.NotRequired[float | None],
    "sigma": typing.NotRequired[float | None],
    "iterations": typing.NotRequired[float | None],
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
        "mris_reposition_surface": mris_reposition_surface_cargs,
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
        "mris_reposition_surface": mris_reposition_surface_outputs,
    }.get(t)


class MrisRepositionSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_reposition_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface file"""


def mris_reposition_surface_params(
    surf: InputPathType,
    volume: InputPathType,
    points: InputPathType,
    output: str,
    size: float | None = 1,
    sigma: float | None = 2.0,
    iterations: float | None = 1,
) -> MrisRepositionSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surf: Input surface.
        volume: Input volume.
        points: Input points.
        output: Output surface filename.
        size: Size parameter for repositioning. Default is 1.
        sigma: Sigma. Default is 2.0.
        iterations: Number of iterations. Default is 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_reposition_surface",
        "surf": surf,
        "volume": volume,
        "points": points,
        "output": output,
    }
    if size is not None:
        params["size"] = size
    if sigma is not None:
        params["sigma"] = sigma
    if iterations is not None:
        params["iterations"] = iterations
    return params


def mris_reposition_surface_cargs(
    params: MrisRepositionSurfaceParameters,
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
    cargs.append("mris_reposition_surface")
    cargs.extend([
        "-s",
        execution.input_file(params.get("surf"))
    ])
    cargs.extend([
        "-v",
        execution.input_file(params.get("volume"))
    ])
    cargs.extend([
        "-p",
        execution.input_file(params.get("points"))
    ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("size") is not None:
        cargs.extend([
            "-z",
            str(params.get("size"))
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "-g",
            str(params.get("sigma"))
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "-i",
            str(params.get("iterations"))
        ])
    return cargs


def mris_reposition_surface_outputs(
    params: MrisRepositionSurfaceParameters,
    execution: Execution,
) -> MrisRepositionSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRepositionSurfaceOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(params.get("output")),
    )
    return ret


def mris_reposition_surface_execute(
    params: MrisRepositionSurfaceParameters,
    execution: Execution,
) -> MrisRepositionSurfaceOutputs:
    """
    Reposition a surface based on the given control points (in JSON format).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRepositionSurfaceOutputs`).
    """
    params = execution.params(params)
    cargs = mris_reposition_surface_cargs(params, execution)
    ret = mris_reposition_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_reposition_surface(
    surf: InputPathType,
    volume: InputPathType,
    points: InputPathType,
    output: str,
    size: float | None = 1,
    sigma: float | None = 2.0,
    iterations: float | None = 1,
    runner: Runner | None = None,
) -> MrisRepositionSurfaceOutputs:
    """
    Reposition a surface based on the given control points (in JSON format).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf: Input surface.
        volume: Input volume.
        points: Input points.
        output: Output surface filename.
        size: Size parameter for repositioning. Default is 1.
        sigma: Sigma. Default is 2.0.
        iterations: Number of iterations. Default is 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRepositionSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REPOSITION_SURFACE_METADATA)
    params = mris_reposition_surface_params(
        surf=surf,
        volume=volume,
        points=points,
        output=output,
        size=size,
        sigma=sigma,
        iterations=iterations,
    )
    return mris_reposition_surface_execute(params, execution)


__all__ = [
    "MRIS_REPOSITION_SURFACE_METADATA",
    "MrisRepositionSurfaceOutputs",
    "MrisRepositionSurfaceParameters",
    "mris_reposition_surface",
    "mris_reposition_surface_params",
]
