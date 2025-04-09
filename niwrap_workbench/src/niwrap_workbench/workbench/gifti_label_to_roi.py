# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GIFTI_LABEL_TO_ROI_METADATA = Metadata(
    id="fbd577d7a4881455906a02f5415f91e4912c0e7b.boutiques",
    name="gifti-label-to-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


GiftiLabelToRoiParameters = typing.TypedDict('GiftiLabelToRoiParameters', {
    "__STYX_TYPE__": typing.Literal["gifti-label-to-roi"],
    "label_in": InputPathType,
    "metric_out": str,
    "opt_name_label_name": typing.NotRequired[str | None],
    "opt_key_label_key": typing.NotRequired[int | None],
    "opt_map_map": typing.NotRequired[str | None],
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
        "gifti-label-to-roi": gifti_label_to_roi_cargs,
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
        "gifti-label-to-roi": gifti_label_to_roi_outputs,
    }.get(t)


class GiftiLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_label_to_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def gifti_label_to_roi_params(
    label_in: InputPathType,
    metric_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
) -> GiftiLabelToRoiParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input gifti label file.
        metric_out: the output metric file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gifti-label-to-roi",
        "label_in": label_in,
        "metric_out": metric_out,
    }
    if opt_name_label_name is not None:
        params["opt_name_label_name"] = opt_name_label_name
    if opt_key_label_key is not None:
        params["opt_key_label_key"] = opt_key_label_key
    if opt_map_map is not None:
        params["opt_map_map"] = opt_map_map
    return params


def gifti_label_to_roi_cargs(
    params: GiftiLabelToRoiParameters,
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
    cargs.append("-gifti-label-to-roi")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_name_label_name") is not None:
        cargs.extend([
            "-name",
            params.get("opt_name_label_name")
        ])
    if params.get("opt_key_label_key") is not None:
        cargs.extend([
            "-key",
            str(params.get("opt_key_label_key"))
        ])
    if params.get("opt_map_map") is not None:
        cargs.extend([
            "-map",
            params.get("opt_map_map")
        ])
    return cargs


def gifti_label_to_roi_outputs(
    params: GiftiLabelToRoiParameters,
    execution: Execution,
) -> GiftiLabelToRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GiftiLabelToRoiOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def gifti_label_to_roi_execute(
    params: GiftiLabelToRoiParameters,
    execution: Execution,
) -> GiftiLabelToRoiOutputs:
    """
    Make a gifti label into an roi metric.
    
    For each map in <label-in>, a map is created in <metric-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GiftiLabelToRoiOutputs`).
    """
    params = execution.params(params)
    cargs = gifti_label_to_roi_cargs(params, execution)
    ret = gifti_label_to_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def gifti_label_to_roi(
    label_in: InputPathType,
    metric_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
    runner: Runner | None = None,
) -> GiftiLabelToRoiOutputs:
    """
    Make a gifti label into an roi metric.
    
    For each map in <label-in>, a map is created in <metric-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input gifti label file.
        metric_out: the output metric file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GiftiLabelToRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_LABEL_TO_ROI_METADATA)
    params = gifti_label_to_roi_params(
        label_in=label_in,
        metric_out=metric_out,
        opt_name_label_name=opt_name_label_name,
        opt_key_label_key=opt_key_label_key,
        opt_map_map=opt_map_map,
    )
    return gifti_label_to_roi_execute(params, execution)


__all__ = [
    "GIFTI_LABEL_TO_ROI_METADATA",
    "GiftiLabelToRoiOutputs",
    "GiftiLabelToRoiParameters",
    "gifti_label_to_roi",
    "gifti_label_to_roi_params",
]
