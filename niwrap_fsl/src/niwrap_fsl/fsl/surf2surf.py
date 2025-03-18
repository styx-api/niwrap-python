# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF2SURF_METADATA = Metadata(
    id="33ef19f0111fbc0a4b52d93be653e4608d688aa7.boutiques",
    name="surf2surf",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Surf2surfParameters = typing.TypedDict('Surf2surfParameters', {
    "__STYX_TYPE__": typing.Literal["surf2surf"],
    "input_surface": InputPathType,
    "output_surface": InputPathType,
    "input_convention": typing.NotRequired[str | None],
    "output_convention": typing.NotRequired[str | None],
    "input_ref_volume": typing.NotRequired[InputPathType | None],
    "output_ref_volume": typing.NotRequired[InputPathType | None],
    "transform": typing.NotRequired[InputPathType | None],
    "output_type": typing.NotRequired[str | None],
    "output_values": typing.NotRequired[str | None],
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
        "surf2surf": surf2surf_cargs,
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


class Surf2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surf2surf_params(
    input_surface: InputPathType,
    output_surface: InputPathType,
    input_convention: str | None = None,
    output_convention: str | None = None,
    input_ref_volume: InputPathType | None = None,
    output_ref_volume: InputPathType | None = None,
    transform: InputPathType | None = None,
    output_type: str | None = None,
    output_values: str | None = None,
) -> Surf2surfParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface.
        output_surface: Output surface.
        input_convention: Input convention [default=caret] - only used if\
            output convention is different.
        output_convention: Output convention [default=same as input].
        input_ref_volume: Input reference volume - Must set this if changing\
            conventions.
        output_ref_volume: Output reference volume [default=same as input].
        transform: In-to-out ASCII matrix or out-to-in warpfield\
            [default=identity].
        output_type: Output type: ASCII, VTK, GIFTI_ASCII, GIFTI_BIN,\
            GIFTI_BIN_GZ (default).
        output_values: Set output scalar values (e.g.\
            --values=mysurface.func.gii or --values=1).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surf2surf",
        "input_surface": input_surface,
        "output_surface": output_surface,
    }
    if input_convention is not None:
        params["input_convention"] = input_convention
    if output_convention is not None:
        params["output_convention"] = output_convention
    if input_ref_volume is not None:
        params["input_ref_volume"] = input_ref_volume
    if output_ref_volume is not None:
        params["output_ref_volume"] = output_ref_volume
    if transform is not None:
        params["transform"] = transform
    if output_type is not None:
        params["output_type"] = output_type
    if output_values is not None:
        params["output_values"] = output_values
    return params


def surf2surf_cargs(
    params: Surf2surfParameters,
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
    cargs.append("surf2surf")
    cargs.append("--surfin=" + execution.input_file(params.get("input_surface")))
    cargs.append("--surfout=" + execution.input_file(params.get("output_surface")))
    if params.get("input_convention") is not None:
        cargs.extend([
            "--convin",
            params.get("input_convention")
        ])
    if params.get("output_convention") is not None:
        cargs.extend([
            "--convout",
            params.get("output_convention")
        ])
    if params.get("input_ref_volume") is not None:
        cargs.extend([
            "--volin",
            execution.input_file(params.get("input_ref_volume"))
        ])
    if params.get("output_ref_volume") is not None:
        cargs.extend([
            "--volout",
            execution.input_file(params.get("output_ref_volume"))
        ])
    if params.get("transform") is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(params.get("transform"))
        ])
    if params.get("output_type") is not None:
        cargs.extend([
            "--outputtype",
            params.get("output_type")
        ])
    if params.get("output_values") is not None:
        cargs.extend([
            "--values",
            params.get("output_values")
        ])
    return cargs


def surf2surf_outputs(
    params: Surf2surfParameters,
    execution: Execution,
) -> Surf2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Surf2surfOutputs(
        root=execution.output_file("."),
    )
    return ret


def surf2surf_execute(
    params: Surf2surfParameters,
    execution: Execution,
) -> Surf2surfOutputs:
    """
    Conversions between surface formats and/or conventions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Surf2surfOutputs`).
    """
    params = execution.params(params)
    cargs = surf2surf_cargs(params, execution)
    ret = surf2surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf2surf(
    input_surface: InputPathType,
    output_surface: InputPathType,
    input_convention: str | None = None,
    output_convention: str | None = None,
    input_ref_volume: InputPathType | None = None,
    output_ref_volume: InputPathType | None = None,
    transform: InputPathType | None = None,
    output_type: str | None = None,
    output_values: str | None = None,
    runner: Runner | None = None,
) -> Surf2surfOutputs:
    """
    Conversions between surface formats and/or conventions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_surface: Input surface.
        output_surface: Output surface.
        input_convention: Input convention [default=caret] - only used if\
            output convention is different.
        output_convention: Output convention [default=same as input].
        input_ref_volume: Input reference volume - Must set this if changing\
            conventions.
        output_ref_volume: Output reference volume [default=same as input].
        transform: In-to-out ASCII matrix or out-to-in warpfield\
            [default=identity].
        output_type: Output type: ASCII, VTK, GIFTI_ASCII, GIFTI_BIN,\
            GIFTI_BIN_GZ (default).
        output_values: Set output scalar values (e.g.\
            --values=mysurface.func.gii or --values=1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Surf2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF2SURF_METADATA)
    params = surf2surf_params(
        input_surface=input_surface,
        output_surface=output_surface,
        input_convention=input_convention,
        output_convention=output_convention,
        input_ref_volume=input_ref_volume,
        output_ref_volume=output_ref_volume,
        transform=transform,
        output_type=output_type,
        output_values=output_values,
    )
    return surf2surf_execute(params, execution)


__all__ = [
    "SURF2SURF_METADATA",
    "Surf2surfOutputs",
    "Surf2surfParameters",
    "surf2surf",
    "surf2surf_params",
]
