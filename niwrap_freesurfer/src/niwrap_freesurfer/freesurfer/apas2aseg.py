# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APAS2ASEG_METADATA = Metadata(
    id="eda1865146654f4bd355ad2e45b11e2c26036db4.boutiques",
    name="apas2aseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Apas2asegParameters = typing.TypedDict('Apas2asegParameters', {
    "__STYXTYPE__": typing.Literal["apas2aseg"],
    "subject": typing.NotRequired[str | None],
    "input_aparc_aseg": typing.NotRequired[InputPathType | None],
    "output_seg": typing.NotRequired[str | None],
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
        "apas2aseg": apas2aseg_cargs,
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
        "apas2aseg": apas2aseg_outputs,
    }.get(t)


class Apas2asegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apas2aseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_seg_file: OutputPathType | None
    """The output segmentation file resulting from the conversion process."""


def apas2aseg_params(
    subject: str | None = None,
    input_aparc_aseg: InputPathType | None = None,
    output_seg: str | None = "apas-aseg.mgz",
) -> Apas2asegParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier specifying the directory where the\
            subject's data is stored.
        input_aparc_aseg: Input aparc+aseg.mgz file to be converted.
        output_seg: Output file for the new segmentation (e.g., apas-aseg.mgz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "apas2aseg",
    }
    if subject is not None:
        params["subject"] = subject
    if input_aparc_aseg is not None:
        params["input_aparc_aseg"] = input_aparc_aseg
    if output_seg is not None:
        params["output_seg"] = output_seg
    return params


def apas2aseg_cargs(
    params: Apas2asegParameters,
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
    cargs.append("apas2aseg")
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("input_aparc_aseg") is not None:
        cargs.extend([
            "--i",
            execution.input_file(params.get("input_aparc_aseg"))
        ])
    if params.get("output_seg") is not None:
        cargs.extend([
            "--o",
            params.get("output_seg")
        ])
    return cargs


def apas2aseg_outputs(
    params: Apas2asegParameters,
    execution: Execution,
) -> Apas2asegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Apas2asegOutputs(
        root=execution.output_file("."),
        output_seg_file=execution.output_file(params.get("output_seg")) if (params.get("output_seg") is not None) else None,
    )
    return ret


def apas2aseg_execute(
    params: Apas2asegParameters,
    execution: Execution,
) -> Apas2asegOutputs:
    """
    Converts aparc+aseg.mgz into aseg.mgz-like format by replacing specific cortical
    segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Apas2asegOutputs`).
    """
    params = execution.params(params)
    cargs = apas2aseg_cargs(params, execution)
    ret = apas2aseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def apas2aseg(
    subject: str | None = None,
    input_aparc_aseg: InputPathType | None = None,
    output_seg: str | None = "apas-aseg.mgz",
    runner: Runner | None = None,
) -> Apas2asegOutputs:
    """
    Converts aparc+aseg.mgz into aseg.mgz-like format by replacing specific cortical
    segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier specifying the directory where the\
            subject's data is stored.
        input_aparc_aseg: Input aparc+aseg.mgz file to be converted.
        output_seg: Output file for the new segmentation (e.g., apas-aseg.mgz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Apas2asegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APAS2ASEG_METADATA)
    params = apas2aseg_params(
        subject=subject,
        input_aparc_aseg=input_aparc_aseg,
        output_seg=output_seg,
    )
    return apas2aseg_execute(params, execution)


__all__ = [
    "APAS2ASEG_METADATA",
    "Apas2asegOutputs",
    "Apas2asegParameters",
    "apas2aseg",
    "apas2aseg_params",
]
