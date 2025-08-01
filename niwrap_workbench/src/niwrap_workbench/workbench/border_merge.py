# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BORDER_MERGE_METADATA = Metadata(
    id="b78808fafe6b76e1dfc48d8e5c0856430f0c2bb6.boutiques",
    name="border-merge",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


BorderMergeUpToParameters = typing.TypedDict('BorderMergeUpToParameters', {
    "__STYXTYPE__": typing.Literal["up_to"],
    "last_border": str,
    "opt_reverse": bool,
})


BorderMergeSelectParameters = typing.TypedDict('BorderMergeSelectParameters', {
    "__STYXTYPE__": typing.Literal["select"],
    "border": str,
    "up_to": typing.NotRequired[BorderMergeUpToParameters | None],
})


BorderMergeBorderParameters = typing.TypedDict('BorderMergeBorderParameters', {
    "__STYXTYPE__": typing.Literal["border"],
    "border_file_in": InputPathType,
    "select": typing.NotRequired[list[BorderMergeSelectParameters] | None],
})


BorderMergeParameters = typing.TypedDict('BorderMergeParameters', {
    "__STYXTYPE__": typing.Literal["border-merge"],
    "border_file_out": str,
    "border": typing.NotRequired[list[BorderMergeBorderParameters] | None],
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
        "border-merge": border_merge_cargs,
        "border": border_merge_border_cargs,
        "select": border_merge_select_cargs,
        "up_to": border_merge_up_to_cargs,
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
        "border-merge": border_merge_outputs,
    }.get(t)


def border_merge_up_to_params(
    last_border: str,
    opt_reverse: bool = False,
) -> BorderMergeUpToParameters:
    """
    Build parameters.
    
    Args:
        last_border: the number or name of the last column to include.
        opt_reverse: use the range in reverse order.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "up_to",
        "last_border": last_border,
        "opt_reverse": opt_reverse,
    }
    return params


def border_merge_up_to_cargs(
    params: BorderMergeUpToParameters,
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
    cargs.append("-up-to")
    cargs.append(params.get("last_border"))
    if params.get("opt_reverse"):
        cargs.append("-reverse")
    return cargs


def border_merge_select_params(
    border: str,
    up_to: BorderMergeUpToParameters | None = None,
) -> BorderMergeSelectParameters:
    """
    Build parameters.
    
    Args:
        border: the border number or name.
        up_to: use an inclusive range of borders.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "select",
        "border": border,
    }
    if up_to is not None:
        params["up_to"] = up_to
    return params


def border_merge_select_cargs(
    params: BorderMergeSelectParameters,
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
    cargs.append("-select")
    cargs.append(params.get("border"))
    if params.get("up_to") is not None:
        cargs.extend(dyn_cargs(params.get("up_to")["__STYXTYPE__"])(params.get("up_to"), execution))
    return cargs


def border_merge_border_params(
    border_file_in: InputPathType,
    select_: list[BorderMergeSelectParameters] | None = None,
) -> BorderMergeBorderParameters:
    """
    Build parameters.
    
    Args:
        border_file_in: a border file to use borders from.
        select_: select a single border to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border",
        "border_file_in": border_file_in,
    }
    if select_ is not None:
        params["select"] = select_
    return params


def border_merge_border_cargs(
    params: BorderMergeBorderParameters,
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
    cargs.append("-border")
    cargs.append(execution.input_file(params.get("border_file_in")))
    if params.get("select") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("select")] for a in c])
    return cargs


class BorderMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_file_out: OutputPathType
    """the output border file"""


def border_merge_params(
    border_file_out: str,
    border: list[BorderMergeBorderParameters] | None = None,
) -> BorderMergeParameters:
    """
    Build parameters.
    
    Args:
        border_file_out: the output border file.
        border: specify an input border file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border-merge",
        "border_file_out": border_file_out,
    }
    if border is not None:
        params["border"] = border
    return params


def border_merge_cargs(
    params: BorderMergeParameters,
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
    cargs.append("wb_command")
    cargs.append("-border-merge")
    cargs.append(params.get("border_file_out"))
    if params.get("border") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("border")] for a in c])
    return cargs


def border_merge_outputs(
    params: BorderMergeParameters,
    execution: Execution,
) -> BorderMergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BorderMergeOutputs(
        root=execution.output_file("."),
        border_file_out=execution.output_file(params.get("border_file_out")),
    )
    return ret


def border_merge_execute(
    params: BorderMergeParameters,
    execution: Execution,
) -> BorderMergeOutputs:
    """
    Merge border files into a new file.
    
    Takes one or more border files and makes a new border file from the borders
    in them.
    
    Example: wb_command -border-merge out.border -border first.border -select 1
    -border second.border
    
    This example would take the first border from first.border, followed by all
    borders from second.border, and write these to out.border.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BorderMergeOutputs`).
    """
    params = execution.params(params)
    cargs = border_merge_cargs(params, execution)
    ret = border_merge_outputs(params, execution)
    execution.run(cargs)
    return ret


def border_merge(
    border_file_out: str,
    border: list[BorderMergeBorderParameters] | None = None,
    runner: Runner | None = None,
) -> BorderMergeOutputs:
    """
    Merge border files into a new file.
    
    Takes one or more border files and makes a new border file from the borders
    in them.
    
    Example: wb_command -border-merge out.border -border first.border -select 1
    -border second.border
    
    This example would take the first border from first.border, followed by all
    borders from second.border, and write these to out.border.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        border_file_out: the output border file.
        border: specify an input border file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_MERGE_METADATA)
    params = border_merge_params(
        border_file_out=border_file_out,
        border=border,
    )
    return border_merge_execute(params, execution)


__all__ = [
    "BORDER_MERGE_METADATA",
    "BorderMergeBorderParameters",
    "BorderMergeOutputs",
    "BorderMergeParameters",
    "BorderMergeSelectParameters",
    "BorderMergeUpToParameters",
    "border_merge",
    "border_merge_border_params",
    "border_merge_params",
    "border_merge_select_params",
    "border_merge_up_to_params",
]
