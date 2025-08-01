# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DCALC_METADATA = Metadata(
    id="34983276632d5f12085998aa5812bfe380a32306.boutiques",
    name="3dcalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dcalcParameters = typing.TypedDict('V3dcalcParameters', {
    "__STYXTYPE__": typing.Literal["3dcalc"],
    "in_file_a": InputPathType,
    "in_file_b": typing.NotRequired[InputPathType | None],
    "in_file_c": typing.NotRequired[InputPathType | None],
    "other": typing.NotRequired[InputPathType | None],
    "overwrite": bool,
    "single_idx": typing.NotRequired[int | None],
    "start_idx": typing.NotRequired[int | None],
    "stop_idx": typing.NotRequired[int | None],
    "expr": str,
    "prefix": typing.NotRequired[str | None],
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
        "3dcalc": v_3dcalc_cargs,
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
        "3dcalc": v_3dcalc_outputs,
    }.get(t)


class V3dcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output image file name."""


def v_3dcalc_params(
    in_file_a: InputPathType,
    expr: str,
    in_file_b: InputPathType | None = None,
    in_file_c: InputPathType | None = None,
    other: InputPathType | None = None,
    overwrite: bool = False,
    single_idx: int | None = None,
    start_idx: int | None = None,
    stop_idx: int | None = None,
    prefix: str | None = None,
) -> V3dcalcParameters:
    """
    Build parameters.
    
    Args:
        in_file_a: Input file to 3dcalc.
        expr: Expr.
        in_file_b: Operand file to 3dcalc.
        in_file_c: Operand file to 3dcalc.
        other: Other options.
        overwrite: Overwrite output.
        single_idx: Volume index for in_file_a.
        start_idx: Start index for in_file_a.
        stop_idx: Stop index for in_file_a.
        prefix: Output image file name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dcalc",
        "in_file_a": in_file_a,
        "overwrite": overwrite,
        "expr": expr,
    }
    if in_file_b is not None:
        params["in_file_b"] = in_file_b
    if in_file_c is not None:
        params["in_file_c"] = in_file_c
    if other is not None:
        params["other"] = other
    if single_idx is not None:
        params["single_idx"] = single_idx
    if start_idx is not None:
        params["start_idx"] = start_idx
    if stop_idx is not None:
        params["stop_idx"] = stop_idx
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3dcalc_cargs(
    params: V3dcalcParameters,
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
    cargs.append("3dcalc")
    cargs.extend([
        "-a",
        execution.input_file(params.get("in_file_a"))
    ])
    if params.get("in_file_b") is not None:
        cargs.extend([
            "-b",
            execution.input_file(params.get("in_file_b"))
        ])
    if params.get("in_file_c") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("in_file_c"))
        ])
    if params.get("other") is not None:
        cargs.append(execution.input_file(params.get("other")))
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("single_idx") is not None:
        cargs.append(str(params.get("single_idx")))
    if params.get("start_idx") is not None:
        cargs.append(str(params.get("start_idx")))
    if params.get("stop_idx") is not None:
        cargs.append(str(params.get("stop_idx")))
    cargs.extend([
        "-expr",
        params.get("expr")
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def v_3dcalc_outputs(
    params: V3dcalcParameters,
    execution: Execution,
) -> V3dcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dcalcOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3dcalc_execute(
    params: V3dcalcParameters,
    execution: Execution,
) -> V3dcalcOutputs:
    """
    AFNI's calculator program.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dcalcOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dcalc_cargs(params, execution)
    ret = v_3dcalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dcalc(
    in_file_a: InputPathType,
    expr: str,
    in_file_b: InputPathType | None = None,
    in_file_c: InputPathType | None = None,
    other: InputPathType | None = None,
    overwrite: bool = False,
    single_idx: int | None = None,
    start_idx: int | None = None,
    stop_idx: int | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dcalcOutputs:
    """
    AFNI's calculator program.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file_a: Input file to 3dcalc.
        expr: Expr.
        in_file_b: Operand file to 3dcalc.
        in_file_c: Operand file to 3dcalc.
        other: Other options.
        overwrite: Overwrite output.
        single_idx: Volume index for in_file_a.
        start_idx: Start index for in_file_a.
        stop_idx: Stop index for in_file_a.
        prefix: Output image file name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCALC_METADATA)
    params = v_3dcalc_params(
        in_file_a=in_file_a,
        in_file_b=in_file_b,
        in_file_c=in_file_c,
        other=other,
        overwrite=overwrite,
        single_idx=single_idx,
        start_idx=start_idx,
        stop_idx=stop_idx,
        expr=expr,
        prefix=prefix,
    )
    return v_3dcalc_execute(params, execution)


__all__ = [
    "V3dcalcOutputs",
    "V3dcalcParameters",
    "V_3DCALC_METADATA",
    "v_3dcalc",
    "v_3dcalc_params",
]
