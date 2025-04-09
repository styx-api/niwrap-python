# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DEFECT2SEG_METADATA = Metadata(
    id="ee34539fd2b9014ec765deedfc67dab265d637bf.boutiques",
    name="defect2seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Defect2segParameters = typing.TypedDict('Defect2segParameters', {
    "__STYX_TYPE__": typing.Literal["defect2seg"],
    "output_seg": str,
    "template": InputPathType,
    "left_hemisphere": typing.NotRequired[list[str] | None],
    "right_hemisphere": typing.NotRequired[list[str] | None],
    "subject": typing.NotRequired[str | None],
    "lh_only": bool,
    "rh_only": bool,
    "cortex": bool,
    "no_cortex": bool,
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
        "defect2seg": defect2seg_cargs,
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
        "defect2seg": defect2seg_outputs,
    }.get(t)


class Defect2segOutputs(typing.NamedTuple):
    """
    Output object returned when calling `defect2seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_segmentation: OutputPathType
    """Resulting defect segmentation volume"""


def defect2seg_params(
    output_seg: str,
    template: InputPathType,
    left_hemisphere: list[str] | None = None,
    right_hemisphere: list[str] | None = None,
    subject: str | None = None,
    lh_only: bool = False,
    rh_only: bool = False,
    cortex: bool = False,
    no_cortex: bool = False,
) -> Defect2segParameters:
    """
    Build parameters.
    
    Args:
        output_seg: Output segmentation volume.
        template: Template for segmentation.
        left_hemisphere: Left hemisphere inputs: surface, defect labels,\
            pointset, and offset.
        right_hemisphere: Right hemisphere inputs: surface, defect labels,\
            pointset, and offset.
        subject: Subject identifier, sets default values for other parameters.
        lh_only: Consider only left hemisphere defects.
        rh_only: Consider only right hemisphere defects.
        cortex: Constrain defects to within cortex.
        no_cortex: Allow defects outside of cortex.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "defect2seg",
        "output_seg": output_seg,
        "template": template,
        "lh_only": lh_only,
        "rh_only": rh_only,
        "cortex": cortex,
        "no_cortex": no_cortex,
    }
    if left_hemisphere is not None:
        params["left_hemisphere"] = left_hemisphere
    if right_hemisphere is not None:
        params["right_hemisphere"] = right_hemisphere
    if subject is not None:
        params["subject"] = subject
    return params


def defect2seg_cargs(
    params: Defect2segParameters,
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
    cargs.append("defect2seg")
    cargs.extend([
        "--o",
        params.get("output_seg")
    ])
    cargs.extend([
        "--t",
        execution.input_file(params.get("template"))
    ])
    if params.get("left_hemisphere") is not None:
        cargs.extend([
            "--lh",
            *params.get("left_hemisphere")
        ])
    if params.get("right_hemisphere") is not None:
        cargs.extend([
            "--rh",
            *params.get("right_hemisphere")
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("lh_only"):
        cargs.append("--lh-only")
    if params.get("rh_only"):
        cargs.append("--rh-only")
    if params.get("cortex"):
        cargs.append("--cortex")
    if params.get("no_cortex"):
        cargs.append("--no-cortex")
    return cargs


def defect2seg_outputs(
    params: Defect2segParameters,
    execution: Execution,
) -> Defect2segOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Defect2segOutputs(
        root=execution.output_file("."),
        output_segmentation=execution.output_file(params.get("output_seg")),
    )
    return ret


def defect2seg_execute(
    params: Defect2segParameters,
    execution: Execution,
) -> Defect2segOutputs:
    """
    Converts surface defect labels into a segmentation volume and pointsets.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Defect2segOutputs`).
    """
    params = execution.params(params)
    cargs = defect2seg_cargs(params, execution)
    ret = defect2seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def defect2seg(
    output_seg: str,
    template: InputPathType,
    left_hemisphere: list[str] | None = None,
    right_hemisphere: list[str] | None = None,
    subject: str | None = None,
    lh_only: bool = False,
    rh_only: bool = False,
    cortex: bool = False,
    no_cortex: bool = False,
    runner: Runner | None = None,
) -> Defect2segOutputs:
    """
    Converts surface defect labels into a segmentation volume and pointsets.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_seg: Output segmentation volume.
        template: Template for segmentation.
        left_hemisphere: Left hemisphere inputs: surface, defect labels,\
            pointset, and offset.
        right_hemisphere: Right hemisphere inputs: surface, defect labels,\
            pointset, and offset.
        subject: Subject identifier, sets default values for other parameters.
        lh_only: Consider only left hemisphere defects.
        rh_only: Consider only right hemisphere defects.
        cortex: Constrain defects to within cortex.
        no_cortex: Allow defects outside of cortex.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Defect2segOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DEFECT2SEG_METADATA)
    params = defect2seg_params(
        output_seg=output_seg,
        template=template,
        left_hemisphere=left_hemisphere,
        right_hemisphere=right_hemisphere,
        subject=subject,
        lh_only=lh_only,
        rh_only=rh_only,
        cortex=cortex,
        no_cortex=no_cortex,
    )
    return defect2seg_execute(params, execution)


__all__ = [
    "DEFECT2SEG_METADATA",
    "Defect2segOutputs",
    "Defect2segParameters",
    "defect2seg",
    "defect2seg_params",
]
