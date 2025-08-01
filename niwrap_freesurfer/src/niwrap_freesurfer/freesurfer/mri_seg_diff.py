# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SEG_DIFF_METADATA = Metadata(
    id="78f61554c72a9c79a5a960acc4e0438704b93d91.boutiques",
    name="mri_seg_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSegDiffParameters = typing.TypedDict('MriSegDiffParameters', {
    "__STYXTYPE__": typing.Literal["mri_seg_diff"],
    "seg1": typing.NotRequired[InputPathType | None],
    "seg2": typing.NotRequired[InputPathType | None],
    "seg": typing.NotRequired[InputPathType | None],
    "diff": str,
    "diff_in": typing.NotRequired[InputPathType | None],
    "merged": typing.NotRequired[str | None],
    "diff_force": bool,
    "debug": bool,
    "checkopts": bool,
    "version": bool,
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
        "mri_seg_diff": mri_seg_diff_cargs,
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
        "mri_seg_diff": mri_seg_diff_outputs,
    }.get(t)


class MriSegDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_seg_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    diff_output: OutputPathType
    """Output diff segmentation file."""
    merged_output: OutputPathType | None
    """Output merged segmentation file."""


def mri_seg_diff_params(
    diff: str,
    seg1: InputPathType | None = None,
    seg2: InputPathType | None = None,
    seg: InputPathType | None = None,
    diff_in: InputPathType | None = None,
    merged: str | None = None,
    diff_force: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    version: bool = False,
) -> MriSegDiffParameters:
    """
    Build parameters.
    
    Args:
        diff: Output diff segmentation volume.
        seg1: First segmentation file (e.g., unedited).
        seg2: Second segmentation file (e.g., edited).
        seg: Source segmentation file (e.g., unedited).
        diff_in: Input diff segmentation volume.
        merged: Merged output, combining unedited with diff.
        diff_force: Force creation of a diff even if no diff is detected.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
        version: Print out version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_seg_diff",
        "diff": diff,
        "diff_force": diff_force,
        "debug": debug,
        "checkopts": checkopts,
        "version": version,
    }
    if seg1 is not None:
        params["seg1"] = seg1
    if seg2 is not None:
        params["seg2"] = seg2
    if seg is not None:
        params["seg"] = seg
    if diff_in is not None:
        params["diff_in"] = diff_in
    if merged is not None:
        params["merged"] = merged
    return params


def mri_seg_diff_cargs(
    params: MriSegDiffParameters,
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
    cargs.append("mri_seg_diff")
    if params.get("seg1") is not None:
        cargs.extend([
            "--seg1",
            execution.input_file(params.get("seg1"))
        ])
    if params.get("seg2") is not None:
        cargs.extend([
            "--seg2",
            execution.input_file(params.get("seg2"))
        ])
    if params.get("seg") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("seg"))
        ])
    cargs.extend([
        "--diff",
        params.get("diff")
    ])
    if params.get("diff_in") is not None:
        cargs.extend([
            "--diff-in",
            execution.input_file(params.get("diff_in"))
        ])
    if params.get("merged") is not None:
        cargs.extend([
            "--merged",
            params.get("merged")
        ])
    if params.get("diff_force"):
        cargs.append("--diff-force")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_seg_diff_outputs(
    params: MriSegDiffParameters,
    execution: Execution,
) -> MriSegDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSegDiffOutputs(
        root=execution.output_file("."),
        diff_output=execution.output_file(params.get("diff")),
        merged_output=execution.output_file(params.get("merged")) if (params.get("merged") is not None) else None,
    )
    return ret


def mri_seg_diff_execute(
    params: MriSegDiffParameters,
    execution: Execution,
) -> MriSegDiffOutputs:
    """
    This program computes and merges differences in segmentation volumes, primarily
    for managing manual edits in FreeSurfer's aseg.mgz.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSegDiffOutputs`).
    """
    params = execution.params(params)
    cargs = mri_seg_diff_cargs(params, execution)
    ret = mri_seg_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_seg_diff(
    diff: str,
    seg1: InputPathType | None = None,
    seg2: InputPathType | None = None,
    seg: InputPathType | None = None,
    diff_in: InputPathType | None = None,
    merged: str | None = None,
    diff_force: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriSegDiffOutputs:
    """
    This program computes and merges differences in segmentation volumes, primarily
    for managing manual edits in FreeSurfer's aseg.mgz.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        diff: Output diff segmentation volume.
        seg1: First segmentation file (e.g., unedited).
        seg2: Second segmentation file (e.g., edited).
        seg: Source segmentation file (e.g., unedited).
        diff_in: Input diff segmentation volume.
        merged: Merged output, combining unedited with diff.
        diff_force: Force creation of a diff even if no diff is detected.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEG_DIFF_METADATA)
    params = mri_seg_diff_params(
        seg1=seg1,
        seg2=seg2,
        seg=seg,
        diff=diff,
        diff_in=diff_in,
        merged=merged,
        diff_force=diff_force,
        debug=debug,
        checkopts=checkopts,
        version=version,
    )
    return mri_seg_diff_execute(params, execution)


__all__ = [
    "MRI_SEG_DIFF_METADATA",
    "MriSegDiffOutputs",
    "MriSegDiffParameters",
    "mri_seg_diff",
    "mri_seg_diff_params",
]
