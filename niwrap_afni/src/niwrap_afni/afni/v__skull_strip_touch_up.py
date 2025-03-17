# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SKULL_STRIP_TOUCH_UP_METADATA = Metadata(
    id="460010f2b657da6818c5cc52af6697286e7b7fd3.boutiques",
    name="@SkullStrip_TouchUp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VSkullStripTouchUpParameters = typing.TypedDict('VSkullStripTouchUpParameters', {
    "__STYX_TYPE__": typing.Literal["@SkullStrip_TouchUp"],
    "prefix": str,
    "brain_dataset": InputPathType,
    "head_dataset": InputPathType,
    "mask_out": bool,
    "orig_dim": bool,
    "help": bool,
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
        "@SkullStrip_TouchUp": v__skull_strip_touch_up_cargs,
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
        "@SkullStrip_TouchUp": v__skull_strip_touch_up_outputs,
    }.get(t)


class VSkullStripTouchUpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__skull_strip_touch_up(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_folder: OutputPathType
    """Output folder containing the touch-up results"""
    output_mask: OutputPathType
    """Output binary mask (if -mask_out flag is used)"""


def v__skull_strip_touch_up_params(
    prefix: str,
    brain_dataset: InputPathType,
    head_dataset: InputPathType,
    mask_out: bool = False,
    orig_dim: bool = False,
    help_: bool = False,
) -> VSkullStripTouchUpParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file and folder name.
        brain_dataset: Skull stripped data set to touch up.
        head_dataset: Whole head anatomical data set.
        mask_out: Output a binary mask in addition to actual data.
        orig_dim: Edit in the original image dimensions.
        help_: Show this help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@SkullStrip_TouchUp",
        "prefix": prefix,
        "brain_dataset": brain_dataset,
        "head_dataset": head_dataset,
        "mask_out": mask_out,
        "orig_dim": orig_dim,
        "help": help_,
    }
    return params


def v__skull_strip_touch_up_cargs(
    params: VSkullStripTouchUpParameters,
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
    cargs.append("@SkullStrip_TouchUp")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-brain",
        execution.input_file(params.get("brain_dataset"))
    ])
    cargs.extend([
        "-head",
        execution.input_file(params.get("head_dataset"))
    ])
    if params.get("mask_out"):
        cargs.append("-mask_out")
    if params.get("orig_dim"):
        cargs.append("-orig_dim")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__skull_strip_touch_up_outputs(
    params: VSkullStripTouchUpParameters,
    execution: Execution,
) -> VSkullStripTouchUpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSkullStripTouchUpOutputs(
        root=execution.output_file("."),
        output_folder=execution.output_file(params.get("prefix") + "_SS_touch_up"),
        output_mask=execution.output_file(params.get("prefix") + "_mask.nii.gz"),
    )
    return ret


def v__skull_strip_touch_up_execute(
    params: VSkullStripTouchUpParameters,
    execution: Execution,
) -> VSkullStripTouchUpOutputs:
    """
    Helper program to touch up failed skull stripping by resampling data, allowing
    manual edits, and outputting corrected data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSkullStripTouchUpOutputs`).
    """
    params = execution.params(params)
    cargs = v__skull_strip_touch_up_cargs(params, execution)
    ret = v__skull_strip_touch_up_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__skull_strip_touch_up(
    prefix: str,
    brain_dataset: InputPathType,
    head_dataset: InputPathType,
    mask_out: bool = False,
    orig_dim: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VSkullStripTouchUpOutputs:
    """
    Helper program to touch up failed skull stripping by resampling data, allowing
    manual edits, and outputting corrected data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file and folder name.
        brain_dataset: Skull stripped data set to touch up.
        head_dataset: Whole head anatomical data set.
        mask_out: Output a binary mask in addition to actual data.
        orig_dim: Edit in the original image dimensions.
        help_: Show this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSkullStripTouchUpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SKULL_STRIP_TOUCH_UP_METADATA)
    params = v__skull_strip_touch_up_params(
        prefix=prefix,
        brain_dataset=brain_dataset,
        head_dataset=head_dataset,
        mask_out=mask_out,
        orig_dim=orig_dim,
        help_=help_,
    )
    return v__skull_strip_touch_up_execute(params, execution)


__all__ = [
    "VSkullStripTouchUpOutputs",
    "VSkullStripTouchUpParameters",
    "V__SKULL_STRIP_TOUCH_UP_METADATA",
    "v__skull_strip_touch_up",
    "v__skull_strip_touch_up_params",
]
