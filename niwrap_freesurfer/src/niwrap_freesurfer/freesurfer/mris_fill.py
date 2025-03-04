# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_FILL_METADATA = Metadata(
    id="c5656563cf43beb0f218120cdf33a3244a656aa3.boutiques",
    name="mris_fill",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisFillParameters = typing.TypedDict('MrisFillParameters', {
    "__STYX_TYPE__": typing.Literal["mris_fill"],
    "resolution": typing.NotRequired[float | None],
    "conform": bool,
    "input_surface": InputPathType,
    "output_volume": str,
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
        "mris_fill": mris_fill_cargs,
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
        "mris_fill": mris_fill_outputs,
    }.get(t)


class MrisFillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_fill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filled_volume: OutputPathType
    """The resulting filled volume output."""


def mris_fill_params(
    input_surface: InputPathType,
    output_volume: str,
    resolution: float | None = None,
    conform: bool = False,
) -> MrisFillParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        output_volume: Output volume file.
        resolution: Set the resolution of the output volume (default = 0.250\
            mm/voxel).
        conform: Conform the volume before writing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_fill",
        "conform": conform,
        "input_surface": input_surface,
        "output_volume": output_volume,
    }
    if resolution is not None:
        params["resolution"] = resolution
    return params


def mris_fill_cargs(
    params: MrisFillParameters,
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
    cargs.append("mris_fill")
    if params.get("resolution") is not None:
        cargs.extend([
            "-r",
            str(params.get("resolution"))
        ])
    if params.get("conform"):
        cargs.append("-c")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_volume"))
    return cargs


def mris_fill_outputs(
    params: MrisFillParameters,
    execution: Execution,
) -> MrisFillOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisFillOutputs(
        root=execution.output_file("."),
        filled_volume=execution.output_file(params.get("output_volume")),
    )
    return ret


def mris_fill_execute(
    params: MrisFillParameters,
    execution: Execution,
) -> MrisFillOutputs:
    """
    A tool that floodfills the interior of a surface and writes the results into a
    volume of specified resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisFillOutputs`).
    """
    params = execution.params(params)
    cargs = mris_fill_cargs(params, execution)
    ret = mris_fill_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_fill(
    input_surface: InputPathType,
    output_volume: str,
    resolution: float | None = None,
    conform: bool = False,
    runner: Runner | None = None,
) -> MrisFillOutputs:
    """
    A tool that floodfills the interior of a surface and writes the results into a
    volume of specified resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_volume: Output volume file.
        resolution: Set the resolution of the output volume (default = 0.250\
            mm/voxel).
        conform: Conform the volume before writing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FILL_METADATA)
    params = mris_fill_params(
        resolution=resolution,
        conform=conform,
        input_surface=input_surface,
        output_volume=output_volume,
    )
    return mris_fill_execute(params, execution)


__all__ = [
    "MRIS_FILL_METADATA",
    "MrisFillOutputs",
    "MrisFillParameters",
    "mris_fill",
    "mris_fill_params",
]
