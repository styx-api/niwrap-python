# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TAL_QC_AZS_METADATA = Metadata(
    id="886563f0c6afbd7ecc04616fab1fcccc741bff0c.boutiques",
    name="tal_QC_AZS",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TalQcAzsParameters = typing.TypedDict('TalQcAzsParameters', {
    "__STYXTYPE__": typing.Literal["tal_QC_AZS"],
    "logfile": InputPathType,
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
        "tal_QC_AZS": tal_qc_azs_cargs,
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


class TalQcAzsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tal_qc_azs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tal_qc_azs_params(
    logfile: InputPathType,
) -> TalQcAzsParameters:
    """
    Build parameters.
    
    Args:
        logfile: Input logfile for processing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tal_QC_AZS",
        "logfile": logfile,
    }
    return params


def tal_qc_azs_cargs(
    params: TalQcAzsParameters,
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
    cargs.append("tal_QC_AZS")
    cargs.append(execution.input_file(params.get("logfile")))
    return cargs


def tal_qc_azs_outputs(
    params: TalQcAzsParameters,
    execution: Execution,
) -> TalQcAzsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TalQcAzsOutputs(
        root=execution.output_file("."),
    )
    return ret


def tal_qc_azs_execute(
    params: TalQcAzsParameters,
    execution: Execution,
) -> TalQcAzsOutputs:
    """
    A tool that processes a logfile.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TalQcAzsOutputs`).
    """
    params = execution.params(params)
    cargs = tal_qc_azs_cargs(params, execution)
    ret = tal_qc_azs_outputs(params, execution)
    execution.run(cargs)
    return ret


def tal_qc_azs(
    logfile: InputPathType,
    runner: Runner | None = None,
) -> TalQcAzsOutputs:
    """
    A tool that processes a logfile.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        logfile: Input logfile for processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalQcAzsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TAL_QC_AZS_METADATA)
    params = tal_qc_azs_params(
        logfile=logfile,
    )
    return tal_qc_azs_execute(params, execution)


__all__ = [
    "TAL_QC_AZS_METADATA",
    "TalQcAzsOutputs",
    "TalQcAzsParameters",
    "tal_qc_azs",
    "tal_qc_azs_params",
]
