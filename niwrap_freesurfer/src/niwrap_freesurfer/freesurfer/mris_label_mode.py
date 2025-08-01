# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_LABEL_MODE_METADATA = Metadata(
    id="591967f9eeb3bb3b9f31868769d0fb3d8379053f.boutiques",
    name="mris_label_mode",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisLabelModeParameters = typing.TypedDict('MrisLabelModeParameters', {
    "__STYXTYPE__": typing.Literal["mris_label_mode"],
    "input_curv_file": InputPathType,
    "hemi": str,
    "surface": str,
    "subject": list[str],
    "output_curv_file": str,
    "summary_statistics": bool,
    "statistics_cond": typing.NotRequired[str | None],
    "output_directory": typing.NotRequired[str | None],
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
        "mris_label_mode": mris_label_mode_cargs,
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


class MrisLabelModeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label_mode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_label_mode_params(
    input_curv_file: InputPathType,
    hemi: str,
    surface: str,
    subject: list[str],
    output_curv_file: str,
    summary_statistics: bool = False,
    statistics_cond: str | None = None,
    output_directory: str | None = None,
) -> MrisLabelModeParameters:
    """
    Build parameters.
    
    Args:
        input_curv_file: Input curvature file.
        hemi: Hemisphere.
        surface: Surface name.
        subject: Subject name(s).
        output_curv_file: Output curvature file.
        summary_statistics: Generate summary statistics.
        statistics_cond: Condition number for summary statistics.
        output_directory: Override the last subject as the output surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_label_mode",
        "input_curv_file": input_curv_file,
        "hemi": hemi,
        "surface": surface,
        "subject": subject,
        "output_curv_file": output_curv_file,
        "summary_statistics": summary_statistics,
    }
    if statistics_cond is not None:
        params["statistics_cond"] = statistics_cond
    if output_directory is not None:
        params["output_directory"] = output_directory
    return params


def mris_label_mode_cargs(
    params: MrisLabelModeParameters,
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
    cargs.append("mris_label_mode")
    cargs.append(execution.input_file(params.get("input_curv_file")))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface"))
    cargs.extend(params.get("subject"))
    cargs.append(params.get("output_curv_file"))
    if params.get("summary_statistics"):
        cargs.append("-s")
    if params.get("statistics_cond") is not None:
        cargs.append(params.get("statistics_cond"))
    if params.get("output_directory") is not None:
        cargs.extend([
            "-o",
            params.get("output_directory")
        ])
    return cargs


def mris_label_mode_outputs(
    params: MrisLabelModeParameters,
    execution: Execution,
) -> MrisLabelModeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisLabelModeOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_label_mode_execute(
    params: MrisLabelModeParameters,
    execution: Execution,
) -> MrisLabelModeOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisLabelModeOutputs`).
    """
    params = execution.params(params)
    cargs = mris_label_mode_cargs(params, execution)
    ret = mris_label_mode_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_label_mode(
    input_curv_file: InputPathType,
    hemi: str,
    surface: str,
    subject: list[str],
    output_curv_file: str,
    summary_statistics: bool = False,
    statistics_cond: str | None = None,
    output_directory: str | None = None,
    runner: Runner | None = None,
) -> MrisLabelModeOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_curv_file: Input curvature file.
        hemi: Hemisphere.
        surface: Surface name.
        subject: Subject name(s).
        output_curv_file: Output curvature file.
        summary_statistics: Generate summary statistics.
        statistics_cond: Condition number for summary statistics.
        output_directory: Override the last subject as the output surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabelModeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL_MODE_METADATA)
    params = mris_label_mode_params(
        input_curv_file=input_curv_file,
        hemi=hemi,
        surface=surface,
        subject=subject,
        output_curv_file=output_curv_file,
        summary_statistics=summary_statistics,
        statistics_cond=statistics_cond,
        output_directory=output_directory,
    )
    return mris_label_mode_execute(params, execution)


__all__ = [
    "MRIS_LABEL_MODE_METADATA",
    "MrisLabelModeOutputs",
    "MrisLabelModeParameters",
    "mris_label_mode",
    "mris_label_mode_params",
]
