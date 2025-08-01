# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IFH2HDR_METADATA = Metadata(
    id="e59ad437a43879fdeda8a194eb2d5e26f853b35c.boutiques",
    name="ifh2hdr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Ifh2hdrParameters = typing.TypedDict('Ifh2hdrParameters', {
    "__STYXTYPE__": typing.Literal["ifh2hdr"],
    "input_file": InputPathType,
    "range": typing.NotRequired[str | None],
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
        "ifh2hdr": ifh2hdr_cargs,
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


class Ifh2hdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ifh2hdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ifh2hdr_params(
    input_file: InputPathType,
    range_: str | None = None,
) -> Ifh2hdrParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input 4dfp file.
        range_: Set range for the 4dfp file. Format: <float>[to<float>].
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ifh2hdr",
        "input_file": input_file,
    }
    if range_ is not None:
        params["range"] = range_
    return params


def ifh2hdr_cargs(
    params: Ifh2hdrParameters,
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
    cargs.append("ifh2hdr")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("range") is not None:
        cargs.extend([
            "-r",
            params.get("range")
        ])
    return cargs


def ifh2hdr_outputs(
    params: Ifh2hdrParameters,
    execution: Execution,
) -> Ifh2hdrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Ifh2hdrOutputs(
        root=execution.output_file("."),
    )
    return ret


def ifh2hdr_execute(
    params: Ifh2hdrParameters,
    execution: Execution,
) -> Ifh2hdrOutputs:
    """
    Tool for converting IFH (Interfile Header) to HDR (Header) format in 4dfp
    (Four-Dimensional Functional Image) file format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Ifh2hdrOutputs`).
    """
    params = execution.params(params)
    cargs = ifh2hdr_cargs(params, execution)
    ret = ifh2hdr_outputs(params, execution)
    execution.run(cargs)
    return ret


def ifh2hdr(
    input_file: InputPathType,
    range_: str | None = None,
    runner: Runner | None = None,
) -> Ifh2hdrOutputs:
    """
    Tool for converting IFH (Interfile Header) to HDR (Header) format in 4dfp
    (Four-Dimensional Functional Image) file format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input 4dfp file.
        range_: Set range for the 4dfp file. Format: <float>[to<float>].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Ifh2hdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IFH2HDR_METADATA)
    params = ifh2hdr_params(
        input_file=input_file,
        range_=range_,
    )
    return ifh2hdr_execute(params, execution)


__all__ = [
    "IFH2HDR_METADATA",
    "Ifh2hdrOutputs",
    "Ifh2hdrParameters",
    "ifh2hdr",
    "ifh2hdr_params",
]
