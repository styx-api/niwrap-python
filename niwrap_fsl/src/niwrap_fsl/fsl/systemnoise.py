# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SYSTEMNOISE_METADATA = Metadata(
    id="9fe5bc1f78d1d88a6ab74a4fea8df0c29e9b2d19.boutiques",
    name="systemnoise",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SystemnoiseParameters = typing.TypedDict('SystemnoiseParameters', {
    "__STYXTYPE__": typing.Literal["systemnoise"],
    "input_signal": InputPathType,
    "output_signal": str,
    "noise_standard_deviation": float,
    "seed": typing.NotRequired[float | None],
    "verbose_flag": bool,
    "help_flag": bool,
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
        "systemnoise": systemnoise_cargs,
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
        "systemnoise": systemnoise_outputs,
    }.get(t)


class SystemnoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `systemnoise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_signal_file: OutputPathType
    """Output signal with added system noise"""


def systemnoise_params(
    input_signal: InputPathType,
    output_signal: str,
    noise_standard_deviation: float,
    seed: float | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> SystemnoiseParameters:
    """
    Build parameters.
    
    Args:
        input_signal: Input signal (possum output matrix).
        output_signal: Output signal (possum matrix form).
        noise_standard_deviation: Set noise standard deviation (units of\
            intensity).
        seed: Input seed value for the sequence.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "systemnoise",
        "input_signal": input_signal,
        "output_signal": output_signal,
        "noise_standard_deviation": noise_standard_deviation,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if seed is not None:
        params["seed"] = seed
    return params


def systemnoise_cargs(
    params: SystemnoiseParameters,
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
    cargs.append("systemnoise")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_signal"))
    ])
    cargs.extend([
        "--out",
        params.get("output_signal")
    ])
    cargs.extend([
        "--sigma",
        str(params.get("noise_standard_deviation"))
    ])
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def systemnoise_outputs(
    params: SystemnoiseParameters,
    execution: Execution,
) -> SystemnoiseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SystemnoiseOutputs(
        root=execution.output_file("."),
        output_signal_file=execution.output_file(params.get("output_signal")),
    )
    return ret


def systemnoise_execute(
    params: SystemnoiseParameters,
    execution: Execution,
) -> SystemnoiseOutputs:
    """
    Tool for adding system noise to a given signal using FSL's utilities.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SystemnoiseOutputs`).
    """
    params = execution.params(params)
    cargs = systemnoise_cargs(params, execution)
    ret = systemnoise_outputs(params, execution)
    execution.run(cargs)
    return ret


def systemnoise(
    input_signal: InputPathType,
    output_signal: str,
    noise_standard_deviation: float,
    seed: float | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> SystemnoiseOutputs:
    """
    Tool for adding system noise to a given signal using FSL's utilities.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_signal: Input signal (possum output matrix).
        output_signal: Output signal (possum matrix form).
        noise_standard_deviation: Set noise standard deviation (units of\
            intensity).
        seed: Input seed value for the sequence.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SystemnoiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SYSTEMNOISE_METADATA)
    params = systemnoise_params(
        input_signal=input_signal,
        output_signal=output_signal,
        noise_standard_deviation=noise_standard_deviation,
        seed=seed,
        verbose_flag=verbose_flag,
        help_flag=help_flag,
    )
    return systemnoise_execute(params, execution)


__all__ = [
    "SYSTEMNOISE_METADATA",
    "SystemnoiseOutputs",
    "SystemnoiseParameters",
    "systemnoise",
    "systemnoise_params",
]
