# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_LABEL_CALC_METADATA = Metadata(
    id="d93d02a327398015e84d46734009d6fa6287d4ae.boutiques",
    name="mris_label_calc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisLabelCalcParameters = typing.TypedDict('MrisLabelCalcParameters', {
    "__STYX_TYPE__": typing.Literal["mris_label_calc"],
    "command": typing.Literal["union", "intersect", "invert", "erode", "dilate"],
    "input1": InputPathType,
    "input2": InputPathType,
    "output": str,
    "iterations": typing.NotRequired[int | None],
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
        "mris_label_calc": mris_label_calc_cargs,
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
        "mris_label_calc": mris_label_calc_outputs,
    }.get(t)


class MrisLabelCalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label_calc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label: OutputPathType
    """The resulting label file after operation"""


def mris_label_calc_params(
    command: typing.Literal["union", "intersect", "invert", "erode", "dilate"],
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    iterations: int | None = None,
) -> MrisLabelCalcParameters:
    """
    Build parameters.
    
    Args:
        command: Command to perform on input labels.
        input1: First input label file.
        input2: Second input label file (used for 'invert', 'erode', 'dilate'\
            operations).
        output: Output label file.
        iterations: Number of times to erode or dilate label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_label_calc",
        "command": command,
        "input1": input1,
        "input2": input2,
        "output": output,
    }
    if iterations is not None:
        params["iterations"] = iterations
    return params


def mris_label_calc_cargs(
    params: MrisLabelCalcParameters,
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
    cargs.append("mris_label_calc")
    cargs.append(params.get("command"))
    cargs.append(execution.input_file(params.get("input1")))
    cargs.append(execution.input_file(params.get("input2")))
    cargs.append(params.get("output"))
    if params.get("iterations") is not None:
        cargs.extend([
            "<n>",
            str(params.get("iterations"))
        ])
    return cargs


def mris_label_calc_outputs(
    params: MrisLabelCalcParameters,
    execution: Execution,
) -> MrisLabelCalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisLabelCalcOutputs(
        root=execution.output_file("."),
        output_label=execution.output_file(params.get("output") + ".label"),
    )
    return ret


def mris_label_calc_execute(
    params: MrisLabelCalcParameters,
    execution: Execution,
) -> MrisLabelCalcOutputs:
    """
    Tool for surface label calculations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisLabelCalcOutputs`).
    """
    params = execution.params(params)
    cargs = mris_label_calc_cargs(params, execution)
    ret = mris_label_calc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_label_calc(
    command: typing.Literal["union", "intersect", "invert", "erode", "dilate"],
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    iterations: int | None = None,
    runner: Runner | None = None,
) -> MrisLabelCalcOutputs:
    """
    Tool for surface label calculations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        command: Command to perform on input labels.
        input1: First input label file.
        input2: Second input label file (used for 'invert', 'erode', 'dilate'\
            operations).
        output: Output label file.
        iterations: Number of times to erode or dilate label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabelCalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL_CALC_METADATA)
    params = mris_label_calc_params(
        command=command,
        input1=input1,
        input2=input2,
        output=output,
        iterations=iterations,
    )
    return mris_label_calc_execute(params, execution)


__all__ = [
    "MRIS_LABEL_CALC_METADATA",
    "MrisLabelCalcOutputs",
    "MrisLabelCalcParameters",
    "mris_label_calc",
    "mris_label_calc_params",
]
