# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

POSSUM_SUM_METADATA = Metadata(
    id="ef2112c90178573702ee927a708c1c298290752b.boutiques",
    name="possum_sum",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PossumSumParameters = typing.TypedDict('PossumSumParameters', {
    "__STYX_TYPE__": typing.Literal["possum_sum"],
    "input_signal": InputPathType,
    "output_signal": str,
    "num_processors": typing.NotRequired[int | None],
    "verbose_flag": bool,
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
        "possum_sum": possum_sum_cargs,
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
        "possum_sum": possum_sum_outputs,
    }.get(t)


class PossumSumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_sum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Sum of all input signals from processors"""


def possum_sum_params(
    input_signal: InputPathType,
    output_signal: str,
    num_processors: int | None = None,
    verbose_flag: bool = False,
) -> PossumSumParameters:
    """
    Build parameters.
    
    Args:
        input_signal: Input signal for one processor (possum output matrix).
        output_signal: Output signal: sum of all the processors (possum matrix\
            form).
        num_processors: Number of processors.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "possum_sum",
        "input_signal": input_signal,
        "output_signal": output_signal,
        "verbose_flag": verbose_flag,
    }
    if num_processors is not None:
        params["num_processors"] = num_processors
    return params


def possum_sum_cargs(
    params: PossumSumParameters,
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
    cargs.append("possum_sum")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_signal"))
    ])
    cargs.extend([
        "-o",
        params.get("output_signal")
    ])
    if params.get("num_processors") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_processors"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def possum_sum_outputs(
    params: PossumSumParameters,
    execution: Execution,
) -> PossumSumOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PossumSumOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_signal")),
    )
    return ret


def possum_sum_execute(
    params: PossumSumParameters,
    execution: Execution,
) -> PossumSumOutputs:
    """
    Sum of output signals from multiple possum processors.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PossumSumOutputs`).
    """
    params = execution.params(params)
    cargs = possum_sum_cargs(params, execution)
    ret = possum_sum_outputs(params, execution)
    execution.run(cargs)
    return ret


def possum_sum(
    input_signal: InputPathType,
    output_signal: str,
    num_processors: int | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> PossumSumOutputs:
    """
    Sum of output signals from multiple possum processors.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_signal: Input signal for one processor (possum output matrix).
        output_signal: Output signal: sum of all the processors (possum matrix\
            form).
        num_processors: Number of processors.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumSumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_SUM_METADATA)
    params = possum_sum_params(
        input_signal=input_signal,
        output_signal=output_signal,
        num_processors=num_processors,
        verbose_flag=verbose_flag,
    )
    return possum_sum_execute(params, execution)


__all__ = [
    "POSSUM_SUM_METADATA",
    "PossumSumOutputs",
    "PossumSumParameters",
    "possum_sum",
    "possum_sum_params",
]
