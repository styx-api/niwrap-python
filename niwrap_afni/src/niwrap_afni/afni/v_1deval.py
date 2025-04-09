# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1DEVAL_METADATA = Metadata(
    id="2d05acc3dd71b6fa154f28feedd32f1badace561.boutiques",
    name="1deval",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V1devalParameters = typing.TypedDict('V1devalParameters', {
    "__STYX_TYPE__": typing.Literal["1deval"],
    "del": typing.NotRequired[float | None],
    "start": typing.NotRequired[float | None],
    "num": typing.NotRequired[float | None],
    "index": typing.NotRequired[InputPathType | None],
    "1D": bool,
    "symbols": typing.NotRequired[list[InputPathType] | None],
    "symbol_values": typing.NotRequired[list[str] | None],
    "expression": str,
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
        "1deval": v_1deval_cargs,
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
        "1deval": v_1deval_outputs,
    }.get(t)


class V1devalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1deval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_1_d: OutputPathType
    """Output of evaluated expression."""


def v_1deval_params(
    expression: str,
    del_: float | None = None,
    start: float | None = None,
    num: float | None = None,
    index: InputPathType | None = None,
    v_1_d: bool = False,
    symbols: list[InputPathType] | None = None,
    symbol_values: list[str] | None = None,
) -> V1devalParameters:
    """
    Build parameters.
    
    Args:
        expression: Expression to evaluate.
        del_: Use 'd' as the step for a single undetermined variable in the\
            expression.
        start: Start at value 's' for a single undetermined variable in the\
            expression.
        num: Evaluate the expression 'n' times.
        index: Read index column from file i.1D and write it out as 1st column\
            of output.
        v_1_d: Write output in the form of a single '1D:' string suitable for\
            input on the command line of another program.
        symbols: Read time series file and assign it to the symbol 'a'. Letters\
            'a' to 'z' may be used as symbols.
        symbol_values: Assign a fixed numerical value to the symbol 'a'.\
            Letters 'a' to 'z' may be used as symbols.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1deval",
        "1D": v_1_d,
        "expression": expression,
    }
    if del_ is not None:
        params["del"] = del_
    if start is not None:
        params["start"] = start
    if num is not None:
        params["num"] = num
    if index is not None:
        params["index"] = index
    if symbols is not None:
        params["symbols"] = symbols
    if symbol_values is not None:
        params["symbol_values"] = symbol_values
    return params


def v_1deval_cargs(
    params: V1devalParameters,
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
    cargs.append("1deval")
    if params.get("del") is not None:
        cargs.extend([
            "-del",
            str(params.get("del"))
        ])
    if params.get("start") is not None:
        cargs.extend([
            "-start",
            str(params.get("start"))
        ])
    if params.get("num") is not None:
        cargs.extend([
            "-num",
            str(params.get("num"))
        ])
    if params.get("index") is not None:
        cargs.extend([
            "-index",
            execution.input_file(params.get("index"))
        ])
    if params.get("1D"):
        cargs.append("-1D:")
    if params.get("symbols") is not None:
        cargs.extend([
            "-a",
            *[execution.input_file(f) for f in params.get("symbols")]
        ])
    if params.get("symbol_values") is not None:
        cargs.extend([
            "-a=",
            *params.get("symbol_values")
        ])
    cargs.extend([
        "-expr",
        params.get("expression")
    ])
    return cargs


def v_1deval_outputs(
    params: V1devalParameters,
    execution: Execution,
) -> V1devalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1devalOutputs(
        root=execution.output_file("."),
        output_1_d=execution.output_file("output.1D"),
    )
    return ret


def v_1deval_execute(
    params: V1devalParameters,
    execution: Execution,
) -> V1devalOutputs:
    """
    Evaluates an expression that may include columns of data from one or more text
    files and writes the result to stdout.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1devalOutputs`).
    """
    params = execution.params(params)
    cargs = v_1deval_cargs(params, execution)
    ret = v_1deval_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1deval(
    expression: str,
    del_: float | None = None,
    start: float | None = None,
    num: float | None = None,
    index: InputPathType | None = None,
    v_1_d: bool = False,
    symbols: list[InputPathType] | None = None,
    symbol_values: list[str] | None = None,
    runner: Runner | None = None,
) -> V1devalOutputs:
    """
    Evaluates an expression that may include columns of data from one or more text
    files and writes the result to stdout.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expression: Expression to evaluate.
        del_: Use 'd' as the step for a single undetermined variable in the\
            expression.
        start: Start at value 's' for a single undetermined variable in the\
            expression.
        num: Evaluate the expression 'n' times.
        index: Read index column from file i.1D and write it out as 1st column\
            of output.
        v_1_d: Write output in the form of a single '1D:' string suitable for\
            input on the command line of another program.
        symbols: Read time series file and assign it to the symbol 'a'. Letters\
            'a' to 'z' may be used as symbols.
        symbol_values: Assign a fixed numerical value to the symbol 'a'.\
            Letters 'a' to 'z' may be used as symbols.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1devalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DEVAL_METADATA)
    params = v_1deval_params(
        del_=del_,
        start=start,
        num=num,
        index=index,
        v_1_d=v_1_d,
        symbols=symbols,
        symbol_values=symbol_values,
        expression=expression,
    )
    return v_1deval_execute(params, execution)


__all__ = [
    "V1devalOutputs",
    "V1devalParameters",
    "V_1DEVAL_METADATA",
    "v_1deval",
    "v_1deval_params",
]
