# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPUTE_OVERLAP_METADATA = Metadata(
    id="97d8d567d0e1c761a649f9ba5d647b7d4352a61b.boutiques",
    name="mri_compute_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriComputeOverlapParameters = typing.TypedDict('MriComputeOverlapParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compute_overlap"],
    "volumes": list[InputPathType],
    "label_numbers": typing.NotRequired[list[str] | None],
    "all_labels": bool,
    "show_label": bool,
    "total_overlap": bool,
    "no_summary": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "output_file": typing.NotRequired[str | None],
    "quiet_mode": bool,
    "translate_label": typing.NotRequired[list[float] | None],
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
        "mri_compute_overlap": mri_compute_overlap_cargs,
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
    }.get(t)


class MriComputeOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_compute_overlap_params(
    volumes: list[InputPathType],
    label_numbers: list[str] | None = None,
    all_labels: bool = False,
    show_label: bool = False,
    total_overlap: bool = False,
    no_summary: bool = False,
    mask: InputPathType | None = None,
    output_file: str | None = None,
    quiet_mode: bool = False,
    translate_label: list[float] | None = None,
    help_: bool = False,
) -> MriComputeOverlapParameters:
    """
    Build parameters.
    
    Args:
        volumes: Input volume files for which overlap measures are computed.
        label_numbers: List of specific label numbers for which to compute\
            overlap measures. If not specified, all labels are considered if -a is\
            provided.
        all_labels: Compute overlap for all labels.
        show_label: Show label name for segmentation.
        total_overlap: Compute the total overlap, which is the number of voxels\
            that are the same among all labels.
        no_summary: Do not compute total label summary.
        mask: Limit the domain of the calculation to the nonzero voxels in\
            specified volume.
        output_file: Filename to write results to.
        quiet_mode: Do not display results on standard display. If -l is\
            specified, this flag is automatically set.
        translate_label: Translate label l1 to label l2.
        help_: Print help.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_overlap",
        "volumes": volumes,
        "all_labels": all_labels,
        "show_label": show_label,
        "total_overlap": total_overlap,
        "no_summary": no_summary,
        "quiet_mode": quiet_mode,
        "help": help_,
    }
    if label_numbers is not None:
        params["label_numbers"] = label_numbers
    if mask is not None:
        params["mask"] = mask
    if output_file is not None:
        params["output_file"] = output_file
    if translate_label is not None:
        params["translate_label"] = translate_label
    return params


def mri_compute_overlap_cargs(
    params: MriComputeOverlapParameters,
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
    cargs.append("mri_compute_overlap")
    cargs.extend([execution.input_file(f) for f in params.get("volumes")])
    if params.get("label_numbers") is not None:
        cargs.extend(params.get("label_numbers"))
    if params.get("all_labels"):
        cargs.append("-a")
    if params.get("show_label"):
        cargs.append("-s")
    if params.get("total_overlap"):
        cargs.append("-total")
    if params.get("no_summary"):
        cargs.append("-nosummary")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-l",
            params.get("output_file")
        ])
    if params.get("quiet_mode"):
        cargs.append("-q")
    if params.get("translate_label") is not None:
        cargs.extend([
            "-t",
            *map(str, params.get("translate_label"))
        ])
    if params.get("help"):
        cargs.append("-h")
    return cargs


def mri_compute_overlap_outputs(
    params: MriComputeOverlapParameters,
    execution: Execution,
) -> MriComputeOverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeOverlapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_compute_overlap_execute(
    params: MriComputeOverlapParameters,
    execution: Execution,
) -> MriComputeOverlapOutputs:
    """
    Computes three different types of overlap measures for labels in input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeOverlapOutputs`).
    """
    params = execution.params(params)
    cargs = mri_compute_overlap_cargs(params, execution)
    ret = mri_compute_overlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_overlap(
    volumes: list[InputPathType],
    label_numbers: list[str] | None = None,
    all_labels: bool = False,
    show_label: bool = False,
    total_overlap: bool = False,
    no_summary: bool = False,
    mask: InputPathType | None = None,
    output_file: str | None = None,
    quiet_mode: bool = False,
    translate_label: list[float] | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriComputeOverlapOutputs:
    """
    Computes three different types of overlap measures for labels in input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volumes: Input volume files for which overlap measures are computed.
        label_numbers: List of specific label numbers for which to compute\
            overlap measures. If not specified, all labels are considered if -a is\
            provided.
        all_labels: Compute overlap for all labels.
        show_label: Show label name for segmentation.
        total_overlap: Compute the total overlap, which is the number of voxels\
            that are the same among all labels.
        no_summary: Do not compute total label summary.
        mask: Limit the domain of the calculation to the nonzero voxels in\
            specified volume.
        output_file: Filename to write results to.
        quiet_mode: Do not display results on standard display. If -l is\
            specified, this flag is automatically set.
        translate_label: Translate label l1 to label l2.
        help_: Print help.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_OVERLAP_METADATA)
    params = mri_compute_overlap_params(
        volumes=volumes,
        label_numbers=label_numbers,
        all_labels=all_labels,
        show_label=show_label,
        total_overlap=total_overlap,
        no_summary=no_summary,
        mask=mask,
        output_file=output_file,
        quiet_mode=quiet_mode,
        translate_label=translate_label,
        help_=help_,
    )
    return mri_compute_overlap_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_OVERLAP_METADATA",
    "MriComputeOverlapOutputs",
    "MriComputeOverlapParameters",
    "mri_compute_overlap",
    "mri_compute_overlap_params",
]
