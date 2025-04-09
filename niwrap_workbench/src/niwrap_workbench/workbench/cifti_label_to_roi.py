# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_LABEL_TO_ROI_METADATA = Metadata(
    id="f43e32f3613afb19c5aaf829734565b6d97fb5d7.boutiques",
    name="cifti-label-to-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiLabelToRoiParameters = typing.TypedDict('CiftiLabelToRoiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-label-to-roi"],
    "label_in": InputPathType,
    "scalar_out": str,
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
        "cifti-label-to-roi": cifti_label_to_roi_cargs,
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
        "cifti-label-to-roi": cifti_label_to_roi_outputs,
    }.get(t)


class CiftiLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_to_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    scalar_out: OutputPathType
    """the output cifti scalar file"""


def cifti_label_to_roi_params(
    label_in: InputPathType,
    scalar_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
) -> CiftiLabelToRoiParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input cifti label file.
        scalar_out: the output cifti scalar file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-label-to-roi",
        "label_in": label_in,
        "scalar_out": scalar_out,
    }
    if opt_name_label_name is not None:
        params["opt_name_label_name"] = opt_name_label_name
    if opt_key_label_key is not None:
        params["opt_key_label_key"] = opt_key_label_key
    if opt_map_map is not None:
        params["opt_map_map"] = opt_map_map
    return params


def cifti_label_to_roi_cargs(
    params: CiftiLabelToRoiParameters,
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
    cargs.append("-cifti-label-to-roi")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("scalar_out"))
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


def cifti_label_to_roi_outputs(
    params: CiftiLabelToRoiParameters,
    execution: Execution,
) -> CiftiLabelToRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiLabelToRoiOutputs(
        root=execution.output_file("."),
        scalar_out=execution.output_file(params.get("scalar_out")),
    )
    return ret


def cifti_label_to_roi_execute(
    params: CiftiLabelToRoiParameters,
    execution: Execution,
) -> CiftiLabelToRoiOutputs:
    """
    Make a cifti label into an roi.
    
    For each map in <label-in>, a map is created in <scalar-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelToRoiOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_label_to_roi_cargs(params, execution)
    ret = cifti_label_to_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_label_to_roi(
    label_in: InputPathType,
    scalar_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
    runner: Runner | None = None,
) -> CiftiLabelToRoiOutputs:
    """
    Make a cifti label into an roi.
    
    For each map in <label-in>, a map is created in <scalar-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input cifti label file.
        scalar_out: the output cifti scalar file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelToRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_TO_ROI_METADATA)
    params = cifti_label_to_roi_params(
        label_in=label_in,
        scalar_out=scalar_out,
        opt_name_label_name=opt_name_label_name,
        opt_key_label_key=opt_key_label_key,
        opt_map_map=opt_map_map,
    )
    return cifti_label_to_roi_execute(params, execution)


__all__ = [
    "CIFTI_LABEL_TO_ROI_METADATA",
    "CiftiLabelToRoiOutputs",
    "CiftiLabelToRoiParameters",
    "cifti_label_to_roi",
    "cifti_label_to_roi_params",
]
