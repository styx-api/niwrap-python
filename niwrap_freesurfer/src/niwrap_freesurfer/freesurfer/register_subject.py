# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REGISTER_SUBJECT_METADATA = Metadata(
    id="73901ff923fee339dbfc9565a4cb0066a06d8cbd.boutiques",
    name="register_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RegisterSubjectParameters = typing.TypedDict('RegisterSubjectParameters', {
    "__STYXTYPE__": typing.Literal["register_subject"],
    "input_volume": typing.NotRequired[InputPathType | None],
    "mask_volume": typing.NotRequired[InputPathType | None],
    "control_points": typing.NotRequired[str | None],
    "output_directory": typing.NotRequired[str | None],
    "log_file": typing.NotRequired[InputPathType | None],
    "gca_file": typing.NotRequired[InputPathType | None],
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
        "register_subject": register_subject_cargs,
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
        "register_subject": register_subject_outputs,
    }.get(t)


class RegisterSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `register_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    normalized_output: OutputPathType | None
    """Intensity normalized output volume."""
    transformed_fsamples: OutputPathType | None
    """Transformed control points."""


def register_subject_params(
    input_volume: InputPathType | None = None,
    mask_volume: InputPathType | None = None,
    control_points: str | None = None,
    output_directory: str | None = None,
    log_file: InputPathType | None = None,
    gca_file: InputPathType | None = None,
) -> RegisterSubjectParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume for registration (e.g., brain.mgz).
        mask_volume: MR volume used to mask input volume.
        control_points: Control points used for registration.
        output_directory: Directory to write output files (e.g., transformed\
            fsamples).
        log_file: Log file for recording registration results.
        gca_file: GCA file required for registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "register_subject",
    }
    if input_volume is not None:
        params["input_volume"] = input_volume
    if mask_volume is not None:
        params["mask_volume"] = mask_volume
    if control_points is not None:
        params["control_points"] = control_points
    if output_directory is not None:
        params["output_directory"] = output_directory
    if log_file is not None:
        params["log_file"] = log_file
    if gca_file is not None:
        params["gca_file"] = gca_file
    return params


def register_subject_cargs(
    params: RegisterSubjectParameters,
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
    cargs.append("register_subject")
    if params.get("input_volume") is not None:
        cargs.append(execution.input_file(params.get("input_volume")))
    if params.get("mask_volume") is not None:
        cargs.append(execution.input_file(params.get("mask_volume")))
    if params.get("control_points") is not None:
        cargs.append(params.get("control_points"))
    if params.get("output_directory") is not None:
        cargs.append(params.get("output_directory"))
    if params.get("log_file") is not None:
        cargs.append(execution.input_file(params.get("log_file")))
    if params.get("gca_file") is not None:
        cargs.append(execution.input_file(params.get("gca_file")))
    return cargs


def register_subject_outputs(
    params: RegisterSubjectParameters,
    execution: Execution,
) -> RegisterSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegisterSubjectOutputs(
        root=execution.output_file("."),
        normalized_output=execution.output_file(params.get("output_directory") + "/norm.mgz") if (params.get("output_directory") is not None) else None,
        transformed_fsamples=execution.output_file(params.get("output_directory") + "/fsamples") if (params.get("output_directory") is not None) else None,
    )
    return ret


def register_subject_execute(
    params: RegisterSubjectParameters,
    execution: Execution,
) -> RegisterSubjectOutputs:
    """
    Tool for registering brain MR volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegisterSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = register_subject_cargs(params, execution)
    ret = register_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def register_subject(
    input_volume: InputPathType | None = None,
    mask_volume: InputPathType | None = None,
    control_points: str | None = None,
    output_directory: str | None = None,
    log_file: InputPathType | None = None,
    gca_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> RegisterSubjectOutputs:
    """
    Tool for registering brain MR volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume for registration (e.g., brain.mgz).
        mask_volume: MR volume used to mask input volume.
        control_points: Control points used for registration.
        output_directory: Directory to write output files (e.g., transformed\
            fsamples).
        log_file: Log file for recording registration results.
        gca_file: GCA file required for registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegisterSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REGISTER_SUBJECT_METADATA)
    params = register_subject_params(
        input_volume=input_volume,
        mask_volume=mask_volume,
        control_points=control_points,
        output_directory=output_directory,
        log_file=log_file,
        gca_file=gca_file,
    )
    return register_subject_execute(params, execution)


__all__ = [
    "REGISTER_SUBJECT_METADATA",
    "RegisterSubjectOutputs",
    "RegisterSubjectParameters",
    "register_subject",
    "register_subject_params",
]
