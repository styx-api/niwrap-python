# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ZEROPAD_METADATA = Metadata(
    id="59ec07bb1e922d973d58ef847258171ce673bab0.boutiques",
    name="zeropad",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ZeropadParameters = typing.TypedDict('ZeropadParameters', {
    "__STYX_TYPE__": typing.Literal["zeropad"],
    "input_number": str,
    "length": float,
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
        "zeropad": zeropad_cargs,
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
        "zeropad": zeropad_outputs,
    }.get(t)


class ZeropadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `zeropad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """File containing the zero-padded output"""


def zeropad_params(
    input_number: str,
    length: float,
) -> ZeropadParameters:
    """
    Build parameters.
    
    Args:
        input_number: Input number to be zero-padded.
        length: Desired length of the output string.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "zeropad",
        "input_number": input_number,
        "length": length,
    }
    return params


def zeropad_cargs(
    params: ZeropadParameters,
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
    cargs.append("zeropad")
    cargs.append(params.get("input_number"))
    cargs.append(str(params.get("length")))
    return cargs


def zeropad_outputs(
    params: ZeropadParameters,
    execution: Execution,
) -> ZeropadOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ZeropadOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("padded_output.txt"),
    )
    return ret


def zeropad_execute(
    params: ZeropadParameters,
    execution: Execution,
) -> ZeropadOutputs:
    """
    Tool for zero-padding numbers to a specified length.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ZeropadOutputs`).
    """
    params = execution.params(params)
    cargs = zeropad_cargs(params, execution)
    ret = zeropad_outputs(params, execution)
    execution.run(cargs)
    return ret


def zeropad(
    input_number: str,
    length: float,
    runner: Runner | None = None,
) -> ZeropadOutputs:
    """
    Tool for zero-padding numbers to a specified length.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_number: Input number to be zero-padded.
        length: Desired length of the output string.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ZeropadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZEROPAD_METADATA)
    params = zeropad_params(
        input_number=input_number,
        length=length,
    )
    return zeropad_execute(params, execution)


__all__ = [
    "ZEROPAD_METADATA",
    "ZeropadOutputs",
    "ZeropadParameters",
    "zeropad",
    "zeropad_params",
]
