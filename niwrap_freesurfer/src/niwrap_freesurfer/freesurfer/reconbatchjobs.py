# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RECONBATCHJOBS_METADATA = Metadata(
    id="3b88343e632e9bbafdf43ea3df14e2cf0c3f34d1.boutiques",
    name="reconbatchjobs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


ReconbatchjobsParameters = typing.TypedDict('ReconbatchjobsParameters', {
    "__STYXTYPE__": typing.Literal["reconbatchjobs"],
    "logfile": str,
    "cmdfiles": list[str],
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
        "reconbatchjobs": reconbatchjobs_cargs,
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


class ReconbatchjobsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reconbatchjobs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def reconbatchjobs_params(
    logfile: str,
    cmdfiles: list[str],
) -> ReconbatchjobsParameters:
    """
    Build parameters.
    
    Args:
        logfile: Log file to capture output of batch jobs.
        cmdfiles: Command files for batch processing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reconbatchjobs",
        "logfile": logfile,
        "cmdfiles": cmdfiles,
    }
    return params


def reconbatchjobs_cargs(
    params: ReconbatchjobsParameters,
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
    cargs.append("reconbatchjobs")
    cargs.append(params.get("logfile"))
    cargs.extend(params.get("cmdfiles"))
    return cargs


def reconbatchjobs_outputs(
    params: ReconbatchjobsParameters,
    execution: Execution,
) -> ReconbatchjobsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReconbatchjobsOutputs(
        root=execution.output_file("."),
    )
    return ret


def reconbatchjobs_execute(
    params: ReconbatchjobsParameters,
    execution: Execution,
) -> ReconbatchjobsOutputs:
    """
    Batch job processor for reconstruction scripts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReconbatchjobsOutputs`).
    """
    params = execution.params(params)
    cargs = reconbatchjobs_cargs(params, execution)
    ret = reconbatchjobs_outputs(params, execution)
    execution.run(cargs)
    return ret


def reconbatchjobs(
    logfile: str,
    cmdfiles: list[str],
    runner: Runner | None = None,
) -> ReconbatchjobsOutputs:
    """
    Batch job processor for reconstruction scripts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        logfile: Log file to capture output of batch jobs.
        cmdfiles: Command files for batch processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconbatchjobsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECONBATCHJOBS_METADATA)
    params = reconbatchjobs_params(
        logfile=logfile,
        cmdfiles=cmdfiles,
    )
    return reconbatchjobs_execute(params, execution)


__all__ = [
    "RECONBATCHJOBS_METADATA",
    "ReconbatchjobsOutputs",
    "ReconbatchjobsParameters",
    "reconbatchjobs",
    "reconbatchjobs_params",
]
