# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MINC2SEQINFO_METADATA = Metadata(
    id="d57928aac7b425a7a859150e95ea57280a4d9604.boutiques",
    name="minc2seqinfo",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Minc2seqinfoParameters = typing.TypedDict('Minc2seqinfoParameters', {
    "__STYXTYPE__": typing.Literal["minc2seqinfo"],
    "mincfile": InputPathType,
    "seqinfofile": str,
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
        "minc2seqinfo": minc2seqinfo_cargs,
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
        "minc2seqinfo": minc2seqinfo_outputs,
    }.get(t)


class Minc2seqinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `minc2seqinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_seqinfofile: OutputPathType
    """File containing the extracted sequence information."""


def minc2seqinfo_params(
    mincfile: InputPathType,
    seqinfofile: str,
) -> Minc2seqinfoParameters:
    """
    Build parameters.
    
    Args:
        mincfile: Input MINC file from which to extract sequence information.
        seqinfofile: Output file where the sequence information will be stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "minc2seqinfo",
        "mincfile": mincfile,
        "seqinfofile": seqinfofile,
    }
    return params


def minc2seqinfo_cargs(
    params: Minc2seqinfoParameters,
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
    cargs.append("minc2seqinfo")
    cargs.append(execution.input_file(params.get("mincfile")))
    cargs.append(params.get("seqinfofile"))
    return cargs


def minc2seqinfo_outputs(
    params: Minc2seqinfoParameters,
    execution: Execution,
) -> Minc2seqinfoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Minc2seqinfoOutputs(
        root=execution.output_file("."),
        out_seqinfofile=execution.output_file(params.get("seqinfofile")),
    )
    return ret


def minc2seqinfo_execute(
    params: Minc2seqinfoParameters,
    execution: Execution,
) -> Minc2seqinfoOutputs:
    """
    Tool for extracting sequence information from MINC files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Minc2seqinfoOutputs`).
    """
    params = execution.params(params)
    cargs = minc2seqinfo_cargs(params, execution)
    ret = minc2seqinfo_outputs(params, execution)
    execution.run(cargs)
    return ret


def minc2seqinfo(
    mincfile: InputPathType,
    seqinfofile: str,
    runner: Runner | None = None,
) -> Minc2seqinfoOutputs:
    """
    Tool for extracting sequence information from MINC files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mincfile: Input MINC file from which to extract sequence information.
        seqinfofile: Output file where the sequence information will be stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Minc2seqinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MINC2SEQINFO_METADATA)
    params = minc2seqinfo_params(
        mincfile=mincfile,
        seqinfofile=seqinfofile,
    )
    return minc2seqinfo_execute(params, execution)


__all__ = [
    "MINC2SEQINFO_METADATA",
    "Minc2seqinfoOutputs",
    "Minc2seqinfoParameters",
    "minc2seqinfo",
    "minc2seqinfo_params",
]
